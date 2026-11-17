
import os
import csv
import networkx as nx
import matplotlib.pyplot as plt

base = "Q3_Cellular_vs_AdHoc"

for folder in ["diagrams", "results", "graphs"]:
    os.makedirs(f"{base}/{folder}", exist_ok=True)

# Cellular network topology
cellular = nx.Graph()

cellular_nodes = {
    "Mobile 1": (0, 1),
    "Mobile 2": (2, 1),
    "Mobile 3": (4, 1),
    "Base Station": (2, 3),
    "Core Network": (2, 5),
    "Server": (4, 5)
}

cellular.add_edges_from([
    ("Mobile 1", "Base Station"),
    ("Mobile 2", "Base Station"),
    ("Mobile 3", "Base Station"),
    ("Base Station", "Core Network"),
    ("Core Network", "Server")
])

# Ad hoc network topology
adhoc = nx.Graph()

adhoc_nodes = {
    "Node A": (0, 2),
    "Node B": (2, 3),
    "Node C": (4, 2),
    "Node D": (2, 1),
    "Node E": (6, 2)
}

adhoc.add_edges_from([
    ("Node A", "Node B"),
    ("Node B", "Node C"),
    ("Node B", "Node D"),
    ("Node C", "Node E"),
    ("Node D", "Node E")
])

# Draw network architectures
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

nx.draw(
    cellular,
    cellular_nodes,
    with_labels=True,
    node_size=2200,
    node_color="lightblue",
    font_size=8,
    ax=axes[0]
)
axes[0].set_title("Cellular Network Architecture")

nx.draw(
    adhoc,
    adhoc_nodes,
    with_labels=True,
    node_size=2200,
    node_color="lightgreen",
    font_size=9,
    ax=axes[1]
)
axes[1].set_title("Ad Hoc Wireless Network Architecture")

plt.tight_layout()
plt.savefig(f"{base}/diagrams/network_architectures.png")
plt.show()

# Comparison of network characteristics
comparison = [
    ["Infrastructure", "Requires base stations", "No fixed infrastructure"],
    ["Communication", "Through base stations", "Direct or multi-hop between nodes"],
    ["Routing", "Infrastructure-managed", "Distributed routing"],
    ["Mobility", "Movement between cells", "Nodes move independently"],
    ["Topology", "Cell-based structure", "Dynamic and changing topology"],
    ["Scalability", "Supports large coverage areas", "Depends on node density and resources"],
    ["Handoff", "Handoff between base stations", "Routes may change as nodes move"],
    ["Failure Handling", "May be affected by base station failure", "Can use alternate node paths"],
    ["Applications", "Mobile networks and cellular services", "Disaster recovery and temporary networks"]
]

with open(f"{base}/results/network_comparison.csv",
          "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Parameter", "Cellular Network", "Ad Hoc Network"
    ])
    writer.writerows(comparison)

# Connectivity analysis
cellular_connected = nx.is_connected(cellular)
adhoc_connected = nx.is_connected(adhoc)

cellular_path = nx.shortest_path(
    cellular, "Mobile 1", "Server"
)

adhoc_path = nx.shortest_path(
    adhoc, "Node A", "Node E"
)

# Failure analysis
cellular_failure = cellular.copy()
cellular_failure.remove_node("Base Station")

adhoc_failure = adhoc.copy()
adhoc_failure.remove_node("Node B")

cellular_surviving = nx.number_connected_components(
    cellular_failure
)
adhoc_surviving = nx.number_connected_components(
    adhoc_failure
)

print("CELLULAR VS AD HOC NETWORK ANALYSIS")
print("-" * 50)

print("\nCELLULAR NETWORK")
print("Network Connected:", cellular_connected)
print("Mobile 1 to Server Path:", cellular_path)
print("Components after Base Station Failure:", cellular_surviving)

print("\nAD HOC NETWORK")
print("Network Connected:", adhoc_connected)
print("Node A to Node E Path:", adhoc_path)
print("Components after Node B Failure:", adhoc_surviving)

# Save connectivity analysis
with open(f"{base}/results/connectivity_analysis.txt", "w") as file:
    file.write("CELLULAR NETWORK\n")
    file.write(f"Connected: {cellular_connected}\n")
    file.write(f"Mobile 1 to Server Path: {cellular_path}\n")
    file.write(f"Components after Base Station Failure: {cellular_surviving}\n")

    file.write("\nAD HOC NETWORK\n")
    file.write(f"Connected: {adhoc_connected}\n")
    file.write(f"Node A to Node E Path: {adhoc_path}\n")
    file.write(f"Components after Node B Failure: {adhoc_surviving}\n")

# Generate comparison graph
categories = [
    "Infrastructure",
    "Centralized Control",
    "Multi-hop Support",
    "Independent Operation"
]

cellular_scores = [5, 5, 1, 1]
adhoc_scores = [1, 1, 5, 5]

x = range(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(
    [i - width / 2 for i in x],
    cellular_scores,
    width,
    label="Cellular"
)

ax.bar(
    [i + width / 2 for i in x],
    adhoc_scores,
    width,
    label="Ad Hoc"
)

ax.set_ylabel("Illustrative Comparison Score")
ax.set_title("Cellular vs Ad Hoc Network Characteristics")
ax.set_xticks(list(x))
ax.set_xticklabels(categories, rotation=15)
ax.set_ylim(0, 6)
ax.legend()
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig(f"{base}/graphs/network_comparison.png")
plt.show()

print("\nEngineering Decision")
print(
    "For disaster environments without fixed infrastructure, "
    "an ad hoc network is suitable because mobile nodes can "
    "communicate through multi-hop wireless connections."
)

print("\nAnalysis completed. Files saved in:", base)
