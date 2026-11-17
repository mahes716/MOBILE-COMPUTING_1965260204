import os
import random
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

random.seed(42)

for folder in ["diagrams", "results", "graphs"]:
    os.makedirs(folder, exist_ok=True)

# Create MANET topology
G = nx.Graph()
edges = [
    ("A", "B"), ("A", "C"), ("B", "D"),
    ("C", "D"), ("C", "E"), ("D", "F"),
    ("E", "F"), ("F", "G")
]
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

def draw_network(graph, title, filename, path=None):
    plt.figure(figsize=(8, 5))
    nx.draw(
        graph, pos, with_labels=True,
        node_color="skyblue", node_size=1000,
        font_weight="bold", edge_color="gray"
    )

    if path and len(path) > 1:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(
            graph, pos, edgelist=path_edges,
            edge_color="red", width=3
        )

    plt.title(title)
    plt.savefig(filename, bbox_inches="tight")
    plt.show()
    plt.close()

draw_network(
    G, "Initial MANET Topology",
    "diagrams/initial_topology.png"
)

# AODV route discovery using RREQ and RREP
source = "A"
destination = "G"

def aodv_route_discovery(graph, source, destination):
    visited = {source}
    queue = [source]
    parent = {source: None}
    rreq_count = 0

    while queue:
        current = queue.pop(0)

        if current == destination:
            break

        for neighbor in graph.neighbors(current):
            rreq_count += 1

            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    if destination not in parent:
        return None, rreq_count, 0

    path = []
    node = destination

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    rrep_count = len(path) - 1

    return path, rreq_count, rrep_count


aodv_path, rreq, rrep = aodv_route_discovery(
    G, source, destination
)

if aodv_path:
    print("AODV ROUTE DISCOVERY")
    print("Source:", source)
    print("Destination:", destination)
    print("Discovered Route:", " -> ".join(aodv_path))
    print("RREQ transmissions:", rreq)
    print("RREP transmissions:", rrep)

    draw_network(
        G, "AODV Discovered Route",
        "diagrams/aodv_route.png", aodv_path
    )

# Simulate link failure and route maintenance
failed_graph = G.copy()
failed_graph.remove_edge("C", "E")

print("\nAODV ROUTE MAINTENANCE")
print("Failed link: C - E")
print("RERR: Route error generated for the broken route")

new_path, new_rreq, new_rrep = aodv_route_discovery(
    failed_graph, source, destination
)

if new_path:
    print("Alternative Route:", " -> ".join(new_path))
else:
    print("No alternative route available")

draw_network(
    failed_graph, "Topology After Link Failure",
    "diagrams/topology_after_failure.png",
    new_path
)

# DSDV-inspired proactive routing table
def dsdv_routes(graph, source):
    routes = []

    for destination in graph.nodes():
        if source == destination:
            routes.append({
                "Source": source,
                "Destination": destination,
                "Next Hop": "-",
                "Hops": 0,
                "Route Status": "Available"
            })
        elif nx.has_path(graph, source, destination):
            path = nx.shortest_path(graph, source, destination)
            routes.append({
                "Source": source,
                "Destination": destination,
                "Next Hop": path[1],
                "Hops": len(path) - 1,
                "Route Status": "Available"
            })
        else:
            routes.append({
                "Source": source,
                "Destination": destination,
                "Next Hop": "-",
                "Hops": -1,
                "Route Status": "Unavailable"
            })

    return routes


dsdv_table = dsdv_routes(G, source)
pd.DataFrame(dsdv_table).to_csv(
    "results/dsdv_routing_table.csv", index=False
)

# Compare AODV and DSDV
aodv_delay = 25 + (rreq * 2) + (rrep * 2)
dsdv_delay = 25

comparison = pd.DataFrame([
    {
        "Protocol": "AODV",
        "Route Discovery": "On demand",
        "Control Messages": rreq + rrep,
        "Initial Delay (ms)": aodv_delay,
        "Routing Table": "Routes maintained when needed",
        "Mobility Handling": "Route rediscovery after failure"
    },
    {
        "Protocol": "DSDV",
        "Route Discovery": "Proactive",
        "Control Messages": len(G.nodes()) * (len(G.nodes()) - 1),
        "Initial Delay (ms)": dsdv_delay,
        "Routing Table": "Routes maintained continuously",
        "Mobility Handling": "Routing updates after topology changes"
    }
])

