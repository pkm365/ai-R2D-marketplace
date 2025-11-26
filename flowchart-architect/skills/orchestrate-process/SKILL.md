---
name: orchestrate-process
description: Orchestrates the complete Requirement-to-Diagram (R2D) workflow by coordinating specialized skills and agents to transform business requirements into professional draw.io flowcharts. Manages the end-to-end process from requirement solicitation through diagram generation and quality assurance.
---

# Process Orchestration

## Overview

This skill orchestrates the complete Requirement-to-Diagram (R2D) workflow by coordinating specialized agents and skills to transform business requirements into professional draw.io flowcharts. It manages the entire process from initial requirement gathering through asset retrieval, logic definition, diagram generation, and quality assurance.

**Core Principle**: Each step is handled by specialized skills with clear responsibilities, ensuring professional-quality outputs through systematic coordination and validation.Never generate these elements manually.

## When to Use

Use this skill when:
- The user needs a complete flowchart generated from business requirements
- Multiple stakeholders or systems need to be represented in the diagram
- Complex business logic requires professional visualization
- Quality assurance and brand compliance are critical
- Iterative refinement based on user feedback is expected

## Process Workflow

Execute all steps below systematically. Use these as ToDos to track your progress through the R2D workflow.

### Step 1: Create Plan

1. **MANDATORY**: Create a new plan file at: `1-输入/[P-project_name]/[process_name]/Plan.md`
   - If a plan file already exists, read it to understand what has been done so far and continue from there.
   - You will update this document as you progress through the planning steps.

2. The plan file **MUST** use the following template structure:

   ```markdown
   # [Project Name] - R2D Process Plan

   ## Workflow Status
   - [ ] Step 1: Create Plan
   - [ ] Step 2: Inception (Requirements)
   - [ ] Step 3: Retrieval (Asset Search)
   - [ ] Step 4A: Gap Analysis
   - [ ] Step 4B: Logic Definition
   - [ ] Step 4.5: Logic Checkpoint (User Confirmation)
   - [ ] Step 5: Generation
   - [ ] Step 6: QA (Audit)
   - [ ] Step 7: Delivery

   ## Requirements Summary
   [Brief summary of the core business requirements]

   ## Asset Selection
   [Template 1 Name]
   [Template 2 Name]

   Each template option should include:
   1. Template name and source
   2. Rationale for why it fits the requirements
   3. Star rating (1-3 ⭐) based on fit

   Once selected: Update with (✅ User Selection) next to the chosen template.

   ## Gap Analysis & Logic Strategy
   [Strategy for bridging gaps between requirements and selected asset]

   ## Logic Structure Preview
   [High-level summary of swimlanes and key steps]

   ## Final Diagram
   - **File**: [Link to diagram.drawio]
   - **Audit Status**: [PASS/FAIL]
   ```

### Step 2: Inception

**Objective**: Transform vague requirements into structured business specifications.

1. **MANDATORY**: Invoke `solicit-requirements` skill to guide requirement clarification:
   - Use professional checklist `flowchart-architect/skills/solicit-requirements/references/requirements-checklist.md` to prompt for missing details
   - Ask clarifying questions about stakeholders, data flows, and business rules
   - Document all requirements systematically

2. Create requirements file at: `1-输入/[P-project_name]/[process_name]/requirements.md` using the following template:

   ```markdown
   # [Project Name] - Process Requirements

   ## 1. Process Overview
   **Process Name**: [Name]
   **Process Owner**: [Name/Role]
   **Document Owner**: [Name/Role]

   ## 2. Swimlane Definition (Departments/Roles)
   List the departments or roles that will have their own swimlane:
   1. [Dept 1, e.g., Production]
   2. [Dept 2, e.g., Quality]
   3. [Dept 3, e.g., Warehouse]

   ## 3. Process Flow Matrix
   | Seq | I/O Document | System/Manual | Responsible Dept | Step Description | Next Step / Condition |
   |-----|--------------|---------------|------------------|------------------|-----------------------|
   | 10  | [Doc Name]   | [Manual/ERP]  | [Dept Name]      | [Action]         | [Go to Step 20]       |
   | 20  | [Doc Name]   | [MES/WMS]     | [Dept Name]      | [Action]         | [If OK -> 30, else -> 10]|
   ```

