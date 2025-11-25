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

### Spacing
- **Between Nodes**: Minimum 60px horizontal, 40px vertical.
- **Padding**: Keep 20px padding inside swimlane borders.

## Shape Standards

| Element | Shape | Style |
|---------|-------|-------|
| **Start/End** | Rounded Rectangle / Capsule | Green fill, White text |
| **Process Step** | Rectangle | White fill, Blue stroke |
| **Decision** | Diamond | White fill, Purple stroke |
| **Document** | Wave-bottom Rectangle | White fill, Black stroke |
| **Database** | Cylinder | Grey fill, Black text |
| **System Action** | Rectangle with Gear Icon | Light Grey fill |

## Connection Rules

- **Flow Direction**: Generally Left-to-Right or Top-to-Bottom.
- **Yes/No Labels**: "Yes" path should go straight or right. "No" path should branch down or loop back.
- **Crossings**: Avoid line crossings whenever possible. Use "Jump" style if crossing is unavoidable.
