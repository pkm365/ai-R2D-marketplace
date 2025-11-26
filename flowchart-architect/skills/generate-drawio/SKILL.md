---
name: generate-drawio
description: Generates a Draw.io XML file from the logic structure, applying strict brand and visualization standards.
---

# Generate DrawIO Skill

## Overview

This skill is the "Builder". It takes the abstract logic structure defined by the Process Analyst and converts it into a concrete, visual Draw.io XML file. It MUST strictly adhere to the project's brand guidelines and visualization standards to ensure a consistent, professional look.

## Inputs

- `1-输入/[P-project_name]/[process_name]/logic_structure.json` (MANDATORY): The source logic to visualize.
- `skills/generate-drawio/references/brand-guidelines.md` (MANDATORY): Defines colors, fonts, and logo usage.
- `skills/generate-drawio/references/visualization-standards.md` (MANDATORY): Defines swimlane layout, spacing, and shape styles.
- `skills/generate-drawio/references/drawio-template.xml` (OPTIONAL): A base XML template to start from.

## Workflow

### Step 1: Load Resources

1. **Read** the Logic Structure: `1-输入/[P-project_name]/[process_name]/logic_structure.json`.
2. **Read** the Standards:
   - `skills/generate-drawio/references/brand-guidelines.md`
   - `skills/generate-drawio/references/visualization-standards.md`

### Step 2: Calculate Layout

**Objective**: Determine the X,Y coordinates for every element (Swimlanes, Steps, Decisions).

1. **Parse Swimlanes**: Calculate the total width and individual swimlane positions based on `visualization-standards.md`.
2. **Position Nodes**:
   - Place the "Start" node in the first active swimlane.
   - Arrange subsequent steps vertically or horizontally based on the flow.
   - Ensure adequate spacing between nodes as defined in the standards.
   - Align nodes to the center of their respective swimlanes.

### Step 3: Generate XML

**Objective**: Construct the Draw.io XML string.

1. **Apply Styles**:
   - Use the **Primary Color** from `brand-guidelines.md` for main process steps.
   - Use the **Secondary Color** for decision diamonds.
   - Apply the correct **Font Family** to all labels.
2. **Construct Elements**:
   - Create `<mxCell>` tags for each node and connection.
   - Ensure all IDs match the `logic_structure.json`.
   - Add metadata (Project Name, Date) to the diagram header/footer if required.

### Step 4: Write Output

1. **Create** `1-输入/[P-project_name]/[process_name]/diagram.drawio`.
2. **Verify**: Ensure the file is valid XML and can be opened in Draw.io.

## Output

- `1-输入/[P-project_name]/[process_name]/diagram.drawio`: The final, editable flowchart file.
