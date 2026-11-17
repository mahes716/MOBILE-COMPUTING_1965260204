import os
import random
import shutil
import zipfile
import math
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

random.seed(42)

BASE_DIR = "Q7_Emergency_Communication_Network"
for folder in ["diagrams", "results", "graphs"]:
    os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

# Emergency response mobile nodes
nodes = {
    "Ambulance": (0, 0),
    "Police": (1, 1),
    "Rescue_1": (2, 0),
    "Rescue_2": (3, 1),
    "Medical_Team": (4, 0),
    "Command_Center": (5, 1),
    "Mobile_HA": (0, 3),
    "Foreign_Agent_1": (2, 3),
    "Foreign_Agent_2": (4, 3)
}

G = nx.Graph()
for name, position in nodes.items():
    G.add_node(name, pos=position)

edges = [
    ("Ambulance", "Police"),
    ("Ambulance", "Rescue_1"),
    ("Police", "Rescue_1"),
    ("Rescue_1", "Rescue_2"),
    ("Rescue_2", "Medical_Team"),
    ("Medical_Team", "Command_Center"),
    ("Ambulance", "Mobile_HA"),
    ("Rescue_1", "Foreign_Agent_1"),
    ("Rescue_2", "Foreign_Agent_1"),
    ("Medical_Team", "Foreign_Agent_2"),
    ("Command_Center", "Foreign_Agent_2"),
    ("Foreign_Agent_1", "Foreign_Agent_2")
]
G.add_edges_from(edges)

pos = nx.get_node_attributes(G, "pos")

def save_network(graph, filename, title, route=None):
    plt.figure(figsize=(11, 7))
    nx.draw(
        graph, pos, with_labels=True, node_size=1700,
        node_color="lightblue", font_size=8,
        font_weight="bold", edge_color="gray"
    )
    if route and len(route) > 1:
        route_edges = list(zip(route, route[1:]))
        nx.draw_networkx_edges(
            graph, pos, edgelist=route_edges,
            edge_color="red", width=3
        )
    plt.title(title)
    plt.savefig(filename, bbox_inches="tight")
    plt.show()
    plt.close()

save_network(
    G,
    os.path.join(BASE_DIR, "diagrams", "emergency_network_architecture.png"),
    "Mobile Emergency Communication Network"
)

# Mobile IP conceptual registration and tunnelling
registration = pd.DataFrame([
    [1, "Ambulance", "Home Agent", "Agent discovery"],
    [2, "Ambulance", "Foreign Agent 1", "Care-of address acquired"],
    [3, "Foreign Agent 1", "Home Agent", "Registration request"],
    [4, "Home Agent", "Foreign Agent 1", "Registration reply"],
    [5, "Home Agent", "Ambulance", "Tunneled packet delivery"]
], columns=["Step", "From", "To", "Process"])

registration.to_csv(
    os.path.join(BASE_DIR, "results", "mobile_ip_registration.csv"),
    index=False
)

# Route discovery from ambulance to command centre
def discover_route(graph, source, destination):
    if nx.has_path(graph, source, destination):
        return nx.shortest_path(graph, source, destination)
    return None

source = "Ambulance"
destination = "Command_Center"
route = discover_route(G, source, destination)

print("EMERGENCY COMMUNICATION ROUTE")
print("Source:", source)
print("Destination:", destination)
print("Route:", " -> ".join(route) if route else "Unavailable")

save_network(
    G,
    os.path.join(BASE_DIR, "diagrams", "emergency_route.png"),
    "Emergency Message Route",
    route
)

# Simulate packet delivery and mobility interruptions
packet_rows = []
total_packets = 100
base_delay = 35
registration_delay = 120
handoff_packets = {35, 70}

for packet_id in range(1, total_packets + 1):
    is_handoff = packet_id in handoff_packets
    delay = base_delay + random.uniform(5, 20)

    if is_handoff:
        delay += registration_delay

    lost = random.random() < 0.04
    packet_rows.append({
        "Packet_ID": packet_id,
        "Source": source,
        "Destination": destination,
        "Handoff_Event": is_handoff,
        "Delay_ms": round(delay, 2),
        "Delivered": not lost
    })

packet_df = pd.DataFrame(packet_rows)
packet_df.to_csv(
    os.path.join(BASE_DIR, "results", "packet_delivery_results.csv"),
    index=False
)

delivered = int(packet_df["Delivered"].sum())
delivery_ratio = delivered / total_packets * 100
average_delay = packet_df.loc[
    packet_df["Delivered"], "Delay_ms"
].mean()

# Simulate link failure and recovery
failed_graph = G.copy()
failed_graph.remove_edge("Rescue_1", "Rescue_2")
alternate_route = discover_route(failed_graph, source, destination)

failure = pd.DataFrame([{
    "Failed_Link": "Rescue_1 - Rescue_2",
    "Alternative_Route_Available": alternate_route is not None,
    "Alternative_Route": " -> ".join(alternate_route) if alternate_route else "None",
    "Failure_Handling": "Route rediscovery using alternate path"
}])

failure.to_csv(
    os.path.join(BASE_DIR, "results", "failure_recovery.csv"),
    index=False
)

save_network(
    failed_graph,
    os.path.join(BASE_DIR, "diagrams", "network_after_link_failure.png"),
    "Network After Link Failure",
    alternate_route
)

