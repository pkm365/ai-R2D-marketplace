# Component Library

Definitions of standard components available for generation.

## Standard Nodes

### `process_step`
- **Type**: `mxGraph.shape.rectangle`
- **Default Size**: 130x50
- **Style**: `whiteSpace=wrap;html=1;rounded=0;strokeColor=#0056b3;strokeWidth=2;arcSize=14;fillColor=#ffffff;fontColor=#000000;`
- **Note**: Uses Corporate Blue stroke with professional rounding.

### `decision_node`
- **Type**: `mxGraph.shape.rhombus`
- **Default Size**: 80x80
- **Style**: `rhombus;whiteSpace=wrap;html=1;strokeColor=#6f42c1;strokeWidth=2;fillColor=#ffffff;fontColor=#000000;`
- **Note**: Uses Logic Purple stroke.

### `terminator`
- **Type**: `mxGraph.shape.ellipse`
- **Default Size**: 80x40
- **Style**: `ellipse;whiteSpace=wrap;html=1;fillColor=#28a745;strokeColor=#28a745;fontColor=#ffffff;`
- **Note**: Solid Green fill for Start/End.

### `document` (Data Input/Output)
- **Type**: `mxGraph.shape.document`
- **Default Size**: 130x60
- **Style**: `shape=document;whiteSpace=wrap;html=1;boundedLbl=1;strokeColor=#666666;strokeWidth=2;fillColor=#FFFEC8;fontColor=#333333;`
- **Note**: Uses Legacy Yellow fill for clear data distinction.

## Swimlanes

### `pool` (Container)
- **Type**: `mxGraph.shape.swimlane`
- **Style**: `swimlane;html=1;childLayout=stackLayout;horizontal=1;startSize=20;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;`

### `lane` (Swimlane)
- **Type**: `mxGraph.shape.swimlane`
- **Style**: `swimlane;html=1;startSize=20;horizontal=0;`

## Connectors

### `sequence_flow`
- **Style**: `edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#000000;strokeWidth=1;`

### `data_association`
- **Style**: `edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;strokeColor=#666666;strokeWidth=1;`
