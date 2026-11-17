
import os
import csv
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

random.seed(42)
np.random.seed(42)

base = "Q2_Mobile_IP"

for folder in ["diagrams", "results", "graphs"]:
    os.makedirs(f"{base}/{folder}", exist_ok=True)

# Mobile IP entities
mobile_node = "Mobile Node"
home_agent = "Home Agent"
foreign_agent = "Foreign Agent"
correspondent_node = "Correspondent Node"

# Network parameters
total_packets = 50
registration_delay = 100
home_agent_delay = 20
foreign_agent_delay = 15
tunnel_overhead = 20
original_packet_size = 1000
packet_loss_probability = 0.04

# Create Mobile IP architecture diagram
fig, ax = plt.subplots(figsize=(12, 5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 5)
ax.axis("off")

entities = [
    (0.5, 2, "Correspondent\nNode"),
    (3.5, 2, "Home Agent"),
    (7.0, 2, "Foreign Agent"),
    (9.8, 2, "Mobile Node")
]

for x, y, label in entities:
    box = FancyBboxPatch(
        (x, y), 1.7, 1,
        boxstyle="round,pad=0.15",
        edgecolor="black",
        facecolor="lightblue"
    )
    ax.add_patch(box)
    ax.text(x + 0.85, y + 0.5, label,
            ha="center", va="center", fontsize=10)

# Packet path arrows
arrows = [
    ((2.2, 2.5), (3.5, 2.5)),
    ((5.2, 2.5), (7.0, 2.5)),
    ((8.7, 2.5), (9.8, 2.5))
]

for start, end in arrows:
    ax.annotate(
        "", xy=end, xytext=start,
        arrowprops=dict(arrowstyle="->", linewidth=2)
    )

ax.text(2.8, 3.2, "Packet", ha="center")
ax.text(6.1, 3.2, "Tunnelling", ha="center")
ax.text(9.2, 3.2, "Decapsulation", ha="center")

ax.text(6, 0.8,
        "Home Agent maintains the Mobile Node's current care-of address",
        ha="center", fontsize=10)

ax.set_title("Mobile IP Architecture and Packet Delivery")
plt.savefig(f"{base}/diagrams/mobile_ip_architecture.png",
            bbox_inches="tight")
plt.show()

# Registration simulation
registration_events = [
    ["1", "Mobile Node", "Agent Discovery"],
    ["2", "Foreign Agent", "Advertisement / Care-of Address"],
    ["3", "Mobile Node", "Registration Request"],
    ["4", "Home Agent", "Binding Update"],
    ["5", "Home Agent", "Registration Reply"],
    ["6", "Foreign Agent", "Registration Confirmation"]
]

with open(f"{base}/results/registration_sequence.csv",
          "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Step", "Entity", "Action"])
    writer.writerows(registration_events)

# Packet delivery through Mobile IP tunnelling
packet_results = []
delivered = 0
lost = 0
total_tunnel_bytes = 0
delays = []

for packet_id in range(1, total_packets + 1):

    # Correspondent Node -> Home Agent -> Foreign Agent -> Mobile Node
    delay = (
        home_agent_delay
        + foreign_agent_delay
        + random.uniform(5, 15)
    )

    packet_size = original_packet_size + tunnel_overhead
    total_tunnel_bytes += packet_size

    if random.random() < packet_loss_probability:
        status = "Lost"
        lost += 1
    else:
        status = "Delivered"
        delivered += 1
        delays.append(delay)

    packet_results.append([
        packet_id,
        original_packet_size,
        tunnel_overhead,
        packet_size,
        round(delay, 2),
        status
    ])

with open(f"{base}/results/packet_delivery.csv",
          "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Packet ID", "Original Size (Bytes)",
        "Tunnel Overhead (Bytes)", "Total Size (Bytes)",
        "Delay (ms)", "Status"
    ])
    writer.writerows(packet_results)

# Frequent mobility registration challenge
mobility_changes = [1, 3, 5, 8, 10]
mobility_results = []

