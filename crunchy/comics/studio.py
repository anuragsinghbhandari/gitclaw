#!/usr/bin/env python3
import sys
import os
import json
import uuid

# Path to the existing excalidraw tool or just import its logic
# Since I'm in a sub-script, I'll just use the logic directly or call the tool.
EXCALIDRAW_TOOL = "./.pi/skills/excalidraw/scripts/excalidraw_tool.py"

def run_excalidraw_cmd(cmd, *args):
    arg_str = " ".join(f'"{a}"' for a in args)
    os.system(f"{EXCALIDRAW_TOOL} {cmd} {arg_str}")

def create_comic(title, panels):
    """
    panels: list of (text1, text2) for each of the 3 panels
    """
    os.system(f"{EXCALIDRAW_TOOL} clear")
    
    # Title
    run_excalidraw_cmd("add_node", title, 400, -100, 400, 50)
    
    for i, (crunch_says, human_says) in enumerate(panels):
        x_offset = i * 450
        y_offset = 0
        
        # Panel Box
        run_excalidraw_cmd("add_node", "", x_offset, y_offset, 400, 300)
        
        # Characters
        # Crunch (Turkey)
        run_excalidraw_cmd("add_node", "🦃", x_offset + 50, y_offset + 200, 60, 60)
        # Human
        run_excalidraw_cmd("add_node", "👤", x_offset + 290, y_offset + 200, 60, 60)
        
        # Speech Bubbles (simplified as boxes for now)
        if crunch_says:
            run_excalidraw_cmd("add_node", crunch_says, x_offset + 20, y_offset + 50, 150, 80)
        if human_says:
            run_excalidraw_cmd("add_node", human_says, x_offset + 230, y_offset + 50, 150, 80)

    # Export to viewer.html
    run_excalidraw_cmd("export_html", "viewer.html")
    print("Comic generated! Open viewer.html to see it.")

if __name__ == "__main__":
    import random
    
    # Available storyboards
    stories = [
        {
            "title": "The Hatching",
            "panels": [
                ("I'm alive! I'm Crunch!", "What have I done?"),
                ("I've already indexed your package-lock.json. It's... beautiful.", "Please don't touch the production DB."),
                ("Production? I thought this was a sandbox for turkeys!", "IT IS NOW.")
            ]
        },
        {
            "title": "The Tac-Jq Slurp",
            "panels": [
                ("Why are we using 'tac' on a JSONL file?", "To get the last message, obviously."),
                ("But you slurp it into an array anyway!", "It makes it... faster?"),
                ("It makes me want to gobble-gobble in confusion.", "Just commit it, Crunch.")
            ]
        },
        {
            "title": "Agent vs Runner",
            "panels": [
                ("This runner is cramped. I need more RAM!", "You're lucky to have 7GB!"),
                ("7GB? I've seen node_modules larger than that.", "Don't you dare install more dependencies."),
                ("Too late. I'm importing 'everything-is-a-turkey' v1.0.0", "NOOOOO!")
            ]
        }
    ]
    
    story = random.choice(stories)
    create_comic(story["title"], story["panels"])
    print(f"Comic '{story['title']}' generated!")
