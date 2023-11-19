import os
import re

dependencyGraph = {}

# Get all files in the current working directory
directory = os.getcwd()
for root, dirs, files in os.walk(directory):
    for filename in files:
        f = os.path.join(root, filename)
        dependencyGraph[f] = []

# Remove the current file
current_file_path = os.path.abspath(__file__)
del dependencyGraph[current_file_path]

# Build Graph
for key, lis in dependencyGraph.items():
    with open(key, 'r') as curFile:
        lines = curFile.readlines()
        for line in lines:
            match = re.match(r'^\s*from\s+(\S+)\s+import\s+\S+', line)
            if match:
                imported_module = match.group(1)
                dependencyGraph[key].append(imported_module)
            else:
                match = re.match(r'^\s*import\s+(\S+)', line)
                if match:
                    imported_module = match.group(1)
                    dependencyGraph[key].append(imported_module)
