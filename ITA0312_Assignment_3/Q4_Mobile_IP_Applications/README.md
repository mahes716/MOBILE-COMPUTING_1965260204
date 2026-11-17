# Q4 – Applications of Mobile IP and Routing Requirements

## 1. Aim

To study real-world applications of Mobile IP and understand the routing requirements created by mobility. An emergency ambulance communication system is selected to demonstrate how Mobile IP supports communication while a mobile node moves between different network coverage areas.

## 2. Application Scenario – Emergency Ambulance Communication

An ambulance travels between different network coverage areas while maintaining communication with a hospital.

The system allows the ambulance to transmit emergency information, patient details and status updates to the hospital during its journey.

Mobile IP supports communication by allowing the ambulance to maintain its home address while updating its current network location.

## 3. Network Components

- **Ambulance (Mobile Node):** Mobile device responsible for sending emergency information.
- **Foreign Networks:** Networks through which the ambulance obtains connectivity.
- **Foreign Agent:** Supports mobility in the visited network in the traditional Mobile IPv4 architecture.
- **Home Agent:** Maintains the ambulance's current Care-of Address and forwards packets.
- **Hospital (Correspondent Node):** Receives emergency information and communicates with the ambulance.

## 4. Network Architecture

The proposed architecture consists of an ambulance, multiple foreign networks, a Home Agent and a hospital.

### Communication Flow

1. The ambulance initially connects to Foreign Network 1.
2. It sends emergency information to the hospital.
3. When the ambulance enters another network, it obtains a new Care-of Address.
4. The Home Agent updates the ambulance's current location through registration.
5. Packets are forwarded through the Home Agent to the ambulance's current network.
6. The ambulance continues communicating with the hospital.

## 5. Implementation

The simulation is implemented using Python in Google Colab.

The program demonstrates:

- Emergency ambulance network architecture.
- Mobile IP-based communication flow.
- Movement across three foreign network areas.
- Care-of Address changes.
- Registration delay during network transitions.
- Packet delivery and packet loss.
- Handoff events.
- Communication delay analysis.

## 6. Simulation Parameters

| Parameter | Value |
|---|---:|
| Total packets | 100 |
| Packet transmission interval | 1 second |
| Registration delay | 2 seconds |
| Base communication delay | 30 ms |
| Packet loss probability | 3% |
| Network areas | 3 |
| Network transitions | 2 |

These are assumed parameters used for the educational simulation.

## 7. Performance Analysis

The program evaluates the following metrics:

- **Packet Delivery Ratio:** Percentage of successfully delivered packets.
- **Packet Loss Rate:** Percentage of packets lost during transmission or registration interruption.
- **Average Delay:** Average delay of successfully delivered packets.
- **Handoffs:** Number of network transitions experienced by the ambulance.
- **Registration Interruption:** Communication interruption while updating the mobile node's network location.

## 8. Routing Requirements

| Requirement | Purpose |
|---|---|
| Continuous connectivity | Maintain ambulance-hospital communication |
| Low delay | Support time-sensitive emergency messages |
| Reliable delivery | Reduce loss of emergency information |
| Mobility support | Maintain communication across networks |
| Security | Protect patient and emergency information |
| Handoff support | Reduce interruption during network transitions |

## 9. Security and Reliability

The emergency communication system should provide:

- Authentication of mobile nodes.
- Secure registration and mobility updates.
- Protection of patient information.
- Reliable packet forwarding.
- Efficient handoff management.
- Recovery from temporary connectivity interruptions.

## 10. Results

The program generates:

- Ambulance network architecture diagram.
- Packet-level simulation results.
- Mobility and registration event records.
- Performance summary.
- Packet delivery and transmission delay graphs.

## 11. Folder Structure

```text
Q4_Mobile_IP_Applications/
│
├── ambulance_network.py
├── README.md
│
├── diagrams/
│   └── ambulance_network.png
│
├── results/
│   ├── ambulance_packet_results.csv
│   ├── mobility_events.csv
│   └── performance_summary.txt
│
└── graphs/
    └── ambulance_performance.png
```

## 12. Execution

Install the required libraries:

```bash
pip install numpy matplotlib networkx
```

Run the program:

```bash
python ambulance_network.py
```

The program can also be executed using Google Colab.

## 13. Conclusion

The emergency ambulance communication scenario demonstrates how Mobile IP can support communication while a mobile node moves between different network areas. The simulation analyses Care-of Address changes, registration interruptions, packet delivery and communication delay. It highlights the importance of reliable routing, security, low latency and efficient mobility management in emergency communication systems.

**Note:** This is an educational simulation using predefined network transitions and assumed parameters. It does not implement a complete Mobile IP protocol or a real emergency communication network.