# Performance tests for different node counts and mobility conditions
test_rows = []
for node_count in [5, 10, 15, 20, 25]:
    for mobility in ["Low", "Medium", "High"]:
        mobility_factor = {"Low": 1, "Medium": 1.5, "High": 2.2}[mobility]
        generated = nx.gnp_random_graph(
            node_count, 0.25, seed=node_count
        )
        if not nx.is_connected(generated):
            largest = max(nx.connected_components(generated), key=len)
            generated = generated.subgraph(largest).copy()

        connected_nodes = len(generated.nodes())
        edge_count = generated.number_of_edges()
        estimated_delay = 30 + (mobility_factor * 12) + (node_count * 0.8)
        estimated_overhead = edge_count * mobility_factor
        estimated_delivery = max(
            60, 98 - (mobility_factor * 5) - (node_count * 0.25)
        )

        test_rows.append({
            "Configured_Nodes": node_count,
            "Connected_Nodes": connected_nodes,
            "Mobility": mobility,
            "Estimated_Delay_ms": round(estimated_delay, 2),
            "Estimated_Routing_Overhead_Entries": round(estimated_overhead, 2),
            "Estimated_Packet_Delivery_Percent": round(estimated_delivery, 2)
        })

test_df = pd.DataFrame(test_rows)
test_df.to_csv(
    os.path.join(BASE_DIR, "results", "performance_test_cases.csv"),
    index=False
)

# Performance graphs
mobility_summary = test_df.groupby("Mobility").mean(numeric_only=True).reset_index()

plt.figure(figsize=(8, 5))
for mobility in ["Low", "Medium", "High"]:
    subset = test_df[test_df["Mobility"] == mobility]
    plt.plot(
        subset["Configured_Nodes"],
        subset["Estimated_Delay_ms"],
        marker="o",
        label=mobility
    )
plt.xlabel("Number of Mobile Nodes")
plt.ylabel("Estimated Delay (ms)")
plt.title("Delay Under Different Mobility Conditions")
plt.legend()
plt.grid(True)
plt.savefig(
    os.path.join(BASE_DIR, "graphs", "mobility_delay.png"),
    bbox_inches="tight"
)
plt.show()
plt.close()

plt.figure(figsize=(8, 5))
for mobility in ["Low", "Medium", "High"]:
    subset = test_df[test_df["Mobility"] == mobility]
    plt.plot(
        subset["Configured_Nodes"],
        subset["Estimated_Packet_Delivery_Percent"],
        marker="s",
        label=mobility
    )
plt.xlabel("Number of Mobile Nodes")
plt.ylabel("Estimated Packet Delivery (%)")
plt.title("Packet Delivery Under Different Mobility Conditions")
plt.legend()
plt.grid(True)
plt.savefig(
    os.path.join(BASE_DIR, "graphs", "packet_delivery.png"),
    bbox_inches="tight"
)
plt.show()
plt.close()

plt.figure(figsize=(8, 5))
for mobility in ["Low", "Medium", "High"]:
    subset = test_df[test_df["Mobility"] == mobility]
    plt.plot(
        subset["Configured_Nodes"],
        subset["Estimated_Routing_Overhead_Entries"],
        marker="^",
        label=mobility
    )
plt.xlabel("Number of Mobile Nodes")
plt.ylabel("Estimated Routing Overhead Entries")
plt.title("Routing Overhead Under Different Mobility Conditions")
plt.legend()
plt.grid(True)
plt.savefig(
    os.path.join(BASE_DIR, "graphs", "routing_overhead.png"),
    bbox_inches="tight"
)
plt.show()
plt.close()

# Save simulation summary
with open(os.path.join(BASE_DIR, "results", "simulation_summary.txt"), "w") as file:
    file.write("MOBILE EMERGENCY COMMUNICATION NETWORK SUMMARY\n")
    file.write("------------------------------------------------\n")
    file.write(f"Total packets: {total_packets}\n")
    file.write(f"Packets delivered: {delivered}\n")
    file.write(f"Packet delivery ratio: {delivery_ratio:.2f}%\n")
    file.write(f"Average delay of delivered packets: {average_delay:.2f} ms\n")
    file.write(f"Initial route: {route}\n")
    file.write(f"Alternative route after link failure: {alternate_route}\n")
    file.write("Mobile IP registration and tunnelling: conceptual sequence recorded\n")

print("\nPERFORMANCE SUMMARY")
print("Total packets:", total_packets)
print("Delivered packets:", delivered)
print(f"Packet delivery ratio: {delivery_ratio:.2f}%")
print(f"Average delay: {average_delay:.2f} ms")
print("\nFailure recovery route:", alternate_route)
print("\nPerformance test cases:")
print(test_df.to_string(index=False))

# Create ZIP containing all generated outputs and this script
script_path = os.path.abspath(__file__)
shutil.copy2(script_path, os.path.join(BASE_DIR, "emergency_network.py"))

zip_name = BASE_DIR + ".zip"
with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zip_file:
    for root, dirs, files_list in os.walk(BASE_DIR):
        for filename in files_list:
            file_path = os.path.join(root, filename)
            zip_file.write(file_path, file_path)

print(f"\nZIP file created: {zip_name}")

try:
    from google.colab import files
    files.download(zip_name)
except ImportError:
    print("ZIP created in the current working directory.")