for changes in mobility_changes:

    total_registration_time = changes * registration_delay
    mobility_loss = min(0.02 + changes * 0.015, 0.8)

    successful_packets = 0
    lost_packets = 0

    for _ in range(total_packets):
        if random.random() < mobility_loss:
            lost_packets += 1
        else:
            successful_packets += 1

    mobility_results.append([
        changes,
        total_registration_time,
        successful_packets,
        lost_packets,
        round(successful_packets / total_packets * 100, 2)
    ])

with open(f"{base}/results/mobility_analysis.csv",
          "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Network Changes",
        "Total Registration Delay (ms)",
        "Delivered Packets",
        "Lost Packets",
        "Packet Delivery Ratio (%)"
    ])
    writer.writerows(mobility_results)

# Triangular routing comparison
triangular_delay = 80
optimized_delay = 45

routing_comparison = [
    ["Triangular Routing", triangular_delay],
    ["Route Optimization", optimized_delay]
]

with open(f"{base}/results/routing_comparison.csv",
          "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Routing Method", "Illustrative Delay (ms)"])
    writer.writerows(routing_comparison)

# Calculate metrics
pdr = delivered / total_packets * 100
loss_rate = lost / total_packets * 100
average_delay = np.mean(delays) if delays else 0
average_packet_size = total_tunnel_bytes / total_packets

print("MOBILE IP SIMULATION")
print("-" * 45)
print("Total Packets:", total_packets)
print("Delivered Packets:", delivered)
print("Lost Packets:", lost)
print("Packet Delivery Ratio:", round(pdr, 2), "%")
print("Packet Loss Rate:", round(loss_rate, 2), "%")
print("Average Packet Delay:", round(average_delay, 2), "ms")
print("Original Packet Size:", original_packet_size, "bytes")
print("Encapsulation Overhead:", tunnel_overhead, "bytes")
print("Total Encapsulated Packet Size:", original_packet_size + tunnel_overhead, "bytes")
print("Average Packet Size:", round(average_packet_size, 2), "bytes")

print("\nFREQUENT MOBILITY ANALYSIS")
for row in mobility_results:
    print(
        f"Network Changes: {row[0]} | "
        f"Registration Delay: {row[1]} ms | "
        f"PDR: {row[4]}%"
    )

print("\nROUTING COMPARISON")
print("Triangular Routing Delay:", triangular_delay, "ms")
print("Optimized Routing Delay:", optimized_delay, "ms")

# Save summary
with open(f"{base}/results/simulation_summary.txt", "w") as file:
    file.write("MOBILE IP SIMULATION RESULTS\n")
    file.write("----------------------------\n")
    file.write(f"Total Packets: {total_packets}\n")
    file.write(f"Delivered Packets: {delivered}\n")
    file.write(f"Lost Packets: {lost}\n")
    file.write(f"Packet Delivery Ratio: {pdr:.2f}%\n")
    file.write(f"Packet Loss Rate: {loss_rate:.2f}%\n")
    file.write(f"Average Delay: {average_delay:.2f} ms\n")
    file.write(f"Tunnel Overhead: {tunnel_overhead} bytes\n")

# Generate graphs
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].bar(
    ["Delivered", "Lost"],
    [delivered, lost]
)
axes[0].set_title("Mobile IP Packet Delivery")
axes[0].set_ylabel("Packets")

axes[1].plot(
    [r[0] for r in mobility_results],
    [r[4] for r in mobility_results],
    marker="o"
)
axes[1].set_title("Mobility Changes vs PDR")
axes[1].set_xlabel("Network Changes")
axes[1].set_ylabel("PDR (%)")
axes[1].grid(True)

axes[2].bar(
    [r[0] for r in routing_comparison],
    [r[1] for r in routing_comparison]
)
axes[2].set_title("Routing Delay Comparison")
axes[2].set_ylabel("Illustrative Delay (ms)")
axes[2].tick_params(axis="x", rotation=15)

plt.tight_layout()
plt.savefig(f"{base}/graphs/mobile_ip_performance.png")
plt.show()

print("\nMobile IP simulation completed.")
print("Generated files are saved in:", base)
