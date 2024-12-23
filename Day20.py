import networkx as nx
from itertools import combinations

# Read the grid input from the file
with open("in.txt") as f:
    ls = f.read().strip().split("\n")

# Create the grid graph based on the grid size
G = nx.grid_2d_graph(len(ls), len(ls[0]))

start = None  # Initialize start to None to handle cases where 'S' might not be found

# Parse the grid and remove walls from the graph
for i, l in enumerate(ls):
    for j, x in enumerate(l):
        p = (i, j)
        if x == "#":
            G.remove_node(p)  # Remove walls
        elif x == "S":
            start = p  # Record the start position

# Ensure that the starting point exists
if start is None:
    raise ValueError("Starting point 'S' not found in the grid!")

# Calculate shortest path lengths from the start using Dijkstra's algorithm
dist = nx.single_source_dijkstra_path_length(G, start)

# Function to calculate the number of "good cheats" based on the cheat distance
def solve(cheat_dist):
    # Compare all pairs of nodes and check if they satisfy the cheat conditions
    return sum(
        # Manhattan distance between points (p1, p2) and (q1, q2) is within the cheat distance
        (d := abs(p1 - q1) + abs(p2 - q2)) <= cheat_dist and 
        # Time saved (difference in path lengths) is greater than or equal to 100
        d2 - d1 - d >= 100
        for ((p1, p2), d1), ((q1, q2), d2) in combinations(dist.items(), 2)
    )

# Part 1: Print the result for cheat distance 2
print("Part 1:", solve(2))

# Part 2: Print the result for cheat distance 20
print("Part 2:", solve(20))
