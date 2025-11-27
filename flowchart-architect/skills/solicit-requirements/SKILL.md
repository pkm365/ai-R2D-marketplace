---
name: solicit-requirements
description: Guides the user through a structured requirement gathering process to populate the Process Flow Matrix.
---

# Solicit Requirements Skill

## Overview

This skill is responsible for the "Inception" step. It transforms vague user requests into structured, actionable business requirements. It uses a professional checklist to ensure all necessary details (stakeholders, systems, data flows) are captured.

## Inputs

- `1-输入/[P-project_name]/[process_name]/Plan.md` (MANDATORY): To understand the current context.
- `flowchart-architect/skills/solicit-requirements/references/requirements-checklist.md` (OPTIONAL): A checklist of questions to ask.
- `flowchart-architect/skills/solicit-requirements/references/process_flow_matrix_template.md` (OPTIONAL): The standard template for process definition.

## Workflow

### Step 1: Context Gathering

1. **Read** the Plan file to see what is already known.
2. **Ask** clarifying questions if the initial request is vague. Focus on:
   - Who are the actors (Departments/Roles)?
   - What triggers the process?
   - What are the key steps?
   - What systems are involved (ERP, MES, WMS)?
   - What documents are exchanged?

### Step 2: Structured Documentation

1. **Synthesize** the user's responses into a structured narrative.
2. **Create** `1-输入/[P-project_name]/[process_name]/requirements.md`.

   **Standard Requirements Format**:
   ```markdown
   # [Project Name] - Process Requirements

   ## 1. Process Overview
   **Process Name**: [Name]
   **Process Owner**: [Name/Role]

   ## 2. Narrative Description
   [Describe the process in natural language. E.g., "First, the PMC prints the notice. Then, Production generates the slip..."]

   ## 3. Key Rules & Constraints
   - [Rule 1]
   - [Rule 2]
   ```

### Step 3: Confirmation
   
1. **Present** the summary to the user.
2. **STOP HERE**: Ask: "Does this accurately reflect your process? Are there any missing steps or actors?"
3. **Wait for user response**.
