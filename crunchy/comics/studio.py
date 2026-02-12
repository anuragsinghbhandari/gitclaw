#!/usr/bin/env python3
import os
import sys

EXCALIDRAW_TOOL = "./.pi/skills/excalidraw/scripts/excalidraw_tool.py"

def run_cmd(cmd, *args):
    arg_str = " ".join(f'"{a}"' for a in args)
    os.system(f"{EXCALIDRAW_TOOL} {cmd} {arg_str}")

def create_comic(title, panels):
    os.system(f"{EXCALIDRAW_TOOL} clear")
    
    # Title - centered
    run_cmd("add_node", title, 450, -150, 600, 60)
    
    for i, (crunch_says, human_says) in enumerate(panels):
        x_panel = i * 500
        y_panel = 0
        
        # 1. Panel Box (Outer)
        run_cmd("add_node", "", x_panel, y_panel, 450, 350)
        
        # 2. Characters (using squares as placeholders for "heads")
        # Crunch Node
        crunch_id = f"crunch_{i}" # Not actually used by tool but for mental mapping
        run_cmd("add_node", "🦃", x_panel + 50, y_panel + 240, 70, 70)
        
        # Human Node
        run_cmd("add_node", "👤", x_panel + 330, y_panel + 240, 70, 70)
        
        # 3. Speech Bubbles / Labels
        if crunch_says:
            # Bubble box
            run_cmd("add_node", crunch_says, x_panel + 30, y_panel + 30, 180, 100)
            # Arrow from crunch to bubble
            # Note: add_node returns id to stdout, but our run_cmd doesn't capture it easily.
            # I'll modify the tool usage or just use boxes for now to avoid ID-tracking complexity
            # since I want to fix the visual layout first.
        
        if human_says:
            # Bubble box
            run_cmd("add_node", human_says, x_panel + 240, y_panel + 30, 180, 100)

    # Export
    run_cmd("export_html", "viewer.html")
    # Also update index.html if it exists to point here
    print("Comic generated with better boxes!")

if __name__ == "__main__":
    import random
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
    story = random.choice(stories)
    create_comic(story["title"], story["panels"])
