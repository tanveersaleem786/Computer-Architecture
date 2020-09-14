#!/usr/bin/env python3
"""Main."""
import sys
# For Day 1
# PS C:\wamp64\www\lambda\repos\7-Computer Science\7-Computer Architecture\Computer-Architecture\ls8> python ls8.py examples/print8.ls8
# from cpu import *
# cpu.load()
# cpu.run()

# For Day 2
# PS C:\wamp64\www\lambda\repos\7-Computer Science\7-Computer Architecture\Computer-Architecture\ls8> python ls8.py examples/mult.ls8

# from cpu2 import *
# # Check the file is enter from command line
# if len(sys.argv) != 2:
#     print("Enter file name.")
#     exit(1)
# cpu = CPU2()
# # Get file name from command line arguments
# cpu.load(sys.argv[1])
# cpu.run()

# Day 3
# Run PS C:\wamp64\www\lambda\repos\7-Computer Science\7-Computer Architecture\Computer-Architecture\ls8> python ls8.py examples/stack.ls8
# from cpu3 import *
# # Check the file is enter from command line
# if len(sys.argv) != 2:
#     print("Enter file name.")
#     exit(1)
# cpu = CPU3()
# # Get file name from command line arguments
# cpu.load(sys.argv[1])
# cpu.run()

# Day 4 
# Run PS C:\wamp64\www\lambda\repos\7-Computer Science\7-Computer Architecture\Computer-Architecture\ls8> python ls8.py examples/call.ls8
from cpu4 import *
# Check the file is enter from command line
if len(sys.argv) != 2:
    print("Enter file name.")
    exit(1)
cpu = CPU4()
# Get file name from command line arguments
cpu.load(sys.argv[1])
cpu.run()

