# Strict Process Flow Matrix Template

Use this table to define your process logic. The script will convert this directly into the diagram structure.

## Rules
1. **ID**: Must be unique (e.g., 010, 020).
2. **Role**: Defines the Swimlane. Consistent spelling is required.
3. **Type**: `process`, `decision`, `terminator`.
4. **Next**:
    - Simple: `020`
    - Decision: `Yes: 030, No: 040`
    - Terminator: Leave empty
5. **System/Documents**: Optional.

## Matrix

| ID | Role | Description | Type | Next | System | Documents |
|----|------|-------------|------|------|--------|-----------|
| 010 | [Role A] | [Start Process] | process | 020 | | |
| 020 | [Role B] | [Action Step] | process | 030 | [System] | [Doc Name] |
| 030 | [Role B] | [Decision Point?] | decision | Yes: 040, No: 020 | | |
| 040 | [Role A] | [End Process] | terminator | | | |
