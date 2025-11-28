import xml.etree.ElementTree as ET
import json
import os
import copy

import argparse

# Default Paths
# Calculate base directory relative to this script:
# script is in: flowchart-architect/skills/generate-drawio/script/
# base is 4 levels up
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../../../.."))

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate Draw.io flowchart from logic JSON.")
    parser.add_argument("--2l", dest="use_2_lane", action="store_true", help="Force use of 2-lane template")
    parser.add_argument("--3l", dest="use_3_lane", action="store_true", help="Force use of 3-lane template")
    parser.add_argument("--base_dir", default=DEFAULT_BASE_DIR, help="Base directory for the project")
    parser.add_argument("--logic_path", required=True, help="Path to the logic structure JSON file")
    parser.add_argument("--output_path", required=True, help="Path for the output Draw.io file")
    return parser.parse_args()

def load_xml(path):
    tree = ET.parse(path)
    return tree, tree.getroot()

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def get_swimlane_ids(root):
    return {
        "seq": "col_seq",
        "io": "col_io",
        "lane_pmc": "col_dept1",
        "lane_purchasing": "col_dept2",
        "lane_system": "col_dept3",
        "desc": "col_desc"
    }

def get_icon_cells(lib_root, icon_type):
    # Return ALL mxCells for a given type (handling groups)
    cells = []
    for add_node in lib_root.findall('add'):
        if add_node.get('as') == icon_type:
            for cell in add_node.findall('mxCell'):
                cells.append(copy.deepcopy(cell))
            return cells
    return []

