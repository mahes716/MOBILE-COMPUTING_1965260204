
import os
import csv
import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

random.seed(42)
np.random.seed(42)

base = "Q5_Proactive_Routing_DSDV"

for folder in ["diagrams", "results", "graphs"]:
    os.makedirs(f"{base}/{folder}", exist_ok=True)

# Create a sample mobile-node topology
G = nx.Graph()

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "F"),
    ("E", "F")
]

G.add_edges_from(edges)

# Draw initial topology
plt.figure(figsize=(8, 5))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G, pos,
    with_labels=True,
    node_color="lightblue",
    node_size=1800,
    font_size=12,
    edge_color="gray",
    width=2
)

plt.title("DSDV Mobile Node Network Topology")
plt.savefig(f"{base}/diagrams/dsdv_topology_before.png")
plt.show()

# Initialize DSDV routing tables
sequence_numbers = {node: 2 for node in G.nodes()}

def build_routing_tables(graph, seq_numbers):
    routing_tables = {}

    for source in graph.nodes():
        table = {}

        for destination in graph.nodes():

            if source == destination:
                table[destination] = {
                    "next_hop": "-",
                    "hops": 0,
                    "sequence_number": seq_numbers[destination]
                }

            elif nx.has_path(graph, source, destination):
                path = nx.shortest_path(
                    graph, source, destination
                )

                table[destination] = {
                    "next_hop": path[1],
                    "hops": len(path) - 1,
                    "sequence_number": seq_numbers[destination]
                }

            else:
                table[destination] = {
                    "next_hop": "Unavailable",
                    "hops": float("inf"),
                    "sequence_number": seq_numbers[destination] + 1
                }

        routing_tables[source] = table

    return routing_tables


routing_tables_before = build_routing_tables(
    G, sequence_numbers
)

# Display routing table before topology change
print("DSDV ROUTING TABLE BEFORE TOPOLOGY CHANGE")
print("-" * 55)

for destination, details in routing_tables_before["A"].items():
    print(
        f"Destination: {destination} | "
        f"Next Hop: {details['next_hop']} | "
        f"Hops: {details['hops']} | "
        f"Sequence Number: {details['sequence_number']}"
    )

# Save initial routing table
with open(f"{base}/results/routing_table_before.csv",
          "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow([
        "Source", "Destination", "Next Hop",
        "Hop Count", "Sequence Number"
    ])

    for source, table in routing_tables_before.items():
        for destination, details in table.items():
            writer.writerow([
                source,
                destination,
                details["next_hop"],
                details["hops"],
                details["sequence_number"]
            ])

# Simulate a topology change: remove link C-D
print("\nTOPOLOGY CHANGE")
print("Link C-D has failed.")

G.remove_edge("C", "D")

# Increase destination sequence numbers after topology change
for node in sequence_numbers:
    sequence_numbers[node] += 2

routing_tables_after = build_routing_tables(
    G, sequence_numbers
)

# Display updated routing table
print("\nDSDV ROUTING TABLE AFTER TOPOLOGY CHANGE")
print("-" * 55)

for destination, details in routing_tables_after["A"].items():
    print(
        f"Destination: {destination} | "
        f"Next Hop: {details['next_hop']} | "
        f"Hops: {details['hops']} | "
        f"Sequence Number: {details['sequence_number']}"
    )

# Save updated routing table
with open(f"{base}/results/routing_table_after.csv",
          "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow([
        "Source", "Destination", "Next Hop",
        "Hop Count", "Sequence Number"
    ])

    for source, table in routing_tables_after.items():
        for destination, details in table.items():
            writer.writerow([
                source,
                destination,
                details["next_hop"],
                details["hops"],
                details["sequence_number"]
            ])

# Draw updated topology
plt.figure(figsize=(8, 5))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G, pos,
    with_labels=True,
    node_color="lightgreen",
    node_size=1800,
    font_size=12,
    edge_color="gray",
    width=2
)

plt.title("DSDV Topology After Link Failure")
plt.savefig(f"{base}/diagrams/dsdv_topology_after.png")
plt.show()

# Compare routes before and after topology change
route_comparison = []

for destination in G.nodes():
    before = routing_tables_before["A"][destination]
    after = routing_tables_after["A"][destination]

    route_comparison.append([
        "A",
        destination,
        before["next_hop"],
        before["hops"],
        after["next_hop"],
        after["hops"]
    ])

with open(f"{base}/results/route_comparison.csv",
          "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow([
        "Source", "Destination",
        "Before Next Hop", "Before Hops",
        "After Next Hop", "After Hops"
    ])
    writer.writerows(route_comparison)

# Periodic routing update overhead
update_intervals = 5
simulation_duration = 20

node_count = len(G.nodes())
periodic_updates = simulation_duration // update_intervals

updates_per_node = node_count - 1
total_control_updates = (
    periodic_updates * node_count * updates_per_node
)

print("\nPERIODIC ROUTING UPDATE ANALYSIS")
print("Number of Nodes:", node_count)
print("Update Interval:", update_intervals, "seconds")
print("Simulation Duration:", simulation_duration, "seconds")
print("Estimated Routing Update Entries:", total_control_updates)

# Network size comparison
network_sizes = [6, 10, 14]
network_results = []

for size in network_sizes:

    network = nx.random_labeled_tree(size, seed=size)

    # Add extra links to create alternative paths
    extra_links = size // 2

    for _ in range(extra_links):
        u, v = random.sample(list(network.nodes()), 2)

        if not network.has_edge(u, v):
            network.add_edge(u, v)

    routing_entries = size * (size - 1)

    delivery_ratio = (
        len([1 for u in network.nodes()
             for v in network.nodes()
             if u != v and nx.has_path(network, u, v)])
        / routing_entries
    ) * 100

    average_hops = np.mean([
        nx.shortest_path_length(network, u, v)
        for u in network.nodes()
        for v in network.nodes()
        if u != v
    ])

    network_results.append([
        size,
        routing_entries,
        round(delivery_ratio, 2),
        round(average_hops, 2)
    ])

with open(f"{base}/results/network_size_analysis.csv",
          "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow([
        "Number of Nodes",
        "Routing Table Entries",
        "Route Availability (%)",
        "Average Hop Count"
    ])
    writer.writerows(network_results)

# Save summary
with open(f"{base}/results/simulation_summary.txt", "w") as file:

    file.write("DSDV ROUTING SIMULATION\n")
    file.write("-----------------------\n")
    file.write(f"Nodes: {node_count}\n")
    file.write("Failed Link: C-D\n")
    file.write(f"Periodic Update Entries: {total_control_updates}\n")
    file.write(f"Update Interval: {update_intervals} seconds\n")

# Generate network size graph
sizes = [row[0] for row in network_results]
entries = [row[1] for row in network_results]
hops = [row[3] for row in network_results]

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

axes[0].plot(sizes, entries, marker="o")
axes[0].set_title("Network Size vs Routing Table Entries")
axes[0].set_xlabel("Number of Nodes")
axes[0].set_ylabel("Routing Table Entries")
axes[0].grid(True)

axes[1].plot(sizes, hops, marker="o")
axes[1].set_title("Network Size vs Average Hop Count")
axes[1].set_xlabel("Number of Nodes")
axes[1].set_ylabel("Average Hop Count")
axes[1].grid(True)

plt.tight_layout()
plt.savefig(f"{base}/graphs/network_size_analysis.png")
plt.show()

print("\nDSDV simulation completed.")
print("Results saved in:", base)
