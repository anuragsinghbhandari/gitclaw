---
name: excalidraw
description: Build and maintain Excalidraw architecture diagrams. Use this when the user asks to "draw", "diagram", or "visualize" an architecture or process.
---

# Excalidraw Skill

This skill allows you to create and manipulate architecture diagrams using the Excalidraw format.

## Overview

The skill manages a `diagram.excalidraw` file in the current workspace. You can add nodes (rectangles with labels) and arrows to represent systems, components, and their relationships.

## Core Capabilities

### 1. Add Nodes
Create a shape with a text label at specific coordinates.
```bash
./.pi/skills/excalidraw/scripts/excalidraw_tool.py add_node "User" 100 100
```

### 2. Connect Nodes
Create an arrow between two existing nodes by their IDs.
```bash
./.pi/skills/excalidraw/scripts/excalidraw_tool.py add_arrow <from_id> <to_id> "API Request"
```

### 3. Move Elements
Update the position of a node.
```bash
./.pi/skills/excalidraw/scripts/excalidraw_tool.py move <id> <new_x> <new_y>
```

### 4. Delete Elements
Remove a node or arrow.
```bash
./.pi/skills/excalidraw/scripts/excalidraw_tool.py delete <id>
```

### 5. List Elements
View current elements and their IDs.
```bash
./.pi/skills/excalidraw/scripts/excalidraw_tool.py list
```

### 7. View Diagram
I've provided an `export_html` command. It creates a standalone HTML file with the diagram data embedded, which bypasses CORS issues when opening locally.
```bash
./.pi/skills/excalidraw/scripts/excalidraw_tool.py export_html viewer.html
```
Open `viewer.html` in your browser to see the masterpiece.

## Workflow: Building an Architecture

1.  **Plan the layout**: Mentally or on paper, decide where components should go (e.g., User on the left, API in the middle, DB on the right).
2.  **Clear the diagram** (optional): `clear` if starting fresh.
3.  **Add components**: Use `add_node` for each component. Note the IDs returned.
4.  **Connect them**: Use `add_arrow` with the recorded IDs.
5.  **Review**: Use `list` to verify the structure.
6.  **Deliver**: Tell the user the `diagram.excalidraw` file is ready. They can open it at [excalidraw.com](https://excalidraw.com) by dragging and dropping the file onto the canvas.

## Resources

### scripts/
- `excalidraw_tool.py`: Python script for manipulating the `.excalidraw` JSON file.
