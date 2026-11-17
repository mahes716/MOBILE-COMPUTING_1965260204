# Q3 – Cellular Networks versus Ad Hoc Wireless Networks

## 1. Aim

To study cellular and ad hoc wireless network architectures, understand their communication mechanisms, and compare their infrastructure, routing, mobility, topology, scalability, handoff and failure-handling characteristics.

## 2. Cellular Network Architecture

A cellular network is an infrastructure-based wireless network that uses base stations to provide communication services to mobile devices.

### Major Components

- **Mobile Nodes:** Devices such as smartphones and laptops.
- **Base Station:** Provides wireless connectivity to mobile devices.
- **Core Network:** Manages communication and connects different network services.
- **Server:** Provides network resources and services.

### Communication Process

1. A mobile device connects to a nearby base station.
2. The base station forwards communication to the core network.
3. The core network routes the data towards the destination.
4. The server processes the request and returns the response.

## 3. Ad Hoc Wireless Network Architecture

An ad hoc wireless network is an infrastructure-less network in which mobile nodes communicate directly or through other nodes.

### Major Characteristics

- Does not require fixed base stations.
- Nodes can communicate directly when within wireless range.
- Supports multi-hop communication.
- Network topology changes as nodes move.
- Routing is distributed among participating nodes.

### Communication Process

1. Mobile nodes discover neighbouring nodes.
2. A source node identifies a route to the destination.
3. Data is forwarded through intermediate nodes when required.
4. The destination receives the transmitted data.

## 4. Technical Comparison

| Parameter | Cellular Network | Ad Hoc Network |
|---|---|---|
| Infrastructure | Requires base stations | No fixed infrastructure |
| Communication | Through base stations | Direct or multi-hop |
| Routing | Infrastructure-managed | Distributed |
| Mobility | Handoff between cells | Dynamic topology |
| Topology | Cell-based | Dynamic |
| Scalability | Supports large coverage areas | Depends on node density and resources |
| Handoff | Between base stations | Routes may change as nodes move |
| Failure Handling | Base station failure can disrupt service | Alternative paths may be available |
| Applications | Mobile communication services | Disaster recovery and temporary networks |

## 5. Implementation

The comparison is implemented using Python in Google Colab.

The program uses:

- **NetworkX:** To create and analyse network topologies.
- **Matplotlib:** To draw network architectures and generate comparison graphs.

Two network architectures are created:

1. Cellular network containing mobile nodes, a base station, core network and server.
2. Ad hoc network containing interconnected mobile nodes without a central base station.

## 6. Connectivity Analysis

The program evaluates:

- Whether the cellular network is connected.
- The communication path from a mobile node to the server.
- Whether the ad hoc network is connected.
- The communication path between two ad hoc nodes.
- Connectivity changes after removing a base station or an intermediate node.

## 7. Performance Comparison

The program generates an illustrative comparison graph using scores from 1 to 5.

The comparison considers:

- Infrastructure requirements.
- Centralized control.
- Multi-hop support.
- Independent operation.

These scores represent qualitative differences and are not measured network-performance values.

## 8. Engineering Decision

For an emergency or disaster environment where fixed infrastructure may be unavailable, an ad hoc wireless network is generally suitable.

Mobile nodes can communicate directly or forward data through intermediate nodes without depending on fixed cellular base stations.

However, communication reliability depends on node availability, wireless connectivity, network density and routing.

## 9. Results

The program generates:

- Cellular and ad hoc network architecture diagrams.
- Network comparison CSV file.
- Connectivity analysis results.
- Network comparison graph.

## 10. Folder Structure

```text
Q3_Cellular_vs_AdHoc/
│
├── cellular_vs_adhoc.py
├── README.md
│
├── diagrams/
│   └── network_architectures.png
│
├── results/
│   ├── network_comparison.csv
│   └── connectivity_analysis.txt
│
└── graphs/
    └── network_comparison.png
```

## 11. Execution

Install the required libraries:

```bash
pip install matplotlib pandas networkx
```

Run the program:

```bash
python cellular_vs_adhoc.py
```

The program can also be executed using Google Colab.

## 12. Conclusion

The comparison demonstrates the differences between infrastructure-based cellular networks and infrastructure-less ad hoc wireless networks. Cellular networks depend on base stations and centralized infrastructure, whereas ad hoc networks allow mobile nodes to communicate through direct and multi-hop connections. Therefore, ad hoc networks can be a suitable choice for temporary emergency communication when fixed infrastructure is unavailable.

**Note:** The implementation uses predefined network topologies and illustrative comparison scores. It is an educational connectivity analysis, not a real-world wireless network simulation.