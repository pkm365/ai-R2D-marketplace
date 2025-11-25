---
name: analyze-gap
description: Analyzes gaps between requirements and standard assets, and extracts the final logic structure for diagram generation.
---

# Analyze Gap Skill

## Overview

This skill acts as the "Logic Architect". It bridges the gap between business requirements and standard process assets. Its goal is to produce a definitive, structured logic definition that can be directly converted into a diagram.

## Inputs

- `output/[project_name]/requirements.md` (MANDATORY)
- `output/[project_name]/asset_search_report.md` (MANDATORY)
- `standard_process_templates/[selected_asset]` (OPTIONAL - if asset selected)

## Workflow

### Step 1: Invoke Process Analyst

1. **MANDATORY**: Invoke the `process-analyst` agent.
2. **Instruction**: "Analyze the requirements in `output/[project_name]/requirements.md` and the asset report in `output/[project_name]/asset_search_report.md`. Perform gap analysis and synthesize the final logic structure."

### Step 2: Verify Outputs

1. **Check** that `output/[project_name]/gap_analysis.md` exists and follows the Gap Matrix format.
2. **Check** that `output/[project_name]/logic_structure.json` exists and contains valid JSON logic.

## Validation

- **Logic Check**: Ensure every row in the `requirements.md` Process Flow Matrix is represented in `logic_structure.json`.
- **Connectivity**: Ensure all steps have at least one input and one output (except Start/End).
