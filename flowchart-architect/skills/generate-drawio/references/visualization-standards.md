# Visualization Standards (Strict Assembly)

## 1. Core Principle
**"Assembly over Creation"**: Do not generate random styles. Strictly assemble the diagram using the constants below.

## 2. Canvas & Layout
- **Page Width**: 827px (A4)
- **Container Width**: 800px
- **Columns**:
    1. **Seq**: 40px
    2. **I/O Docs**: 120px
    3. **Dept 1**: 163px
    4. **Dept 2**: 163px
    5. **Dept 3**: 164px
    6. **Description**: 150px

## 3. Strict Color Palette
| Element | Hex Code |
| :--- | :--- |
| **Header** | `#f8f9fa` |
| **Dept 1** | `#ffffff` |
| **Dept 2** | `#ffffff` |
| **Dept 3** | `#ffffff` |
| **Process Node** | `#ffffff` (Stroke: `#0056b3`) |
| **System Tag** | `#000099` (Text: `#ffffff`) |

## 4. Component Snippets (XML Patterns)

### Process Box (Fixed 100x50)
```xml
<mxCell id="[id]" value="[Name]" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0056b3;fontSize=10;" vertex="1" parent="[lane_id]">
  <mxGeometry x="[center_x]" y="[y]" width="100" height="50" as="geometry"/>
</mxCell>
```

### Decision Node (60x60)
```xml
<mxCell id="[id]" value="?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#6f42c1;strokeWidth=2;fontSize=10;" vertex="1" parent="[lane_id]">
  <mxGeometry x="[center_x]" y="[y]" width="60" height="60" as="geometry"/>
</mxCell>
```

### Document with System Tag (Group)
```xml
<mxCell id="[id]_group" value="" style="group" vertex="1" connectable="0" parent="[lane_id]">
  <mxGeometry x="[center_x]" y="[y]" width="100" height="60" as="geometry"/>
</mxCell>
<mxCell id="[id]_doc" value="[Name]" style="shape=document;whiteSpace=wrap;html=1;boundedLbl=1;size=0.25;fontSize=10;" vertex="1" parent="[id]_group">
  <mxGeometry width="100" height="60" as="geometry"/>
</mxCell>
<mxCell id="[id]_tag" value="&lt;b&gt;[TAG]&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#000099;fontColor=#ffffff;strokeColor=none;align=center;verticalAlign=middle;fontSize=9;" vertex="1" parent="[id]_group">
  <mxGeometry width="26" height="12" as="geometry"/>
</mxCell>
```

### Connector (Orthogonal)
```xml
<mxCell id="edge-[from]-[to]" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#000000;" edge="1" parent="[container_id]" source="[from]" target="[to]">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```
