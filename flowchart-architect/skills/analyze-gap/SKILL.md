---
name: analyze-gap
description: Analyzes gaps between requirements and standard assets, and extracts the final logic structure for diagram generation. Supports distinct modes for Gap Analysis, Logic Synthesis, and Logic Update.
---

# Analyze Gap Skill

## Overview

This skill acts as the "Logic Architect". It bridges the gap between process requirements and standard process assets. Its goal is to produce a definitive, structured logic definition that can be directly converted into a diagram.

## Inputs

- `1-输入/[P-project_name]/[process_name]/requirements.md` (MANDATORY)
- `1-输入/[P-project_name]/[process_name]/asset_search_report.md` (MANDATORY)
- `mode` (MANDATORY): One of `GAP_ANALYSIS`, `LOGIC_SYNTHESIS`, or `LOGIC_UPDATE`.
- `0-辅助/Assets/[selected_asset]` (OPTIONAL - if asset selected)

## Workflow

### Mode 1: GAP_ANALYSIS

**Trigger**: Step 4A of Orchestration.

1. **MANDATORY**: Invoke the `process-analyst` agent (Scenario 1).
2. **Instruction**: "Perform **Gap Analysis** only. Compare `1-输入/[P-project_name]/[process_name]/requirements.md` with the asset in `1-输入/[P-project_name]/[process_name]/asset_search_report.md`. Generate `1-输入/[P-project_name]/[process_name]/gap_analysis.md`."

### Mode 2: LOGIC_SYNTHESIS

**Trigger**: Step 4B of Orchestration.

1. **MANDATORY**: Invoke the `process-analyst` agent (Scenario 2).
2. **Instruction**: "Perform **Logic Synthesis**. Using the requirements and the gap analysis (if any), synthesize the complete process logic. Use `SequentialThinking` to plan first, then generate `1-输入/[P-project_name]/[process_name]/logic_structure.json`."

### Mode 3: LOGIC_UPDATE

**Trigger**: Step 4.5 of Orchestration (if user requests changes).

1. **MANDATORY**: Invoke the `process-analyst` agent (Scenario 3).
2. **Instruction**: "Perform **Logic Update**. The user has requested changes to the logic. Read the current `logic_structure.json` and apply the requested modifications using `Edit` or `MultiEdit`."

## Validation

- **Logic Check**: Ensure every row in the `requirements.md` Process Flow Matrix is represented in `logic_structure.json`.
- **Connectivity**: Ensure all steps have at least one input and one output (except Start/End).
