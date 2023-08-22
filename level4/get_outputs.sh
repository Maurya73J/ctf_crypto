#!/bin/bash

 ssh student@172.27.26.188 -t 2>/dev/null | python3 script.py | grep -A1 "Slowly, a new" | grep -v "Slowly" | sed 's/--//g' | grep -E '[a-z]' | sed 's/^[ \t]*//g' | sed '/^$/d' > output_random.txt
