# Proactive Routing Protocols – DSDV Simulation

## Overview

This project demonstrates the working principles of proactive routing using Destination-Sequenced Distance Vector (DSDV). It explores routing-table maintenance, topology changes, route availability, and routing update overhead in a mobile ad hoc network (MANET).

## Objectives

- Understand proactive routing protocols.
- Study DSDV routing-table structure.
- Observe route changes after a link failure.
- Understand the role of destination sequence numbers.
- Estimate routing update overhead.
- Analyse network performance at different network sizes.

## Technologies Used

- Python
- NetworkX
- NumPy
- Pandas
- Matplotlib
- Google Colab

## Installation

Run the following command in Google Colab or a Python environment:

```bash
pip install networkx matplotlib pandas numpy
```

## Project Structure

```text
Q5_Proactive_Routing_DSDV/
│
├── dsdv_simulation.py
├── README.md
│
├── diagrams/
│   ├── dsdv_topology_before.png
│   └── dsdv_topology_after.png
│
├── results/
│   ├── routing_table_before.csv
│   ├── routing_table_after.csv
│   ├── route_comparison.csv
│   ├── network_size_analysis.csv
│   └── simulation_summary.txt
│
└── graphs/
    └── network_size_analysis.png
```

## Implementation

### 1. Network Topology

A sample network containing six nodes (A–F) is created using NetworkX. The initial topology and connections between nodes are visualised.

### 2. Routing Table Generation

Routing information is generated for each node, including:

- Destination node
- Next-hop node
- Number of hops
- Destination sequence number
- Route availability

The initial routing tables are exported as CSV files.

### 3. Topology Change Analysis

A link between two nodes is removed to represent a network topology change. The routing information is recalculated, and the updated topology and routing tables are generated.

### 4. Routing Update Overhead

The project estimates the number of routing update entries using:

- Number of network nodes
- Routing update interval
- Simulation duration
- Number of destinations per node

For the configured example:

- Number of nodes: 6
- Update interval: 5 seconds
- Simulation duration: 20 seconds
- Estimated routing update entries: 120

This value is a simplified estimate based on periodic update rounds and destination entries, not a count of actual transmitted DSDV control packets.

### 5. Network Size Analysis

Different network sizes are generated and analysed to observe how network size affects routing-related metrics. The results are saved in CSV format and visualised using Matplotlib.

## Outputs

The program generates:

- Initial and updated network topology diagrams
- Routing tables before and after topology changes
- Route comparison results
- Network size analysis
- Routing update overhead summary
- Performance graphs

## Execution

1. Open Google Colab.
2. Upload `dsdv_simulation.py`.
3. Install the required libraries.
4. Execute the Python script.
5. Allow the program to generate the diagrams, graphs, and result files.
6. Download the generated output folders.

## Note on Simulation Scope

This is an educational, DSDV-inspired routing analysis. It uses shortest-path calculations and simplified sequence-number updates to demonstrate routing changes. It does not implement the complete DSDV protocol, actual periodic routing advertisements, or real wireless packet transmission. The routing update overhead is an estimate rather than measured network traffic.

## Conclusion

The project demonstrates the fundamental concepts of proactive routing through routing-table generation, topology changes, route recalculation, and routing update overhead estimation. It illustrates how maintaining routing information can help nodes identify available routes when network topology changes.