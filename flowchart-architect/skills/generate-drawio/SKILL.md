---
name: generate-drawio
description: Generates a Draw.io XML file from the logic structure, applying strict brand and visualization standards.
---

# Generate DrawIO Skill
## Overview

This skill is the "generate-drawio". It takes the abstract logic structure defined by the Process Analyst and converts it into a concrete, visual Draw.io XML file. It MUST strictly adhere to the project's brand guidelines and visualization standards to ensure a consistent, professional look.

## Inputs

- `1-输入/[P-project_name]/[process_name]/logic_structure.json` (MANDATORY): The source logic to visualize.
- `skills/generate-drawio/references/brand-guidelines.md` (MANDATORY): Defines colors, fonts, and logo usage.
- `skills/generate-drawio/references/visualization-standards.md` (MANDATORY):2.  **Generate Diagram**:
    - Run the assembler script: `uv run flowchart-architect/skills/generate-drawio/script/assembler.py`
    - The script will load `standard_template_v1.xml` and `logic_structure.json` to generate `diagram.drawio`.
- `skills/generate-drawio/references/icon_library.xml` (MANDATORY): The "Golden Snippets" for all components. **MUST** copy XML from here.

## Workflow

**Objective**: Construct the Draw.io XML string.

1. **Apply Styles**:
   - Use the **Primary Color** from `brand-guidelines.md` for main process steps.
   - Use the **Secondary Color** for decision diamonds.
   - Apply the correct **Font Family** to all labels.
    - **Layout Hints**: You MUST infer layout requirements from the image and populate `x_offset` and `port_config` accordingly:
        - **Parallel Splits**: Use `x_offset: -90` for the start node and `entry: left` for branches.
        - **Parallel Merges**: Use `exit: right` and `jetty: 60` to force wide overlaps.
        - **Loops**: Use `exit: right` and `entry: top` for upward loops.
    - **Swimlanes**: The script automatically adjusts to the number of swimlanes defined in your JSON (e.g., 2, 3, or more). No manual template selection is needed.
2. **Construct Elements**:
   - Create `<mxCell>` tags for each node and connection.
   - Ensure all IDs match the `logic_structure.json`.
   - Add metadata (Project Name, Date) to the diagram header/footer if required.

### Step 4: Write Output

1. **Create** `1-输入/[P-project_name]/[process_name]/diagram.drawio`.
2. **Verify**: Ensure the file is valid XML and can be opened in Draw.io.

## Output

- `1-输入/[P-project_name]/[process_name]/diagram.drawio`: The final, editable flowchart file.
