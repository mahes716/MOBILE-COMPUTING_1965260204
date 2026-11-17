
import os
import csv
import random
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

random.seed(42)
np.random.seed(42)

base = "Q4_Mobile_IP_Applications"

for folder in ["diagrams", "results", "graphs"]:
    os.makedirs(f"{base}/{folder}", exist_ok=True)

# Emergency communication network architecture
G = nx.DiGraph()

nodes = {
    "Ambulance\n(Mobile Node)": (0, 2),
    "Base Station 1\n(Foreign Network)": (2.5, 3.5),
    "Base Station 2\n(Foreign Network)": (2.5, 0.5),
    "Home Agent": (5.5, 2),
    "Hospital\n(Correspondent Node)": (8.5, 2)
}

G.add_edges_from([
    ("Ambulance\n(Mobile Node)", "Base Station 1\n(Foreign Network)"),
    ("Ambulance\n(Mobile Node)", "Base Station 2\n(Foreign Network)"),
    ("Base Station 1\n(Foreign Network)", "Home Agent"),
    ("Base Station 2\n(Foreign Network)", "Home Agent"),
    ("Home Agent", "Hospital\n(Correspondent Node)")
])

plt.figure(figsize=(12, 6))

nx.draw(
    G,
    nodes,
    with_labels=True,
    node_size=3000,
    node_color="lightblue",
    font_size=8,
    arrows=True,
    arrowsize=20
)

plt.title("Mobile IP Based Emergency Ambulance Communication")
plt.savefig(
    f"{base}/diagrams/ambulance_network.png",
    bbox_inches="tight"
)
plt.show()

# Simulation configuration
total_packets = 100
packet_interval = 1
registration_delay = 2.0

base_delay = 30
packet_loss_probability = 0.03

# Ambulance travels through three network areas
coverage_areas = [
    "Foreign Network 1",
    "Foreign Network 2",
    "Foreign Network 3"
]

care_of_addresses = [
    "10.1.0.1",
    "10.2.0.1",
    "10.3.0.1"
]

current_area = coverage_areas[0]
current_coa = care_of_addresses[0]
registration_until = 0

delivered = 0
lost = 0
delays = []
handoffs = 0

packet_records = []
mobility_records = []

print("EMERGENCY AMBULANCE MOBILE IP SIMULATION")
print("-" * 55)

for packet_id in range(1, total_packets + 1):

    current_time = (packet_id - 1) * packet_interval

    # Ambulance changes network area during its journey
    if packet_id == 35:
        new_area = coverage_areas[1]
        new_coa = care_of_addresses[1]

    elif packet_id == 70:
        new_area = coverage_areas[2]
        new_coa = care_of_addresses[2]

    else:
        new_area = current_area
        new_coa = current_coa

    # Mobile IP registration after changing networks
    if new_area != current_area:

        current_area = new_area
        current_coa = new_coa
        handoffs += 1
        registration_until = current_time + registration_delay

        mobility_records.append([
            current_time,
            current_area,
            current_coa,
            registration_delay
        ])

        print(
            f"Handoff {handoffs}: {current_area}, "
            f"Care-of Address: {current_coa}"
        )

    # Send emergency communication packet
    if current_time < registration_until:
        status = "Registration Interruption"
        delay = None

    else:
        delay = base_delay + random.uniform(5, 15)

        if random.random() < packet_loss_probability:
            status = "Packet Lost"
            lost += 1
        else:
            status = "Delivered"
            delivered += 1
            delays.append(delay)

    if status == "Registration Interruption":
        lost += 1

    packet_records.append([
        packet_id,
        current_time,
        current_area,
        current_coa,
        status,
        round(delay, 2) if delay is not None else ""
    ])

    print(
        f"Packet {packet_id}: {current_area} | "
        f"{status}"
    )

# Calculate performance metrics
pdr = delivered / total_packets * 100
loss_rate = lost / total_packets * 100
average_delay = np.mean(delays) if delays else 0

print("\nPERFORMANCE ANALYSIS")
print("-" * 40)
print("Total Packets:", total_packets)
print("Delivered Packets:", delivered)
print("Lost Packets:", lost)
print("Handoffs:", handoffs)
print("Packet Delivery Ratio:", round(pdr, 2), "%")
print("Packet Loss Rate:", round(loss_rate, 2), "%")
print("Average Delay:", round(average_delay, 2), "ms")

# Save packet records
with open(f"{base}/results/ambulance_packet_results.csv",
          "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow([
        "Packet ID", "Time (s)", "Network Area",
        "Care-of Address", "Status", "Delay (ms)"
    ])
    writer.writerows(packet_records)

# Save mobility and registration events
with open(f"{base}/results/mobility_events.csv",
          "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow([
        "Time (s)", "New Network",
        "Care-of Address", "Registration Delay (s)"
    ])
    writer.writerows(mobility_records)

# Save summary
with open(f"{base}/results/performance_summary.txt", "w") as file:

    file.write("EMERGENCY AMBULANCE COMMUNICATION RESULTS\n")
    file.write("-----------------------------------------\n")
    file.write(f"Total Packets: {total_packets}\n")
    file.write(f"Delivered Packets: {delivered}\n")
    file.write(f"Lost Packets: {lost}\n")
    file.write(f"Handoffs: {handoffs}\n")
    file.write(f"Packet Delivery Ratio: {pdr:.2f}%\n")
    file.write(f"Packet Loss Rate: {loss_rate:.2f}%\n")
    file.write(f"Average Delay: {average_delay:.2f} ms\n")

# Generate performance graphs
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].bar(
    ["Delivered", "Lost"],
    [delivered, lost]
)
axes[0].set_title("Emergency Packet Delivery")
axes[0].set_ylabel("Number of Packets")

axes[1].plot(
    range(1, len(delays) + 1),
    delays,
    marker="."
)
axes[1].set_title("Successful Packet Transmission Delay")
axes[1].set_xlabel("Delivered Packet")
axes[1].set_ylabel("Delay (ms)")
axes[1].grid(True)

plt.tight_layout()
plt.savefig(f"{base}/graphs/ambulance_performance.png")
plt.show()

print("\nSimulation completed.")
print("Results saved in:", base)