3. **MANDATORY** Present requirements summary to user for confirmation before proceeding.
   - **STOP HERE**: Ask "Is this requirements summary accurate? Shall we proceed?"
   - **Wait for user response**.

4. **Update Plan**:
   - Update `1-输入/[P-project_name]/[process_name]/Plan.md`
   - Mark **Step 2: Inception** as [x]
   - Fill in the **Requirements Summary** section.

### Step 3: Retrieval

**Objective**: Search for existing standard process templates that match requirements.

1. **MANDATORY**: Invoke `search-standard-assets` skill to:
   - Analyze requirements against standard asset library
   - Search for matching pre-made process templates
   - Retrieve applicable standard processes if found

2. **Outcomes**:
   - **Match Found**: Retrieve standard process template  ->  Proceed to Gap Analysis
   - **No Match**: Continue to Logic Definition with fresh extraction

3. Document retrieval results in: `1-输入/[P-project_name]/[process_name]/asset_search_report.md` using the following template:

   ```markdown
   # Asset Search Report - [Project Name]

   ## 1. Search Criteria
   - **Keywords**: [List keywords used]
   - **Filters**: [Any filters applied]

   ## 2. Search Results
   | Template Name | Source | Relevance Score (1-10) | Notes |
   |---------------|--------|------------------------|-------|
   | [Name]        | [Path] | [Score]                | [Why] |

   ## 3. Selected Asset
   **Selected**: [Template Name OR "None"]
   **Rationale**: [Why this was chosen or why no match was found]

   ## 4. Gap Assessment (Initial)
   - **Fit**: [High/Medium/Low]
   - **Major Gaps**: [Brief list of obvious missing features]
   ```

4. **User Selection Checkpoint (STOP HERE)**:
   - Present the search results to the user.
   - Ask: "I found these templates. Which one would you like to use? Or should we start from scratch?"
   - **Wait for user response**.
   - Update `asset_search_report.md` with the selected asset (or "None").

5. **Update Plan**:
   - Update `1-输入/[P-project_name]/[process_name]/Plan.md`
   - Mark **Step 3: Retrieval** as [x]
   - Fill in the **Asset Selection** section with the chosen template and rationale.

### Step 4A: Gap Analysis - Only if assets found

**Objective**: Compare requirements against standard templates and identify deviations.

1. **MANDATORY**: Invoke `analyze-gap` skill with `mode=GAP_ANALYSIS` to:
   - Compare business requirements with standard template
   - Identify logical deviations and custom requirements
   - Document gap analysis findings
   - Determine if deviations are justified

2. Create gap analysis file at: `1-输入/[P-project_name]/[process_name]/gap_analysis.md` using the following template:

   ```markdown
   # Gap Analysis - [Project Name]

   ## Process Flow Gap Matrix
   | Seq | I/O Document | System/Manual | Responsible Dept | Step Description | Gap Type | Action Taken |
   |-----|--------------|---------------|------------------|------------------|----------|--------------|
   | 10  | [Doc]        | [Sys/Man]     | [Dept]           | [Action]         | [Missing/Modified/New] | [Added/Updated/Ignored] |
   ```

3. **Validation**: Present gap analysis to user for confirmation before logic extraction.

4. **Update Plan**:
   - Update `1-输入/[P-project_name]/[process_name]/Plan.md`
   - Mark **Step 4A: Gap Analysis** as [x]
   - Fill in the **Gap Analysis & Logic Strategy** section.

### Step 4B: Logic Definition

**Objective**: Extract and structure the complete business logic for the diagram.

1. **MANDATORY**: Invoke `analyze-gap` skill with `mode=LOGIC_SYNTHESIS` to extract logic:
   - **If assets found**: Merge standard template with gap analysis
   - **If no assets**: Perform fresh logic extraction from requirements

2. Create logic structure file at: `1-输入/[P-project_name]/[process_name]/logic_structure.json`

