# Q2 – Mobile IP and Mobility Management

## 1. Aim

To study Mobile IP architecture and mobility management, understand how mobile nodes communicate across different networks, and simulate packet delivery, registration, tunnelling, and mobility-related challenges.

## 2. Mobile IP Architecture

Mobile IP allows a mobile device to move from its home network to a foreign network while maintaining communication.

The architecture consists of four major entities:

- **Mobile Node (MN):** A device that moves between different networks.
- **Home Agent (HA):** Maintains the current location information of the Mobile Node and forwards packets to its current network.
- **Foreign Agent (FA):** Assists the Mobile Node in the visited network and supports packet forwarding.
- **Correspondent Node (CN):** The device or system communicating with the Mobile Node.

## 3. Working Process

The Mobile IP communication process follows these steps:

1. The Mobile Node enters a foreign network.
2. Agent discovery identifies the available mobility agent.
3. The Mobile Node obtains a Care-of Address.
4. The Mobile Node sends a registration request.
5. The Home Agent updates the Mobile Node's location information.
6. The Correspondent Node sends packets towards the Home Agent.
7. The Home Agent encapsulates packets and tunnels them to the Foreign Agent.
8. The Foreign Agent forwards packets to the Mobile Node.

## 4. Implementation

The simulation is implemented using Python in Google Colab.

The program demonstrates:

- Mobile IP architecture representation.
- Agent discovery and registration sequence.
- Packet delivery through tunnelling.
- Encapsulation overhead.
- Packet delivery ratio and packet loss.
- Registration delay under repeated network changes.
- Triangular routing and route optimization comparison.

## 5. Simulation Parameters

| Parameter | Value |
|---|---:|
| Total packets | 50 |
| Original packet size | 1000 bytes |
| Tunnelling overhead | 20 bytes |
| Home Agent delay | 20 ms |
| Foreign Agent delay | 15 ms |
| Registration delay per network change | 100 ms |
| Packet loss probability | 4% |

These are assumed simulation parameters used to demonstrate Mobile IP concepts.

## 6. Performance Analysis

The simulation evaluates the following metrics:

- **Packet Delivery Ratio (PDR):** Percentage of packets successfully delivered.
- **Packet Loss Rate:** Percentage of packets lost during transmission.
- **Average Packet Delay:** Average delay of successfully delivered packets.
- **Tunnelling Overhead:** Additional bytes introduced through encapsulation.
- **Registration Delay:** Time required for registration during network changes.
- **Routing Delay:** Illustrative comparison between triangular routing and route optimization.

## 7. Challenges in Mobile IP

### Registration Delay
Frequent network changes require repeated registration, which can increase communication delay.

### Tunnelling Overhead
Encapsulation adds additional headers to packets, increasing transmission overhead.

### Triangular Routing
Packets may travel through the Home Agent before reaching the Mobile Node, creating a potentially longer route.

### Packet Loss During Mobility
Packets may be lost during handoff or while the Mobile Node is registering with a new network.

### Security
Registration messages and mobility updates require authentication and protection against unauthorized changes.

### Scalability
A large number of mobile nodes can increase the processing and registration load on mobility agents.

## 8. Possible Improvements

- Use route optimization to reduce unnecessary routing through the Home Agent.
- Reduce registration delay through efficient mobility management.
- Use secure authentication for registration messages.
- Minimize unnecessary tunnelling overhead.
- Use efficient handoff mechanisms to reduce packet loss during movement.

## 9. Results

The program generates:

- Mobile IP architecture diagram.
- Registration sequence CSV file.
- Packet delivery results.
- Mobility analysis results.
- Routing comparison results.
- Simulation summary.
- Performance graphs.

## 10. Folder Structure

```text
Q2_Mobile_IP/
│
├── mobile_ip_simulation.py
├── README.md
│
├── diagrams/
│   └── mobile_ip_architecture.png
│
├── results/
│   ├── registration_sequence.csv
│   ├── packet_delivery.csv
│   ├── mobility_analysis.csv
│   ├── routing_comparison.csv
│   └── simulation_summary.txt
│
└── graphs/
    └── mobile_ip_performance.png
```

## 11. Execution

Install the required libraries:

```bash
pip install numpy matplotlib
```

Run the simulation:

```bash
python mobile_ip_simulation.py
```

The simulation can also be executed using Google Colab.

## 12. Conclusion

The Mobile IP simulation demonstrates how a mobile node maintains communication when moving between networks. It illustrates registration, packet forwarding, tunnelling