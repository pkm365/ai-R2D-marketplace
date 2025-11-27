# Logic Structure JSON Schema

This schema defines the input format for `assembler.py`. To generate a standardized Draw.io flowchart, the AI must extract the image content into this JSON structure.

## Root Object
| Field | Type | Description |
|---|---|---|
| `meta` | Object | Metadata (process_name, owner, date). |
| `swimlanes` | Array | List of swimlane definitions. |
| `steps` | Array | Ordered list of process steps. |

## Swimlane Object
| Field | Type | Description |
|---|---|---|
| `id` | String | Unique ID (e.g., "lane_pmc"). |
| `name` | String | Display name (e.g., "PMC"). |
| `type` | String | "department" (wide) or "system" (narrow, deprecated if unused). |

## Step Object
| Field | Type | Description |
|---|---|---|
| `id` | String | Unique ID (e.g., "step_10"). |
| `type` | String | `process`, `subprocess` (double lines), `decision` (diamond), `terminator` (oval). |
| `name` | String | Main text label. |
| `description` | String | (Optional) Side note text. |
| `lane_id` | String | ID of the swimlane this step belongs to. |
| `system_tag` | String | (Optional) e.g., "ERP". Adds a system tag group. |
| `doc_ref` | String | (Optional) Input document name. Adds document icon. |
| `doc_output` | String | (Optional) Output document name. Adds document icon. |
| `next` | Array/Dict | List of next step IDs (for process) or Dict of Label->ID (for decision). |
| `x_offset` | Integer | (Optional) Horizontal shift in pixels. Use `-90` for parallel split points. |
| `port_config` | Object | (Optional) Fine-grained control over connection points. |

### Port Config Object
Controls how arrows enter/exit this step.
| Field | Type | Description |
|---|---|---|
| `entry` | String | "top", "bottom", "left", "right". Default: "top". |
| `exit` | String | "top", "bottom", "left", "right". Default: "bottom". |
| `jetty` | Integer | (Optional) Length of straight line before turning. Use `60` for wide parallel merges. |

## Layout Strategies (AI Instructions)

### 1. Standard Flow
- **Default**: No config needed. Arrows go Bottom -> Top.

### 2. Parallel Split (1-to-Many)
- **Start Node**: Set `x_offset: -90` to create a vertical "bus" line on the left.
- **Parallel Steps**: Set `port_config: { "entry": "left" }` to accept arrows from the bus.

### 3. Parallel Merge (Many-to-1)
- **Parallel Steps**: Set `port_config: { "exit": "right", "jetty": 60 }`.
- **Effect**: Arrows travel wide to the right and overlap vertically before dropping to the next step.

### 4. Decision Bypass ("No" Path)
- **Logic**: If label is "No", the script automatically defaults to `exit: right`, `entry: right`, `jetty: 40`.
- **Manual Override**: Can be overridden via `port_config` if needed.

### 5. Loop Back (Upward)
- **Logic**: If target is physically above source, script defaults to `exit: right`, `entry: top` (C-shape loop).