comparison.to_csv(
    "results/aodv_dsdv_comparison.csv", index=False
)

# Network size analysis
network_sizes = [5, 10, 15, 20, 25]
size_results = []

for size in network_sizes:
    network = nx.gnp_random_graph(size, 0.3, seed=size)

    if not nx.is_connected(network):
        largest = max(nx.connected_components(network), key=len)
        network = network.subgraph(largest).copy()

    node_count = len(network.nodes())
    aodv_overhead = network.number_of_edges()
    dsdv_overhead = node_count * max(node_count - 1, 0)

    size_results.append({
        "Network Size": size,
        "Connected Nodes": node_count,
        "AODV Discovery Overhead": aodv_overhead,
        "DSDV Update Entries Estimate": dsdv_overhead
    })

size_df = pd.DataFrame(size_results)
size_df.to_csv(
    "results/network_size_comparison.csv", index=False
)

# Routing overhead graph
plt.figure(figsize=(8, 5))
plt.plot(
    size_df["Network Size"],
    size_df["AODV Discovery Overhead"],
    marker="o", label="AODV"
)
plt.plot(
    size_df["Network Size"],
    size_df["DSDV Update Entries Estimate"],
    marker="s", label="DSDV"
)
plt.xlabel("Network Size")
plt.ylabel("Estimated Control Entries")
plt.title("AODV vs DSDV Routing Overhead")
plt.legend()
plt.grid(True)
plt.savefig(
    "graphs/routing_overhead_comparison.png",
    bbox_inches="tight"
)
plt.show()
plt.close()

# Initial delay comparison graph
plt.figure(figsize=(7, 5))
plt.bar(
    comparison["Protocol"],
    comparison["Initial Delay (ms)"]
)
plt.xlabel("Routing Protocol")
plt.ylabel("Illustrative Initial Delay (ms)")
plt.title("AODV vs DSDV Initial Communication Delay")
plt.savefig(
    "graphs/initial_delay_comparison.png",
    bbox_inches="tight"
)
plt.show()
plt.close()

# Save summary
with open("results/simulation_summary.txt", "w") as file:
    file.write("AODV VS DSDV SIMULATION SUMMARY\n")
    file.write("--------------------------------\n")
    file.write(f"Source: {source}\n")
    file.write(f"Destination: {destination}\n")
    file.write(f"AODV RREQ transmissions: {rreq}\n")
    file.write(f"AODV RREP transmissions: {rrep}\n")
    file.write(f"Initial AODV route: {aodv_path}\n")
    file.write(f"Alternative route: {new_path}\n")
    file.write("Failed link: C-E\n")
    file.write(f"Illustrative AODV delay: {aodv_delay} ms\n")
    file.write(f"Illustrative DSDV delay: {dsdv_delay} ms\n")

print("\nAODV vs DSDV Comparison")
print(comparison.to_string(index=False))

print("\nNetwork Size Analysis")
print(size_df.to_string(index=False))

print("\nAll files generated successfully.")


# Create downloadable ZIP package
import zipfile
import shutil

package_name = "Q6_Reactive_Routing_Comparison"
os.makedirs(package_name, exist_ok=True)

for folder in ["diagrams", "results", "graphs"]:
    destination = os.path.join(package_name, folder)
    if os.path.exists(destination):
        shutil.rmtree(destination)
    shutil.copytree(folder, destination)

shutil.copy2(
    os.path.abspath(__file__),
    os.path.join(package_name, "aodv_dsdv_comparison.py")
)

zip_name = package_name + ".zip"

with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zip_file:
    for root, dirs, files_list in os.walk(package_name):
        for filename in files_list:
            file_path = os.path.join(root, filename)
            zip_file.write(file_path, file_path)

print(f"\nZIP file created: {zip_name}")

try:
    from google.colab import files
    files.download(zip_name)
except ImportError:
    print("Download the ZIP file from your local working directory.")
