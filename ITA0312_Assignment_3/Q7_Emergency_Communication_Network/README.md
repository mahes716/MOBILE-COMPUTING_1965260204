# Mobile Emergency Communication Network

## Overview

This project demonstrates the design of a mobile emergency communication network for disaster-response situations involving ambulances, police vehicles, rescue teams, and medical personnel.

The proposed network uses mobile wireless communication, Mobile IP concepts, and route discovery to maintain communication when fixed infrastructure is unavailable or network links fail.

## Objectives

- Design a mobile emergency communication architecture.
- Demonstrate communication between mobile nodes.
- Understand Mobile IP registration and tunnelling.
- Demonstrate route discovery and maintenance.
- Analyse link failure and alternative route availability.
- Evaluate delay, packet delivery, and routing overhead.
- Study network performance under different mobility conditions and network sizes.

## Technologies Used

- Python
- NetworkX
- NumPy
- Pandas
- Matplotlib
- Google Colab

## Installation

Install the required libraries:

```bash
pip install networkx matplotlib pandas numpy
```

## Project Structure

```text
Q7_Emergency_Communication_Network/
│
├── emergency_network.py
│
├── diagrams/
│   ├── emergency_network_architecture.png
│   ├── emergency_route.png
│   └── network_after_link_failure.png
│
├── results/
│   ├── mobile_ip_registration.csv
│   ├── packet_delivery_results.csv
│   ├── failure_recovery.csv
│   ├── performance_test_cases.csv
│   └── simulation_summary.txt
│
└── graphs/
    ├── mobility_delay.png
    ├── packet_delivery.png
    └── routing_overhead.png
```

## Proposed Network Architecture

The emergency communication network contains the following components:

- **Mobile Nodes:** Ambulances, police vehicles, rescue teams, and medical personnel.
- **Home Agent (HA):** Maintains the mobile node's home-network association.
- **Foreign Agent (FA):** Represents a visited-network agent in the traditional Mobile IPv4 architecture.
- **Correspondent Node (CN):** Represents the destination communicating with a mobile node.
- **Wireless Links:** Enable communication between mobile devices and network infrastructure.

## Implementation

### 1. Network Architecture

A mobile emergency network is created using NetworkX. The nodes represent emergency-response units and Mobile IP infrastructure. Wireless connections between nodes are displayed in the architecture diagram.

### 2. Mobile IP Registration and Tunnelling

A conceptual Mobile IP registration sequence is generated to demonstrate:

1. Agent discovery.
2. Care-of address acquisition.
3. Registration request.
4. Registration reply.
5. Tunnelling-based packet delivery.

The registration sequence is exported as a CSV file.

### 3. Emergency Route Discovery

A communication route is calculated between the ambulance and command centre. The selected path is highlighted in the network diagram.

### 4. Packet Delivery and Mobility Analysis

The simulation generates 100 packets and records:

- Packet ID
- Source and destination
- Handoff events
- Communication delay
- Packet delivery status

Handoff events introduce additional delay to represent mobility-related communication interruption.

### 5. Link Failure and Recovery

A wireless link is removed to simulate network failure. The program checks whether an alternative communication route is available and records the recovery result.

### 6. Performance Evaluation

The network is tested using different configured node counts:

- 5 nodes
- 10 nodes
- 15 nodes
- 20 nodes
- 25 nodes

Three mobility conditions are considered:

- Low mobility
- Medium mobility
- High mobility

The performance analysis includes:

- Estimated communication delay
- Estimated routing overhead
- Estimated packet delivery ratio

The results are stored in CSV files and represented using graphs.

## Execution

1. Open Google Colab.
2. Upload `emergency_network.py`.
3. Install the required libraries.
4. Execute the Python file.
5. View the generated diagrams, graphs, and result files.
6. The program automatically creates and downloads a ZIP file containing the generated outputs.

## Simulation Scope and Limitations

This is an educational network design and simulation.

- Mobile IP registration and tunnelling are represented through a conceptual sequence, not actual Mobile IP packet exchange.
- Route discovery uses NetworkX shortest-path calculations.
- Link failure and alternative route availability are demonstrated using graph operations.
- Delay, packet delivery, and routing overhead values are simulated or estimated, not measured from real wireless devices.
- The project does not implement a complete AODV or DSDV protocol.

## Conclusion

The project demonstrates a possible mobile emergency communication architecture for disaster-response environments. It illustrates how mobile communication, Mobile IP concepts, route discovery, and failure recovery can support communication between emergency-response teams.

Performance analysis under different network sizes and mobility conditions helps evaluate the expected behaviour of the proposed network and understand the trade-offs involved in designing communication systems for highly dynamic wireless environments.