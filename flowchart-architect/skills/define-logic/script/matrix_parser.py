import re
import json
import sys
import argparse
from pathlib import Path

def parse_markdown_table(file_path):
    """Parses a strict markdown table into a list of dictionaries."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    table_data = []
    in_table = False
    headers = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Detect Header Row
        if line.startswith('|') and 'ID' in line and 'Role' in line:
            in_table = True
            # Extract headers, cleaning whitespace
            headers = [h.strip() for h in line.split('|') if h.strip()]
            continue
        
        if in_table and line.startswith('|'):
            # Skip separator line
            if '---' in line:
                continue
            
            # Parse row
            cells = [c.strip() for c in line.split('|')]
            
            # Handle leading/trailing pipes which create empty strings
            if len(cells) > 0 and cells[0] == '': cells.pop(0)
            if len(cells) > 0 and cells[-1] == '': cells.pop(-1)
            
            # Ensure row has same number of columns as headers
            if len(cells) != len(headers):
                # Handle cases where empty trailing columns might be dropped or added
                # This is a basic robustness check
                if len(cells) < len(headers):
                    cells.extend([''] * (len(headers) - len(cells)))
                else:
                    cells = cells[:len(headers)]

            row = dict(zip(headers, cells))
            table_data.append(row)

    return table_data

def convert_to_logic_structure(table_data, process_name="Generated Process"):
    """Converts parsed table data into the logic_structure.json format."""
    swimlanes = {}
    steps = []
    
    # First pass: Identify swimlanes and create steps
    for row in table_data:
        role = row.get('Role', 'Unknown')
        if role not in swimlanes:
            swimlanes[role] = {
                "id": f"lane_{role.lower().replace(' ', '_')}",
                "name": role,
                "type": "department"
            }
        
        step_id = f"step_{row.get('ID', '000')}"
        
        # Parse Next Logic
        next_val = row.get('Next', '')
        next_steps = []
        next_dict = {}
        
        # Decision Logic: "Yes: 050, No: 020"
        if ':' in next_val and ',' in next_val: 
            parts = [p.strip() for p in next_val.split(',')]
            for p in parts:
                if ':' in p:
                    cond, target = p.split(':', 1)
                    next_dict[cond.strip()] = f"step_{target.strip()}"
            next_steps = next_dict
        # Single Next Step: "020"
        elif next_val:
            next_steps = [f"step_{next_val}"]
        
        step = {
            "id": step_id,
            "type": row.get('Type', 'process').lower(),
            "name": row.get('Description', ''),
            "lane_id": swimlanes[role]['id'],
            "next": next_steps,
            "system_tag": row.get('System', '') if row.get('System', '') else None,
            "doc_ref": row.get('Documents', '') if row.get('Documents', '') else None,
            "description": row.get('Detailed Description', '')
        }
        steps.append(step)

    logic_structure = {
        "meta": {
            "process_name": process_name,
            "version": "1.0",
            "generator": "matrix_parser.py"
        },
        "swimlanes": list(swimlanes.values()),
        "steps": steps
    }
    
    return logic_structure

def main():
    parser = argparse.ArgumentParser(description="Convert Strict Process Matrix Markdown to Logic Structure JSON.")
    parser.add_argument("input_file", help="Path to the input markdown file containing the matrix.")
    parser.add_argument("--output", help="Path to the output JSON file. Defaults to stdout.", default=None)
    
    args = parser.parse_args()
    
    data = parse_markdown_table(args.input_file)
    if not data:
        print("Error: No valid table data found in input file.", file=sys.stderr)
        sys.exit(1)
        
    logic = convert_to_logic_structure(data)
    
    json_output = json.dumps(logic, indent=2)
    
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(json_output)
            print(f"Successfully wrote logic structure to {args.output}")
        except Exception as e:
            print(f"Error writing output file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(json_output)

if __name__ == "__main__":
    main()
