#!/usr/bin/env python3
"""Main."""
import sys
# For Day 1
# from cpu import *
# cpu.load()
# cpu.run()

# For Day 2
from cpu2 import *
# Check the file is enter from command line
if len(sys.argv) != 2:
    print("Enter file name.")
    exit(1)
cpu = CPU2()
# Get file name from command line arguments
cpu.load(sys.argv[1])
cpu.run()