3. **Logic Structure Format**:
   ```json
   {
     "swimlanes": [
       {
         "name": "Input Lane",
         "width": 150,
         "elements": [...]
       },
       {
         "name": "Process Lane",
         "width": 200,
         "elements": [...]
       }
     ],
     "connections": [...],
     "metadata": {
       "total_height": 1610,
       "diagram_title": "Process Name"
     }
   }
   ```

### Step 4.5: Logic Checkpoint

**Objective**: Present extracted logic to user for validation before generation.

1. Read `1-输入/[P-project_name]/[process_name]/logic_structure.json`
2. Present logic summary to user using the **Process Flow Matrix** format (same as Step 2):
   - **CRITICAL**: You MUST use the table format with columns: Seq, I/O Document, System/Manual, Responsible Dept, Step Description, Next Step/Condition.
   - This ensures the user verifies the *exact* sequence and logic that will be generated.

3. **User Confirmation Required (STOP HERE)**:
   - "I will draw the following steps: [summary]..."
   - "Is this logic correct? Any modifications needed?"
   - **CRITICAL**: Do NOT proceed to Step 5 until the user explicitly replies "Yes" or "Confirmed".

4. **If modifications requested**:
   - Invoke `analyze-gap` skill with `mode=LOGIC_UPDATE` to apply changes.
   - Repeat Step 4.5 until confirmed.

5. **Update Plan**:
   - Update `1-输入/[P-project_name]/[process_name]/Plan.md`
   - Mark **Step 4B: Logic Definition** and **Step 4.5: Logic Checkpoint** as [x]
   - Fill in the **Logic Structure Preview** section.

### Step 5: Generation

**Objective**: Generate professional draw.io XML from validated logic structure.

1. **MANDATORY**: Invoke `generate-drawio` skill:
   - Read `1-输入/[P-project_name]/[process_name]/logic_structure.json`
   - Read references/components.md for component templates
   - Read references/visualization-standards.md for styling rules
   - Calculate coordinates and positioning
   - Generate complete mxGraphModel XML

2. Create diagram file at: `1-输入/[P-project_name]/[process_name]/diagram.drawio`

3. **Generation Standards**:
   - All components follow brand guidelines
   - Proper spacing and alignment
   - Consistent color scheme
   - Valid XML structure
   - All connections properly routed

4. **Update Plan**:
   - Update `1-输入/[P-project_name]/[process_name]/Plan.md`
   - Mark **Step 5: Generation** as [x]
   - Fill in the **Final Diagram** section with the file link.

### Step 6: QA

**Objective**: Verify generated diagram meets quality and compliance standards.

1. **MANDATORY**: Invoke `xml-auditor` agent to audit `1-输入/[P-project_name]/[process_name]/diagram.drawio`:
   - **XML Syntax Check**: Valid structure, proper IDs, parent references
   - **Brand Compliance**: Colors, fonts, layout follow standards
   - **Logic Validation**: All steps from logic_structure.json are represented
   - **Visual Quality**: No overlapping elements, proper spacing

2. Create audit report at: `1-输入/[P-project_name]/[process_name]/audit_report.md`

3. **Audit Results**:
   - **PASS**: Proceed to delivery
   - **FAIL**: Self-correct and regenerate diagram

4. **If audit fails**:
   - Read audit findings
   - Correct identified issues
   - Regenerate `1-输入/[P-project_name]/[process_name]/diagram.drawio`
   - Re-run audit until PASS

5. **Update Plan**:
   - Update `1-输入/[P-project_name]/[process_name]/Plan.md`
   - Mark **Step 6: QA** as [x]
   - Fill in the **Audit Status** (PASS/FAIL).

### Step 7: Delivery

**Objective**: Present final professional diagram to user.

1. Present `1-输入/[P-project_name]/[process_name]/diagram.drawio` for user review
2. Provide summary of the workflow executed
3. Explain process requirements were addressed
4. Document all generated artifacts

## Iteration Cycle

**Objective**: Handle user feedback and refinement requests.

### Logic Changes

1. User requests changes to process steps, decision points, or data flow
2. Update `1-输入/[P-project_name]/[process_name]/logic_structure.json`
3. Regenerate `1-输入/[P-project_name]/[process_name]/diagram.drawio` from Step 5
4. Re-run QA audit
5. Deliver updated diagram (v2, v3, etc.)

