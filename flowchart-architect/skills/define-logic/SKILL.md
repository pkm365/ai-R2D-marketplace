---
name: define-logic
description: Analyzes gaps between requirements and standard assets, and extracts the final logic structure for diagram generation. Supports distinct modes for Gap Analysis, Logic Synthesis, and Logic Update.
---

# Define Logic Skill

## Overview

This skill acts as the "Logic Architect". It bridges the gap between process requirements and standard process assets. Its goal is to produce a definitive, structured logic definition that can be directly converted into a diagram.

## Inputs

- `1-输入/[P-project_name]/[process_name]/requirements.md` (MANDATORY)
- `1-输入/[P-project_name]/[process_name]/asset_search_report.md` (MANDATORY)
- `mode` (MANDATORY): One of `GAP_ANALYSIS`, `LOGIC_SYNTHESIS`, `LOGIC_UPDATE`, or `LOGIC_FROM_STANDARD_MATRIX`.
- `0-辅助/Assets/[selected_asset]` (OPTIONAL - if asset selected)

## Workflow

### Path A: AI-Assisted Workflow (Modes 1-3)
Use this path when requirements are vague or when adapting standard assets.

#### Mode 1: GAP_ANALYSIS

**Trigger**: Step 4A of Orchestration.

1. **MANDATORY**: Invoke the `process-analyst` agent (Scenario 1).
2. **Instruction**: "Perform **Gap Analysis** only. Compare `1-输入/[P-project_name]/[process_name]/requirements.md` with the asset in `1-输入/[P-project_name]/[process_name]/asset_search_report.md`. Generate `1-输入/[P-project_name]/[process_name]/gap_analysis.md`."

### Mode 2: LOGIC_SYNTHESIS

**Trigger**: Step 4B of Orchestration.

1. **MANDATORY**: Invoke the `process-analyst` agent (Scenario 2).
2. **Instruction**: "Perform **Logic Synthesis**. Read the fuzzy `requirements.md`. Transform it into the **Standard Process Flow Matrix** format. Save this as `process_flow_matrix.md`."
3. **MANDATORY**: Once the matrix is created, **Execute Mode 4** to generate the JSON.

### Mode 3: LOGIC_UPDATE

**Trigger**: Step 4.5 of Orchestration (if user requests changes).

**CRITICAL**: You MUST update the `requirements.md` (Process Flow Matrix) FIRST to reflect the changes. The Matrix and Logic Structure must always be in sync.

1. **MANDATORY**: Invoke the `process-analyst` agent (Scenario 3).
2. **Instruction**: "Perform **Logic Update**. The user has requested changes. First, update `requirements.md` to reflect these changes. Then, update `logic_structure.json` to match the new requirements."

**Note**: This mode is for the AI path. If using the **Script Workflow**, do not use Mode 3. Instead, update the matrix and re-run **Mode 4**.

### Path B: Deterministic Script Workflow (Mode 4)
Use this path when you have a precise "Process Flow Matrix" and want 100% predictable output.

#### Mode 4: LOGIC_FROM_STANDARD_MATRIX

**Trigger**: User provides the standard "Process Flow Matrix" (Markdown Table) in `process_flow_matrix.md`.

1. **MANDATORY**: Execute the `matrix_parser.py` script.
2. **Command**:
   ```bash
   uv run flowchart-architect/skills/define-logic/script/matrix_parser.py \
     "[ABSOLUTE_PATH_TO_PROCESS_FLOW_MATRIX_MD]" \
     --output "[ABSOLUTE_PATH_TO_LOGIC_JSON]"
   ```

## Validation

- **Logic Check**: Ensure every row in the `requirements.md` Process Flow Matrix is represented in `logic_structure.json`.
- **Connectivity**: Ensure all steps have at least one input and one output (except Start/End).
