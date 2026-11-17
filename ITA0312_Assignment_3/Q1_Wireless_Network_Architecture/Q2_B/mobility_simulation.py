
import os
import csv
import random
import shutil
import numpy as np
import matplotlib.pyplot as plt

random.seed(42)
np.random.seed(42)

folder = "Q1_Wireless_Network_Architecture"
os.makedirs(folder + "/results", exist_ok=True)
os.makedirs(folder + "/graphs", exist_ok=True)
os.makedirs(folder + "/screenshots", exist_ok=True)

# Wireless access point locations
ap1_position = 0
ap2_position = 100
coverage_radius = 65

# Simulation settings
packet_interval = 0.5
handoff_duration = 1.5
simulation_speeds = [1, 3, 6]

all_results = []
all_packet_records = []
all_handoff_records = []

print("WIRELESS MOBILITY SIMULATION")
print("-" * 50)

for speed in simulation_speeds:

    position = 0
    current_ap = "AP1"
    time = 0
    handoff_until = -1

    total_packets = 0
    delivered_packets = 0
    lost_packets = 0
    delays = []
    handoffs = 0

    print(f"\nMobility Speed: {speed} m/s")
    print("-" * 35)

    while position < 100:

        position = min(position + speed * packet_interval, 100)

        distance_ap1 = abs(position - ap1_position)
        distance_ap2 = abs(position - ap2_position)

        # Select the nearest access point
        best_ap = "AP1" if distance_ap1 <= distance_ap2 else "AP2"

        # Check whether the mobile node is within coverage
        in_coverage = min(distance_ap1, distance_ap2) <= coverage_radius

        # Initiate handoff when the best access point changes
        if best_ap != current_ap:
            current_ap = best_ap
            handoffs += 1
            handoff_until = time + handoff_duration

            event = [
                speed,
                round(time, 2),
                round(position, 2),
                current_ap
            ]

            all_handoff_records.append(event)

            print(
                f"Handoff {handoffs}: Connected to {current_ap} "
                f"at {time:.2f} seconds"
            )

        total_packets += 1

        # Determine packet transmission status
        if not in_coverage:
            status = "No Coverage"
            delay = None

        elif time < handoff_until:
            status = "Handoff Interruption"
            delay = None

        else:
            packet_loss_probability = 0.03 + (speed * 0.005)

            delay = random.uniform(10, 20) + (speed * 1.5)

            if random.random() < packet_loss_probability:
                status = "Wireless Packet Loss"
                delay = None
            else:
                status = "Delivered"
                delivered_packets += 1
                delays.append(delay)

        if status != "Delivered":
            lost_packets += 1

        all_packet_records.append([
            speed,
            round(time, 2),
            round(position, 2),
            current_ap,
            status,
            round(delay, 2) if delay is not None else ""
        ])

        time += packet_interval

    pdr = delivered_packets / total_packets * 100
    loss_rate = lost_packets / total_packets * 100
    average_delay = np.mean(delays) if delays else 0

    all_results.append([
        speed,
        total_packets,
        delivered_packets,
        lost_packets,
        handoffs,
        round(pdr, 2),
        round(loss_rate, 2),
        round(average_delay, 2),
        round(time, 2)
    ])

    print("Total Packets:", total_packets)
    print("Delivered Packets:", delivered_packets)
    print("Lost Packets:", lost_packets)
    print("Handoffs:", handoffs)
    print("Packet Delivery Ratio:", round(pdr, 2), "%")
    print("Packet Loss Rate:", round(loss_rate, 2), "%")
    print("Average Delay:", round(average_delay, 2), "ms")
    print("Scenario Completed at:", round(time, 2), "seconds")

# Save packet-level records
with open(folder + "/results/mobility_packet_results.csv",
          "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow([
        "Speed (m/s)", "Time (s)", "Position (m)",
        "Connected AP", "Packet Status", "Delay (ms)"
    ])
    writer.writerows(all_packet_records)

# Save handoff events
with open(folder + "/results/handoff_events.csv",
          "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow([
        "Speed (m/s)", "Handoff Time (s)",
        "Position (m)", "New Access Point"
    ])
    writer.writerows(all_handoff_records)

# Save scenario comparison
with open(folder + "/results/mobility_summary.csv",
          "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow([
        "Speed (m/s)", "Total Packets", "Delivered",
        "Lost", "Handoffs", "PDR (%)",
        "Loss Rate (%)", "Average Delay (ms)",
        "Completion Time (s)"
    ])
    writer.writerows(all_results)

# Display comparison
print("\nMOBILITY SCENARIO COMPARISON")
print("-" * 50)

for result in all_results:
    print(
        f"Speed: {result[0]} m/s | "
        f"PDR: {result[5]}% | "
        f"Loss: {result[6]}% | "
        f"Delay: {result[7]} ms | "
        f"Handoffs: {result[4]}"
    )

# Generate performance graphs
speeds = [r[0] for r in all_results]
pdr_values = [r[5] for r in all_results]
delay_values = [r[7] for r in all_results]
loss_values = [r[6] for r in all_results]

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].plot(speeds, pdr_values, marker="o")
axes[0].set_title("Packet Delivery Ratio vs Speed")
axes[0].set_xlabel("Mobility Speed (m/s)")
axes[0].set_ylabel("PDR (%)")
axes[0].grid(True)

axes[1].plot(speeds, delay_values, marker="o")
axes[1].set_title("Average Delay vs Speed")
axes[1].set_xlabel("Mobility Speed (m/s)")
axes[1].set_ylabel("Delay (ms)")
axes[1].grid(True)

axes[2].plot(speeds, loss_values, marker="o")
axes[2].set_title("Packet Loss Rate vs Speed")
axes[2].set_xlabel("Mobility Speed (m/s)")
axes[2].set_ylabel("Packet Loss (%)")
axes[2].grid(True)

plt.tight_layout()
plt.savefig(folder + "/graphs/mobility_performance.png")
plt.show()

# Save this script in the assignment folder
shutil.copy2(
    "mobility_simulation.py",
    folder + "/mobility_simulation.py"
)

print("\nMobility simulation completed.")
print("Results and graphs saved in:", folder)
