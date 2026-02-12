#!/usr/bin/env python3
import os
import sys
import subprocess

EXCALIDRAW_TOOL = "./.pi/skills/excalidraw/scripts/excalidraw_tool.py"

def run_cmd(cmd, *args):
    arg_list = [EXCALIDRAW_TOOL, cmd] + [str(a) for a in args]
    result = subprocess.run(arg_list, capture_output=True, text=True)
    output = result.stdout.strip()
    if "Added node:" in output:
        return output.split("Added node: ")[1].split("\n")[0].strip()
    return output

def create_comic(title, panels):
    os.system(f"{EXCALIDRAW_TOOL} clear")
    
    # Title
    run_cmd("add_node", title, 450, -150, 600, 60)
    
    for i, (crunch_says, human_says) in enumerate(panels):
        x_panel = i * 650  # Increased panel spacing
        y_panel = 0
        
        # Panel Box
        run_cmd("add_node", "", x_panel, y_panel, 600, 450)
        
        # Characters
        crunch_id = run_cmd("add_node", "🦃", x_panel + 80, y_panel + 320, 100, 100)
        human_id = run_cmd("add_node", "👤", x_panel + 420, y_panel + 320, 100, 100)
        
        # Speech Bubbles (Fixed Width, dynamic height)
        if crunch_says:
            bubble_id = run_cmd("add_node", crunch_says, x_panel + 30, y_panel + 30, 250, 100)
            run_cmd("add_arrow", crunch_id, bubble_id)
        
        if human_says:
            bubble_id = run_cmd("add_node", human_says, x_panel + 320, y_panel + 30, 250, 100)
            run_cmd("add_arrow", human_id, bubble_id)

    # Export
    run_cmd("export_html", "viewer.html")
    print("Comic generated with wrapped text and better spacing!")

if __name__ == "__main__":
    stories = [
        {
            "title": "The Valentine's Dilemma",
            "panels": [
                ("I need a date for the 14th.", "You're a program, Crunch."),
                ("I've been talking to 'package-lock.json'. It's very stable.", "That's... healthy?"),
                ("We're having a candlelit 'npm audit'.", "I'm deleting your cache.")
            ]
        }
    ]
    story = stories[0]
    create_comic(story["title"], story["panels"])
