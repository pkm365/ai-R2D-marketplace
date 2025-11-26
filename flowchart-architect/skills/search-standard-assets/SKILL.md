---
name: search-standard-assets
description: Orchestrates the search for standard process templates using the Asset Librarian agent.
---

# Search Standard Assets Skill

## Overview

This skill handles the "Retrieval" step. It analyzes the structured requirements and delegates the actual search task to the `asset-librarian` agent. Its goal is to find existing templates that can accelerate the flowchart creation process.

## Inputs

- `1-输入/[P-project_name]/[process_name]/requirements.md` (MANDATORY): The source of search keywords.

## Workflow

### Step 1: Keyword Extraction

1. **Read** `1-输入/[P-project_name]/[process_name]/requirements.md`.
2. **Extract** key terms from:
   - Process Name
   - Swimlane names (Departments)
   - System names (e.g., SAP, MES)
   - Key actions in the Process Flow Matrix

### Step 2: Invoke Asset Librarian

1. **MANDATORY**: Invoke the `asset-librarian` agent.
2. **Instruction**: "Search for standard process templates related to: [List of Keywords]. Focus on finding matches for [Specific Process Goal]."

### Step 3: Report Generation

1. **Receive** the report from the `asset-librarian`.
2. **Create** `1-输入/[P-project_name]/[process_name]/asset_search_report.md` using the standard template:

   ```markdown
   # Asset Search Report - [Project Name]

   ## 1. Search Criteria
   - **Keywords**: [List keywords used]

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