### Style/Visual Changes

1. User requests changes to colors, layout, or visual presentation
2. Modify generation parameters in Step 5
3. Update `1-输入/[P-project_name]/[process_name]/diagram.drawio`
4. Re-run QA audit for syntax validation
5. Deliver updated diagram

**Iteration Tracking**: Maintain version history in file names or documentation.

## Skill Coordination

### solicit-requirements
- **Responsibility**: Requirement gathering
- **Outputs**: requirements.md

### analyze-gap
- **Responsibility**: Logic extraction, gap analysis
- **Outputs**: logic_structure.json, gap_analysis.json

### search-standard-assets
- **Responsibility**: Template retrieval, asset management
- **Outputs**: asset_search_report.md, 0-辅助/Assets/

### xml-auditor (Agent)
- **Responsibility**: Quality assurance, compliance checking
- **Outputs**: audit_report.md

### generate-drawio
- **Responsibility**: Diagram generation
- **Outputs**: diagram.drawio

## File Structure

```
output/
`-- [project_name]/
    |-- Plan.md                      # Step 1: Process tracking plan
    |-- requirements.md              # Step 2: Structured requirements
    |-- asset_search_report.md       # Step 3: Asset retrieval results
    |-- gap_analysis.json           # Step 4A: Gap analysis (if applicable)
    |-- logic_structure.json        # Step 4B: Extracted business logic
    |-- diagram.drawio             # Step 5: Generated diagram
    `-- audit_report.md            # Step 6: Quality assurance report
```

## Quality Checklist

Verify completion before delivery:
- [ ] **requirements.md**: Complete structured requirements documented
- [ ] **asset_search_report.md**: Standard asset search completed
- [ ] **logic_structure.json**: Business logic extracted and user-confirmed
- [ ] **generate-drawio skill invoked**: Professional diagram generated
- [ ] **audit_report.md**: Quality audit completed and passed
- [ ] User confirmation obtained at logic checkpoint
- [ ] All artifacts properly documented and delivered

## Tools to Use

**Skill Invocations** (MANDATORY):
- `solicit-requirements` - For requirement gathering and clarification
- `search-standard-assets` - For standard template retrieval
- `analyze-gap` - For gap analysis and logic extraction
- `generate-drawio` - For diagram generation from logic structure

**File Operations**:
- Read/write requirements, logic, and diagram files
- Create and manage output artifacts
- Track iterations and version history

## Common Pitfalls to Avoid

1. **Skipping Logic Confirmation**: Generating diagram without user logic validation  ->  Always get confirmation at Step 4.5
2. **Bypassing Asset Search**: Creating from scratch when templates exist  ->  Always search standard assets first
3. **Ignoring Audit Results**: Delivering failed diagrams  ->  Fix all audit issues before delivery
4. **Missing Requirements**: Incomplete business specifications  ->  Use systematic checklist in Step 2
5. **No Iteration Support**: Refusing user modifications  ->  Support full rework cycle with logic updates

## Example Execution

**Scenario**: User requests flowchart for "Customer Order Processing System"

Execute workflow:
1. **Step 1**: Create Plan.md  ->  Initialize process tracking
2. **Step 2**: solicit-requirements  ->  Document order validation, payment processing, inventory checks, shipping
3. **Step 3**: search-standard-assets  ->  Find existing "Order Processing Template"
4. **Step 4A**: analyze-gap (GAP_ANALYSIS)  ->  Identify custom return policy logic
5. **Step 4B**: analyze-gap (LOGIC_SYNTHESIS)  ->  Merge template with custom logic in logic_structure.json
6. **Step 4.5**: Present "I will draw: Order Input  ->  Validation  ->  Payment  ->  Inventory  ->  Shipping  ->  Output"
7. **Step 5**: generate-drawio  ->  Create professional swimlane diagram
8. **Step 6**: xml-auditor agent  ->  Validate syntax and brand compliance
9. **Step 7**: Deliver diagram.drawio with complete artifact package

**Result**: Professional, brand-compliant flowchart that accurately represents business requirements with rework capability for user feedback.

**CRITICAL**: Always execute steps sequentially and obtain user confirmation at the logic checkpoint before generation.
