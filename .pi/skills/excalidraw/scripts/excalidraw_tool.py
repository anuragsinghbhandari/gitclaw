#!/usr/bin/env python3
import json
import uuid
import random
import sys
import os

DIAGRAM_FILE = "diagram.excalidraw"

def load_diagram():
    if os.path.exists(DIAGRAM_FILE):
        with open(DIAGRAM_FILE, "r") as f:
            return json.load(f)
    else:
        return {
            "type": "excalidraw",
            "version": 2,
            "source": "https://github.com/gitclaw/gitclaw",
            "elements": [],
            "appState": {
                "viewBackgroundColor": "#ffffff",
                "gridSize": 20
            },
            "files": {}
        }

def save_diagram(data):
    with open(DIAGRAM_FILE, "w") as f:
        json.dump(data, f, indent=2)

def create_element(element_type, **kwargs):
    element = {
        "id": str(uuid.uuid4()),
        "type": element_type,
        "x": kwargs.get("x", 0),
        "y": kwargs.get("y", 0),
        "width": kwargs.get("width", 100),
        "height": kwargs.get("height", 100),
        "strokeColor": kwargs.get("strokeColor", "#1e1e1e"),
        "backgroundColor": kwargs.get("backgroundColor", "transparent"),
        "fillStyle": kwargs.get("fillStyle", "solid"),
        "strokeWidth": kwargs.get("strokeWidth", 2),
        "strokeStyle": kwargs.get("strokeStyle", "solid"),
        "roughness": kwargs.get("roughness", 1),
        "opacity": kwargs.get("opacity", 100),
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": 3} if element_type in ["rectangle", "diamond"] else None,
        "seed": random.randint(1, 1000000),
        "version": 1,
        "versionNonce": random.randint(1, 1000000),
        "isDeleted": False,
        "boundElements": None,
        "updated": 1,
        "link": None,
        "locked": False
    }
    
    if element_type == "text":
        element.update({
            "text": kwargs.get("text", ""),
            "fontSize": kwargs.get("fontSize", 20),
            "fontFamily": kwargs.get("fontFamily", 1),
            "textAlign": kwargs.get("textAlign", "center"),
            "verticalAlign": kwargs.get("verticalAlign", "middle"),
            "baseline": 18,
            "containerId": kwargs.get("containerId", None),
            "originalText": kwargs.get("text", "")
        })
    elif element_type == "arrow":
        element.update({
            "points": kwargs.get("points", [[0, 0], [100, 100]]),
            "lastCommittedPoint": None,
            "startBinding": kwargs.get("startBinding", None),
            "endBinding": kwargs.get("endBinding", None),
            "startArrowhead": None,
            "endArrowhead": "arrow"
        })
        # For arrows, width and height are determined by points
        pts = element["points"]
        min_x = min(p[0] for p in pts)
        max_x = max(p[0] for p in pts)
        min_y = min(p[1] for p in pts)
        max_y = max(p[1] for p in pts)
        element["width"] = max_x - min_x
        element["height"] = max_y - min_y

    return element

def add_node(label, x, y, width=150, height=80, shape="rectangle"):
    data = load_diagram()
    
    # Create the shape
    node = create_element(shape, x=x, y=y, width=width, height=height)
    
    # Create the text
    text_element = create_element("text", x=x, y=y, width=width, height=height, text=label, containerId=node["id"])
    
    # Bind text to node
    node["boundElements"] = [{"id": text_element["id"], "type": "text"}]
    
    data["elements"].extend([node, text_element])
    save_diagram(data)
    return node["id"]

def add_arrow(from_id, to_id, label=""):
    data = load_diagram()
    
    from_elem = next((e for e in data["elements"] if e["id"] == from_id), None)
    to_elem = next((e for e in data["elements"] if e["id"] == to_id), None)
    
    if not from_elem or not to_elem:
        print(f"Error: Could not find node {from_id} or {to_id}")
        return
    
    # Calculate center points
    x1, y1 = from_elem["x"] + from_elem["width"] / 2, from_elem["y"] + from_elem["height"] / 2
    x2, y2 = to_elem["x"] + to_elem["width"] / 2, to_elem["y"] + to_elem["height"] / 2
    
    arrow = create_element("arrow", x=x1, y=y1, points=[[0, 0], [x2-x1, y2-y1]], 
                           startBinding={"elementId": from_id, "focus": 0, "gap": 1},
                           endBinding={"elementId": to_id, "focus": 0, "gap": 1})
    
    data["elements"].append(arrow)
    
    if label:
        # Add label text to the arrow
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        text_label = create_element("text", x=mid_x - 50, y=mid_y - 10, width=100, height=20, text=label)
        data["elements"].append(text_label)

    save_diagram(data)
    return arrow["id"]

def clear_diagram():
    if os.path.exists(DIAGRAM_FILE):
        os.remove(DIAGRAM_FILE)
    print("Diagram cleared.")

def list_elements():
    data = load_diagram()
    for e in data["elements"]:
        if e["type"] == "text" and "containerId" in e and e["containerId"]:
            continue # Skip bound text labels for brevity
        label = ""
        if e["type"] != "text":
            # try to find bound text
            bound_text = next((t for t in data["elements"] if t["type"] == "text" and t.get("containerId") == e["id"]), None)
            if bound_text:
                label = f" ({bound_text['text']})"
        else:
            label = f" ({e['text']})"
            
        print(f"{e['id']}: {e['type']}{label} at ({e['x']}, {e['y']})")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: excalidraw_tool.py [add_node|add_arrow|clear|list] ...")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "add_node":
        label = sys.argv[2]
        x = int(sys.argv[3])
        y = int(sys.argv[4])
        node_id = add_node(label, x, y)
        print(f"Added node: {node_id}")
    elif cmd == "add_arrow":
        from_id = sys.argv[2]
        to_id = sys.argv[3]
        label = sys.argv[4] if len(sys.argv) > 4 else ""
        arrow_id = add_arrow(from_id, to_id, label)
        print(f"Added arrow: {arrow_id}")
    elif cmd == "clear":
        clear_diagram()
    elif cmd == "list":
        list_elements()
    elif cmd == "delete":
        element_id = sys.argv[2]
        data = load_diagram()
        data["elements"] = [e for e in data["elements"] if e["id"] != element_id and e.get("containerId") != element_id]
        save_diagram(data)
        print(f"Deleted element: {element_id}")
    elif cmd == "move":
        element_id = sys.argv[2]
        new_x = int(sys.argv[3])
        new_y = int(sys.argv[4])
        data = load_diagram()
        for e in data["elements"]:
            if e["id"] == element_id:
                dx = new_x - e["x"]
                dy = new_y - e["y"]
                e["x"] = new_x
                e["y"] = new_y
                # If it's a container, move bound text too
                for t in data["elements"]:
                    if t.get("containerId") == element_id:
                        t["x"] += dx
                        t["y"] += dy
                break
        save_diagram(data)
        print(f"Moved element: {element_id}")
    else:
        print(f"Unknown command: {cmd}")