def main():
    args = parse_arguments()
    
    base_dir = args.base_dir
    
    # Define paths based on base_dir
    template_2_lane_path = os.path.join(base_dir, "flowchart-architect/skills/generate-drawio/references/canvas_template_2_lanes.xml")
    template_3_lane_path = os.path.join(base_dir, "flowchart-architect/skills/generate-drawio/references/canvas_template_3_lanes.xml")
    icon_lib_path = os.path.join(base_dir, "flowchart-architect/skills/generate-drawio/references/icon_library.xml")
    
    # Logic and Output paths
    logic_path = args.logic_path
    output_path = args.output_path

    print(f"Loading logic from {logic_path}...")
    logic = load_json(logic_path)

    # Determine Template based on Swimlanes
    dept_lanes = [l for l in logic['swimlanes'] if l['type'] == 'department']
    num_depts = len(dept_lanes)
    
    if args.use_2_lane:
        print("Forcing 2-Lane Template.")
        template_path = template_2_lane_path
        total_width = 800
    elif args.use_3_lane:
        print("Forcing 3-Lane Template.")
        template_path = template_3_lane_path
        total_width = 800
    elif num_depts <= 2:
        print(f"Detected {num_depts} departments. Using 2-Lane Template (A4).")
        template_path = template_2_lane_path
        total_width = 800
    else:
        print(f"Detected {num_depts} departments. Using 3-Lane Template (A4).")
        template_path = template_3_lane_path
        total_width = 800

    print(f"Loading template from {template_path}...")
    template_tree, template_root = load_xml(template_path)
    lib_tree, lib_root = load_xml(icon_lib_path)

    root_model = template_root.find('.//root')
    
    # 1. Dynamic Swimlane Generation
    cells_map = {elem.get('id'): elem for elem in root_model.findall('.//mxCell')}
    if 'main_container' in cells_map:
        cells_map['main_container'].set('value', logic['meta']['process_name'])
    
    # Fixed Columns
    fixed_cols = {
        "col_seq": 40,
        "col_io": 120,
        "col_desc": 150
    }
    
    # Calculate Widths
    # total_width is set above based on template selection
    available_width = total_width - sum(fixed_cols.values())
    dept_width = available_width / num_depts if num_depts > 0 else 220
    
    # Remove existing department columns from template to avoid duplicates
    for cell in root_model.findall('.//mxCell'):
        if cell.get('id', '').startswith('col_dept'):
            root_model.remove(cell)
            
    # Create New Department Columns
    current_x = 40 + 120 # Start after Seq + IO
    lane_ids = {
        "seq": "col_seq",
        "io": "col_io",
        "desc": "col_desc"
    }
    
    # Re-insert Dept Columns
    for i, lane in enumerate(dept_lanes):
        lane_id = lane['id']
        xml_id = f"col_dept_{i}"
        lane_ids[lane_id] = xml_id # Map logic ID to XML ID
        
        new_col = ET.Element('mxCell')
        new_col.set('id', xml_id)
        new_col.set('value', lane['name'])
        new_col.set('style', "swimlane;html=1;startSize=30;fillColor=#ffffff;fontColor=#000000;strokeColor=#000000;strokeWidth=2;")
        new_col.set('parent', "main_container")
        new_col.set('vertex', "1")
        
        geo = ET.SubElement(new_col, 'mxGeometry')
        geo.set('x', str(current_x))
        geo.set('y', "30")
        geo.set('width', str(dept_width))
        geo.set('height', "570") # Initial height, will be resized later
        geo.set('as', "geometry")
        
        root_model.append(new_col)
        current_x += dept_width
        
    # Update Description Column Position
    if 'col_desc' in cells_map:
        desc_cell = cells_map['col_desc']
        # Move to end of list to ensure it renders on the right
        root_model.remove(desc_cell)
        root_model.append(desc_cell)
        
        geo = desc_cell.find('mxGeometry')
        if geo is not None:
            geo.set('x', str(current_x))
            
    # Update Helper for Lane Index (Dynamic)
    def get_lane_index(lane_id):
        for idx, l in enumerate(dept_lanes):
            if l['id'] == lane_id:
                return idx
        return 0

    # 2. Process Steps and Add Nodes
    y_cursor = 30 + 40 # Start below header (header=30) + padding
    y_step = 100 # Vertical spacing
    
    step_y_map = {} # Store Y for routing
    # lane_ids is already defined dynamically above
    
    for i, step in enumerate(logic['steps']):
        step_id = step['id']
        step_type = step['type']
        target_lane_logic_id = step.get('lane_id', 'lane_pmc')
        target_lane_xml_id = lane_ids.get(target_lane_logic_id, "col_dept1")
        
        # A. Sequence Number
        seq_cell = ET.Element('mxCell')
        seq_cell.set('id', f"seq_{i}")
        seq_cell.set('value', str((i+1)*10))
        seq_cell.set('style', "text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;")
        seq_cell.set('vertex', "1")
        seq_cell.set('parent', lane_ids['seq'])
        geo = ET.SubElement(seq_cell, 'mxGeometry')
        geo.set('x', "0")
        geo.set('y', str(y_cursor + 20))
        geo.set('width', "40")
        geo.set('height', "20")
        geo.set('as', "geometry")
        root_model.append(seq_cell)

        # B. Main Node
        icon_type_map = {
            "process": "process_step", 
            "decision": "decision_node", 
            "terminator": "terminator",
            "subprocess": "subprocess_step"
        }
        
        # Determine specific template based on tags
        template_key = icon_type_map.get(step_type, "process_step")
        if step.get('system_tag'):
            template_key = "system_step"
            
        cells = get_icon_cells(lib_root, template_key)
        
        if cells:
            # Check if it's a group (more than 1 cell)
            if len(cells) > 1:
                # Group Handling (System Step)
                group_parent = None
                children = []
                for cell in cells:
                    if cell.get('connectable') == "0": # Group container
                        group_parent = cell
                    else:
                        children.append(cell)
                
                if group_parent:
                    main_cell = group_parent # The group itself is the main object to position
                    main_cell.set('id', step_id)
                    main_cell.set('parent', target_lane_xml_id)
                    
                    # Center Group
                    lane_width = dept_width if "dept" in target_lane_xml_id else 150
                    node_width = int(main_cell.find('mxGeometry').get('width', 100))
                    center_x = (lane_width - node_width) / 2
                    
                    main_cell.find('mxGeometry').set('x', str(center_x))
                    main_cell.find('mxGeometry').set('y', str(y_cursor))
                    
                    root_model.append(main_cell)
                    
                    for child in children:
                        child.set('parent', step_id) # Parent to the group
                        # Update text if it's the main label
                        if "Process Name" in child.get('value', ''):
                            child.set('value', step['name'])
                        # Update System Tag
                        if "[SYS]" in child.get('value', ''):
                            child.set('value', step['system_tag'])
                        # Generate unique ID
                        child.set('id', f"{step_id}_{child.get('id')}")
                        root_model.append(child)
            else:
                # Single Cell Handling
                main_cell = cells[0]
                main_cell.set('id', step_id)
                main_cell.set('value', step['name'])
                main_cell.set('parent', target_lane_xml_id)
                
                # Center
                lane_width = dept_width if "dept" in target_lane_xml_id else 150
                node_width = int(main_cell.find('mxGeometry').get('width', 100))
                center_x = (lane_width - node_width) / 2
                
                # Apply X Offset
                center_x += step.get('x_offset', 0)
                
                main_cell.find('mxGeometry').set('x', str(center_x))
                main_cell.find('mxGeometry').set('y', str(y_cursor))
                
                if step.get('system_tag') and template_key != "system_step":
                     main_cell.set('value', f"{step['name']}\n[{step['system_tag']}]")
                
                root_model.append(main_cell)

        # C. Description
        if 'description' in step:
            desc_cell = ET.Element('mxCell')
            desc_cell.set('id', f"desc_{i}")
            desc_cell.set('value', step['description'])
            desc_cell.set('style', "text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;")
            desc_cell.set('vertex', "1")
            desc_cell.set('parent', lane_ids['desc'])
            geo = ET.SubElement(desc_cell, 'mxGeometry')
            geo.set('x', "5")
            geo.set('y', str(y_cursor))
            geo.set('width', "140")
            geo.set('height', "60")
            geo.set('as', "geometry")
            root_model.append(desc_cell)

        # D. I/O Document (Group Handling)
        if step.get('doc_ref') or step.get('doc_output'):
            doc_name = step.get('doc_ref') or step.get('doc_output')
            doc_cells = get_icon_cells(lib_root, "document_with_tag")
            
            if doc_cells:
                # 1. Identify Group Parent and Children
                # In library: Parent has connectable="0", Children have parent="doc_group_template"
                group_parent = None
                children = []
                
                # Find the group container first
                for cell in doc_cells:
                    if cell.get('connectable') == "0":
                        group_parent = cell
                    else:
                        children.append(cell)
                
                if group_parent:
                    new_group_id = f"doc_group_{i}"
                    group_parent.set('id', new_group_id)
                    group_parent.set('parent', lane_ids['io'])
                    # Center in 120px column: (120 - 100) / 2 = 10
                    group_parent.find('mxGeometry').set('x', "10") 
                    group_parent.find('mxGeometry').set('y', str(y_cursor))
                    root_model.append(group_parent)
                    
                    for child in children:
                        child.set('parent', new_group_id) # Re-parent to new group
                        # Update values
                        if "TAG" in child.get('value', ''):
                             child.set('value', "DOC") # Default tag
                        elif "Doc Name" in child.get('value', ''):
                             child.set('value', doc_name)
                        
                        # Generate unique ID
                        child.set('id', f"doc_child_{i}_{child.get('id')}")
                        root_model.append(child)

        # Store Y for routing
        step_y_map[step_id] = y_cursor

        y_cursor += y_step

    # 3. Resize Containers
    # Add some padding at the bottom
    total_height = y_cursor + 60
    
    # Resize Main Container
    if 'main_container' in cells_map:
        geo = cells_map['main_container'].find('mxGeometry')
        if geo is not None:
            geo.set('height', str(total_height))
            geo.set('width', str(total_width))
            
    # Resize All Columns
    # lane_ids is already defined
    for lane_key, lane_id in lane_ids.items():
        if lane_id in cells_map:
            geo = cells_map[lane_id].find('mxGeometry')
            if geo is not None:
                geo.set('height', str(total_height - 30))

    # 4. Insert Connectors
    connector_template = get_icon_cells(lib_root, "connector")[0]
    
    # Helper to get port config
    def get_port_config(step_id, logic_data):
        for s in logic_data['steps']:
            if s['id'] == step_id:
                return s.get('port_config', {})
        return {}
        
    # Helper to get lane index
    def get_lane_index(lane_id):
        if "pmc" in lane_id: return 0
        if "purchasing" in lane_id: return 1
        return 0

    for step in logic['steps']:
        source_id = step['id']
        next_steps = step.get('next')
        
        if not next_steps:
            continue
            
        targets = []
        if isinstance(next_steps, list):
            for t in next_steps:
                targets.append((t, None)) # (target_id, label)
        elif isinstance(next_steps, dict):
            for label, t in next_steps.items():
                targets.append((t, label))
        
        source_config = step.get('port_config', {})
        source_lane = step.get('lane_id', 'lane_pmc')
        source_y = step_y_map.get(source_id, 0)
        
        for target_id, label in targets:
            edge = copy.deepcopy(connector_template)
            edge.set('id', f"edge_{source_id}_{target_id}")
            edge.set('source', source_id)
            edge.set('target', target_id)
            edge.set('parent', '1') 
            
            # Find target details
            target_step = next((s for s in logic['steps'] if s['id'] == target_id), None)
            target_lane = target_step.get('lane_id', 'lane_pmc') if target_step else 'lane_pmc'
            target_y = step_y_map.get(target_id, 0)
            target_config = get_port_config(target_id, logic)
            
            # Default Style
            style = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
            
            # Determine Sides based on Logic
            exit_side = "bottom"
            entry_side = "top"
            jetty = "auto"
            
            src_lane_idx = get_lane_index(source_lane)
            tgt_lane_idx = get_lane_index(target_lane)
            
            if src_lane_idx == tgt_lane_idx:
                # Same Lane
                if label == "No":
                    # Bypass/Loop Logic: Exit Right, Entry Right
                    exit_side = "right"
                    entry_side = "right"
                    jetty = "25"
                elif label == "Yes":
                    # Standard Flow
                    exit_side = "bottom"
                    entry_side = "top"
                elif target_y < source_y:
                    # Loop Back Up
                    exit_side = "left"
                    entry_side = "left"
                else:
                    # Standard Downward
                    exit_side = "bottom"
                    entry_side = "top"
            elif src_lane_idx < tgt_lane_idx:
                # Left to Right (e.g. PMC -> Purchasing)
                exit_side = "right"
                entry_side = "left"
            else: # src_lane_idx > tgt_lane_idx
                # Right to Left (e.g. Purchasing -> PMC)
                exit_side = "left"
                entry_side = "right"

            # Manual Config Overrides
            if 'exit' in source_config: exit_side = source_config['exit']
            if 'entry' in target_config: entry_side = target_config['entry']
            if 'jetty' in source_config: jetty = str(source_config['jetty'])
            
            # Apply Jetty
            if jetty != "auto":
                style = style.replace("jettySize=auto", f"jettySize={jetty}")

            # Apply Exit Style
            if exit_side == "top":    style += "exitX=0.5;exitY=0;exitDx=0;exitDy=0;"
            elif exit_side == "bottom": style += "exitX=0.5;exitY=1;exitDx=0;exitDy=0;"
            elif exit_side == "left":   style += "exitX=0;exitY=0.5;exitDx=0;exitDy=0;"
            elif exit_side == "right":  style += "exitX=1;exitY=0.5;exitDx=0;exitDy=0;"
            
            # Apply Entry Style
            if entry_side == "top":    style += "entryX=0.5;entryY=0;entryDx=0;entryDy=0;"
            elif entry_side == "bottom": style += "entryX=0.5;entryY=1;entryDx=0;entryDy=0;"
            elif entry_side == "left":   style += "entryX=0;entryY=0.5;entryDx=0;entryDy=0;"
            elif entry_side == "right":  style += "entryX=1;entryY=0.5;entryDx=0;entryDy=0;"

            edge.set('style', style)
            
            if label:
                edge.set('value', label)
            
            root_model.append(edge)

    template_tree.write(output_path)
    print(f"Diagram saved to {output_path}")

if __name__ == "__main__":
    main()
