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

1. **Synthesize** the user's responses into the **Process Flow Matrix** format.
2. **Create** `1-输入/[P-project_name]/[process_name]/requirements.md` using the standard template:

   ```markdown
   # [Project Name] - Process Requirements

   ## 1. Process Overview
   **Process Name**: [Name]
   **Process Owner**: [Name/Role]
   **Document Owner**: [Name/Role]

   ## 2. Swimlane Definition (Departments/Roles)
   List the departments or roles that will have their own swimlane:
   1. [Dept 1]
   2. [Dept 2]

   ## 3. Process Flow Matrix
   | Seq | I/O Document | System/Manual | Responsible Dept | Step Description | Next Step / Condition |
   |-----|--------------|---------------|------------------|------------------|-----------------------|
   | 10  | [Doc Name]   | [Manual/ERP]  | [Dept Name]      | [Action]         | [Go to Step 20]       |
   ```

### Step 3: Confirmation

1. **Present** the summary to the user.
2. **Ask**: "Does this accurately reflect your process? Are there any missing steps or actors?"
