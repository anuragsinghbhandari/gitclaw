#!/usr/bin/env python3
import json
import uuid
import random
import sys
import os
import textwrap

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
    
    if label:
        # Instead of growing width, we wrap text to fit the width
        # Approx characters per line for current font size
        chars_per_line = max(10, int(width / 9))
        wrapped_text = "\n".join(textwrap.wrap(label, width=chars_per_line))
        
        # Calculate height based on number of lines
        line_count = wrapped_text.count("\n") + 1
        min_height = line_count * 25 + 20
        actual_height = max(height, min_height)
        
        node = create_element(shape, x=x, y=y, width=width, height=actual_height)
        text_element = create_element("text", x=x, y=y, width=width, height=actual_height, text=wrapped_text, containerId=node["id"])
        node["boundElements"] = [{"id": text_element["id"], "type": "text"}]
        data["elements"].extend([node, text_element])
        save_diagram(data)
        return node["id"]
    else:
        node = create_element(shape, x=x, y=y, width=width, height=height)
        data["elements"].append(node)
        save_diagram(data)
        return node["id"]

def add_arrow(from_id, to_id, label=""):
    data = load_diagram()
    
    from_elem = next((e for e in data["elements"] if e["id"] == from_id), None)
    to_elem = next((e for e in data["elements"] if e["id"] == to_id), None)
    
    if not from_elem or not to_elem:
        return None
    
    x1, y1 = from_elem["x"] + from_elem["width"] / 2, from_elem["y"] + from_elem["height"] / 2
    x2, y2 = to_elem["x"] + to_elem["width"] / 2, to_elem["y"] + to_elem["height"] / 2
    
    dx = x2 - x1
    dy = y2 - y1
    dist = (dx**2 + dy**2)**0.5
    
    if dist == 0:
        return None

    actual_start_x = x1
    actual_start_y = y1
    actual_end_x = x2
    actual_end_y = y2

    arrow = create_element("arrow", x=actual_start_x, y=actual_start_y, 
                           points=[[0, 0], [actual_end_x - actual_start_x, actual_end_y - actual_start_y]], 
                           startBinding={"elementId": from_id, "focus": 0, "gap": 1},
                           endBinding={"elementId": to_id, "focus": 0, "gap": 1})
    
    data["elements"].append(arrow)
    save_diagram(data)
    return arrow["id"]

def clear_diagram():
    if os.path.exists(DIAGRAM_FILE):
        os.remove(DIAGRAM_FILE)
    print("Diagram cleared.")

def export_html(output_path):
    data = load_diagram()
    json_data = json.dumps(data)
    
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Excalidraw Viewer</title>
    <style>
        body, html {{ margin: 0; padding: 0; height: 100%; width: 100%; overflow: hidden; background-color: #f8f9fa; }}
        #excalidraw-container {{ height: 100vh; width: 100vw; }}
    </style>
</head>
<body>
    <div id="excalidraw-container"></div>
    <script src="https://cdn.jsdelivr.net/npm/react@18/umd/react.production.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@excalidraw/excalidraw/dist/excalidraw.production.min.js"></script>
    <script>
        const diagramData = {json_data};
        const App = () => {{
            return React.createElement(ExcalidrawLib.Excalidraw, {{
                initialData: {{
                    elements: diagramData.elements,
                    appState: {{ viewBackgroundColor: "#ffffff" }},
                    scrollToContent: true
                }},
                viewModeEnabled: true
            }});
        }};
        const root = ReactDOM.createRoot(document.getElementById("excalidraw-container"));
        root.render(React.createElement(App));
    </script>
</body>
</html>"""
    with open(output_path, "w") as f:
        f.write(html_template)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "add_node":
        label = sys.argv[2]
        x = int(sys.argv[3])
        y = int(sys.argv[4])
        w = int(sys.argv[5]) if len(sys.argv) > 5 else 150
        h = int(sys.argv[6]) if len(sys.argv) > 6 else 80
        node_id = add_node(label, x, y, w, h)
        print(f"Added node: {node_id}")
    elif cmd == "add_arrow":
        from_id = sys.argv[2]
        to_id = sys.argv[3]
        arrow_id = add_arrow(from_id, to_id)
        print(f"Added arrow: {arrow_id}")
    elif cmd == "clear":
        clear_diagram()
    elif cmd == "export_html":
        output = sys.argv[2] if len(sys.argv) > 2 else "viewer.html"
        export_html(output)
