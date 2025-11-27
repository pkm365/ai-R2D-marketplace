---
name: generate-drawio
description: Generates a Draw.io XML file from the logic structure using the assembler script.
---

# Generate DrawIO Skill

## Overview

This skill automates the generation of a Draw.io flowchart by executing the `assembler.py` script. It takes a `logic_structure.json` file as input and produces a `diagram.drawio` file, applying all visualization standards and template selections automatically.

## Inputs

-   `logic_path` (MANDATORY): The absolute path to the `logic_structure.json` file.
-   `output_path` (MANDATORY): The absolute path where the `diagram.drawio` file should be saved.
-   `flags` (OPTIONAL):
    -   `--2l`: Force use of the 2-lane (A4) template.
    -   `--3l`: Force use of the 3-lane (Wide) template.

## Workflow

**Objective**: Execute the assembler script to generate the flowchart.

1.  **Identify Paths**: Determine the absolute paths for the input logic file and the desired output file.
2.  **Execute Assembler**: Run the python script using `uv run`.

    ```bash
    uv run flowchart-architect/skills/generate-drawio/script/assembler.py \
      --logic_path "[ABSOLUTE_PATH_TO_LOGIC_JSON]" \
      --output_path "[ABSOLUTE_PATH_TO_OUTPUT_DRAWIO]" \
      [OPTIONAL_FLAGS]
    ```

    *Example:*
    ```bash
    uv run flowchart-architect/skills/generate-drawio/script/assembler.py \
      --logic_path "/Users/jarryfeng/projects/my-process/logic_structure.json" \
      --output_path "/Users/jarryfeng/projects/my-process/diagram.drawio" \
      --2l
    ```

## Output

-   `[output_path]`: The generated Draw.io XML file, ready to be opened in Draw.io.
