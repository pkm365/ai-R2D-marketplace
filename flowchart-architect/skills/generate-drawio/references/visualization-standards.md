# Visualization Standards

Standard rules for layout, spacing, and shape usage in flowcharts.

## Layout Rules

### Swimlanes
- **Orientation**: Horizontal (Left-to-Right) is preferred for time-based processes. Vertical (Top-to-Down) for hierarchical flows.
- **Ordering**:
    - **Customer/External**: Topmost swimlane
    - **Front Office**: Middle swimlanes
    - **Back Office/Systems**: Bottom swimlanes
- **Height/Width**: Minimum 150px per swimlane.

### Spacing Guidelines (Legacy Standard)
- **Vertical gap between elements**: 80-100px
- **Horizontal margin within lane**: 10-35px
- **Lane top margin**: 20px (after swimlane header)
- **Padding**: Keep 20px padding inside swimlane borders.

## Dimension Guidelines

### Standard Sizes
- **Process box**: 130x50 px
- **Data box**: 130x60 px
- **Start/End**: 80x40 px
- **Decision**: 80x80 px

### Grid System
- Geometry uses **10-unit grid** coordinates.
- Align all centers to the swimlane center line.

## XML Template Patterns

### Basic Process Box
```xml
<mxCell id="[unique-id]" 
  value="[Step Name]" 
  style="whiteSpace=wrap;html=1;rounded=0;strokeColor=#0056b3;strokeWidth=2;arcSize=14;fillColor=#ffffff;" 
  parent="[lane-id]" vertex="1">
  <mxGeometry x="[x]" y="[y]" width="130" height="50" as="geometry"/>
</mxCell>
```

### Basic Connector/Edge
```xml
<mxCell id="edge-[from]-[to]" 
  style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#000000;" 
  parent="[container-id]" source="[source-id]" target="[target-id]" edge="1">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Labeled Connector (Decision Branch)
```xml
<mxCell id="edge-label-[id]" 
  value="Yes" 
  style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" 
  parent="edge-[from]-[to]" vertex="1" connectable="0">
  <mxGeometry x="-0.2" y="0" relative="1" as="geometry">
    <mxPoint as="offset"/>
  </mxGeometry>
</mxCell>
```

### Swimlane Definition
```xml
<mxCell id="[lane-id]" 
  value="[Lane Name]" 
  style="swimlane;html=1;startSize=20;horizontal=0;" 
  parent="swimlane-container" vertex="1">
  <mxGeometry x="[x]" y="0" width="[width]" height="[total-height]" as="geometry"/>
</mxCell>
```
