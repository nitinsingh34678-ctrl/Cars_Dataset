import networkx as nwx
graph = nwx.Graph()
while True:
    choice = int(input("Want to insert nodes and enter edge press? 1 for yes and 2 for no"))
    if choice == 1:
        node1 = input("Enter node1 ").strip().upper()
        node2 = input("Enter node2 ").strip().upper()
        weight = int(input("Enter weight between node1 and node2 "))
        graph.add_edge(node1, node2, weight = weight)
    else:
        break
print(f"\nGraph")
graph.adj.items()
for node, neighbors in graph.adj.items():
    print(node, neighbors)
start = input("Enter start node").strip().upper()
goal = input("Enter goal node").strip().upper()
graph.nodes()
heuristic_values = {}
heuristic_values[goal] = 0
for node in graph.nodes():
    if node != goal:
        heuristic_val = int(input(f"Enter the heuristic value from node {node} to goal node {goal} "))
        heuristic_values[node] = heuristic_val   
        def get_heuristic(u,v):
            return heuristic_values[u]
path = nwx.astar_path(graph, start, goal, heuristic=get_heuristic, weight='weight')
"->".join(path)
total_cost = nwx.astar_path_length(graph, start, goal, heuristic=get_heuristic, weight='weight')
path_length=len(path)
max_weight=0
for i in range(len(path)-1):
    weight=graph[path[i]][path[i+1]]['weight']
    if weight >max_weight:
        max_weight = weight
print("\n shortest path : ""->".join(path))
print("path lenght",path_length)
print("Total Cost : ",total_cost)
print("max weight",max_weight)