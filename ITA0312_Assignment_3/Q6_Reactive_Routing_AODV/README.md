# Reactive Routing and Protocol Comparison – AODV vs DSDV

## Overview

This project demonstrates reactive routing using Ad hoc On-Demand Distance Vector (AODV) and compares it with Destination-Sequenced Distance Vector (DSDV), a proactive routing protocol.

The simulation explores route discovery, route maintenance, link failures, routing overhead, initial communication delay, and network size.

## Objectives

- Understand reactive routing protocols.
- Study AODV route discovery using RREQ and RREP.
- Understand route error handling using RERR.
- Analyse route maintenance after link failure.
- Compare AODV and DSDV routing mechanisms.
- Evaluate routing overhead and initial communication delay.
- Study routing behaviour across different network sizes.

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
Q6_Reactive_Routing_Comparison/
│
├── aodv_dsdv_comparison.py
├── README.md
│
├── diagrams/
│   ├── initial_topology.png
│   ├── aodv_route.png
│   └── topology_after_failure.png
│
├── results/
│   ├── dsdv_routing_table.csv
│   ├── aodv_dsdv_comparison.csv
│   ├── network_size_comparison.csv
│   └── simulation_summary.txt
│
└── graphs/
    ├── routing_overhead_comparison.png
    └── initial_delay_comparison.png
```

## Implementation

### 1. MANET Topology Creation

A sample Mobile Ad Hoc Network (MANET) is created using NetworkX. Nodes represent mobile devices, and edges represent wireless communication links.

### 2. AODV Route Discovery

The simulation demonstrates on-demand route discovery between a source node and destination node.

- RREQ (Route Request): Initiates route discovery.
- RREP (Route Reply): Represents the response along the discovered route.
- The discovered route is displayed in the network topology.

### 3. Route Maintenance

A communication link is removed to simulate a link failure.

The simulation demonstrates the generation of a conceptual RERR (Route Error) and searches for an alternative route between the source and destination.

### 4. DSDV Routing Table

A DSDV-inspired routing table is generated using shortest-path calculations. It contains destination nodes, next-hop information, hop counts, and route availability.

### 5. AODV and DSDV Comparison

The protocols are compared using the following characteristics:

| Parameter | AODV | DSDV |
|---|---|---|
| Routing type | Reactive | Proactive |
| Route discovery | On demand | Routes maintained in advance |
| Routing table | Routes maintained when needed | Continuously maintained |
| Initial communication delay | Route discovery may introduce delay | Routes may already be available |
| Control overhead | Mainly during discovery and maintenance | Periodic routing updates |
| Mobility handling | Route rediscovery after failure | Routing updates after topology changes |

### 6. Network Size Analysis

Different network sizes are generated to estimate routing overhead for both protocols. The results are stored in CSV format and visualised using graphs.

## Execution

1. Open Google Colab.
2. Upload `aodv_dsdv_comparison.py`.
3. Install the required libraries.
4. Execute the Python file.
5. View the generated topology diagrams, graphs, and result files.
6. The program automatically creates and downloads a ZIP file containing the generated outputs.

## Simulation Scope and Limitations

This is an educational comparison model, not a complete implementation of AODV or DSDV.

- RREQ and RREP counts are derived from a simplified graph traversal.
- RERR is represented conceptually when a link fails.
- DSDV routes are calculated using shortest-path algorithms rather than actual DSDV routing advertisements.
- Routing overhead values are estimates, not measured wireless control traffic.
- Communication delay values are illustrative and are not obtained from real packet transmission.

## Conclusion

The project demonstrates the fundamental differences between reactive and proactive routing protocols. AODV discovers routes when communication is required, whereas DSDV maintains routing information continuously. The comparison helps understand their suitability for mobile networks with different levels of topology changes and communication requirements.