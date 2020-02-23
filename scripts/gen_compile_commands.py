#!/usr/bin/env python3

import json
import glob

def main():
    commands = []
    for fn in glob.glob("build/*/compile_commands.json"):
        with open(fn) as f:
            cmds = json.load(f)
        if not (isinstance(cmds, list) and len(cmds)):
            print("[ERROR] something is wrong in: " + fn)
        commands.extend(cmds)

    with open("compile_commands.json", "w") as f:
        json.dump(commands, f, indent=2)

if __name__ == '__main__': main()
