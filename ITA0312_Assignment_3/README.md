# Mobile Computing – Assignment 3 (CO3)

## Assignment Information

| Detail | Information |
|---|---|
| Subject | Mobile Computing |
| Assignment | Assignment 3 – CO3 |
| Mode | Pair Work |
| Group Size | 2 Students |
| Duration | 1 Week |
| Total Marks | 50 |
| Student A | CH. Rama Krishna – 192372280 |
| Student B | K. Navadeep Reddy – 192311305 |

## 1. Overview

This assignment explores the fundamental concepts of mobile computing, wireless network architecture, mobility management, Mobile IP, cellular and ad hoc networks, and routing protocols.

The assignment consists of seven questions covering theoretical analysis, network architecture design, Python-based simulations, performance evaluation, and a collaborative emergency communication network design.

The primary objective is to understand how wireless networks operate, how mobile devices maintain communication while moving between networks, and how routing protocols support communication in dynamic mobile environments.

## 2. Objectives

- Understand wireless network architecture and communication characteristics.
- Analyse mobility, handoff, packet loss, and transmission delay.
- Study Mobile IP architecture and mobility management.
- Understand agent discovery, registration, and packet tunnelling.
- Compare cellular and ad hoc wireless networks.
- Explore real-world applications of Mobile IP.
- Study proactive routing using DSDV.
- Study reactive routing using AODV.
- Compare routing overhead, delay, and mobility handling.
- Design and evaluate a mobile emergency communication network.

## 3. Technologies and Tools Used

| Technology / Tool | Purpose |
|---|---|
| Python | Simulation and implementation |
| Google Colab | Execution environment |
| NetworkX | Network topology and graph analysis |
| NumPy | Numerical operations |
| Pandas | Data processing and CSV generation |
| Matplotlib | Graphs and network visualisation |

## 4. Software Requirements

### Required Software

- Python 3.10 or later
- Google Colab or a local Python environment
- A web browser
- Git and GitHub for repository management

### Python Libraries

The following libraries are required:

```bash
pip install numpy pandas matplotlib networkx
```

### Library Installation in Google Colab

Run this command before executing the Python scripts:

```python
!pip install -q numpy pandas matplotlib networkx
```

No paid APIs or external services are required for these simulations.

## 5. Project Structure

```text
ITA0312_Assignment-3/
│
├── README.md
├── requirements.txt
│
├── Q1_Wireless_Network_Architecture/
│   ├── q1_wireless_analysis.py
│   ├── mobility_simulation.py
│   ├── diagrams/
│   ├── results/
│   ├── graphs/
│   └── screenshots/
│
├── Q2_Mobile_IP/
│   ├── mobile_ip_simulation.py
│   ├── diagrams/
│   ├── results/
│   └── graphs/
│
├── Q3_Cellular_vs_AdHoc/
│   ├── cellular_vs_adhoc.py
│   ├── diagrams/
│   ├── results/
│   └── graphs/
│
├── Q4_Mobile_IP_Applications/
│   ├── ambulance_network.py
│   ├── diagrams/
│   ├── results/
│   └── graphs/
│
├── Q5_Proactive_Routing_DSDV/
│   ├── dsdv_simulation.py
│   ├── diagrams/
│   ├── results/
│   └── graphs/
│
├── Q6_Reactive_Routing_Comparison/
│   ├── aodv_dsdv_comparison.py
│   ├── diagrams/
│   ├── results/
│   └── graphs/
│
└── Q7_Emergency_Communication_Network/
    ├── emergency_network.py
    ├── diagrams/
    ├── results/
    └── graphs/
```

Each question folder contains its corresponding implementation and generated output files. Individual README files can also be maintained inside each question folder.

## 6. Assignment Modules and Implementations

### Q1 – Wireless Network Architecture and Mobility Analysis (6 Marks)

**Objective:** Understand wireless network architecture and analyse the effect of mobile-node movement on communication.

**Implementation:**
- Design an infrastructure-mode wireless network.
- Identify mobile nodes, access points, switches, and gateways.
- Simulate packet communication.
- Analyse mobility between wireless coverage areas.
- Compare stationary, pedestrian, and vehicle mobility conditions.
- Evaluate handoff interruption, packet loss, and delay.

**Files:**
- `q1_wireless_analysis.py`
- `mobility_simulation.py`

**Expected Outputs:**
- Wireless network architecture diagram.
- Mobility simulation results.
- Packet delivery and handoff analysis.
- Performance graphs and CSV files.

### Q2 – Mobile IP and Mobility Management (7 Marks)

**Objective:** Understand how Mobile IP maintains communication when a mobile node changes its network location.

**Implementation:**
- Represent Mobile Node (MN), Home Agent (HA), Foreign Agent (FA), and Correspondent Node (CN).
- Demonstrate agent discovery and registration.
- Simulate packet delivery and tunnelling.
- Analyse registration delay and tunnelling overhead.
- Compare triangular routing and an optimised routing scenario.
- Study mobility-related packet loss.

**File:** `mobile_ip_simulation.py`

**Expected Outputs:**
- Mobile IP architecture diagram.
- Registration sequence.
- Packet delivery results.
- Mobility analysis.
- Routing comparison and performance graphs.

### Q3 – Cellular Networks versus Ad Hoc Wireless Networks (7 Marks)

**Objective:** Compare infrastructure-based cellular networks and infrastructure-less ad hoc networks.

**Implementation:**
- Create cellular and ad hoc network topologies.
- Compare communication architecture and routing.
- Analyse connectivity and network failures.
- Study the impact of removing a base station or an intermediate node.
- Evaluate the suitability of both architectures for emergency situations.

**File:** `cellular_vs_adhoc.py`

**Expected Outputs:**
- Cellular network architecture.
- Ad hoc network architecture.
- Network comparison CSV.
- Connectivity analysis.
- Network comparison graph.

### Q4 – Applications of Mobile IP and Routing Requirements (7 Marks)

**Objective:** Explore the application of Mobile IP in a real-world mobile communication scenario.

**Selected Application:** Emergency Ambulance Communication Network.

**Implementation:**
- Represent an ambulance, visited networks, Home Agent, and communication endpoints.
- Simulate movement between network areas.
- Demonstrate care-of address changes.
- Analyse packet delivery during mobility.
- Evaluate handoff interruption and communication delay.

**File:** `ambulance_network.py`

**Expected Outputs:**
- Ambulance network architecture.
- Packet delivery results.
- Mobility event records.
- Performance summary.
- Performance graphs.

### Q5 – Proactive Routing Protocols in Mobile Networks (6 Marks)

**Selected Protocol:** Destination-Sequenced Distance Vector (DSDV).

**Objective:** Understand proactive routing and continuous routing-table maintenance.

**Implementation:**
- Create a mobile network topology.
- Generate routing tables.
- Analyse next-hop information and hop counts.
- Demonstrate topology changes.
- Compare routing information before and after link failure.
- Estimate routing update overhead.
- Analyse different network sizes.

**File:** `dsdv_simulation.py`

**Expected Outputs:**
- Initial and updated network topologies.
- Routing tables.
- Route comparison CSV.
- Network size analysis.
- Routing overhead summary and graphs.

### Q6 – Reactive Routing and Protocol Comparison (7 Marks)

**Selected Protocols:** AODV and DSDV.

**Objective:** Study reactive routing and compare its behaviour with proactive routing.

**Implementation:**
- Demonstrate AODV route discovery.
- Represent Route Request (RREQ).
- Represent Route Reply (RREP).
- Demonstrate conceptual Route Error (RERR).
- Simulate link failure and alternative route discovery.
- Compare AODV and DSDV.
- Analyse routing overhead and initial communication delay.
- Evaluate different network sizes.

**File:** `aodv_dsdv_comparison.py`

**Expected Outputs:**
- Initial MANET topology.
- AODV discovered route.
- Network topology after link failure.
- DSDV-inspired routing table.
- AODV and DSDV comparison CSV.
- Routing overhead and delay graphs.

### Q7 – Design a Mobile Emergency Communication Network (10 Marks)

**Objective:** Design a mobile emergency communication network for disaster-response situations.

**Scenario:** Ambulances, police vehicles, rescue teams, and medical personnel must communicate while moving across different geographical areas, even when fixed communication infrastructure is unavailable.

**Implementation:**
- Design an emergency communication network architecture.
- Represent Mobile IP components.
- Demonstrate a conceptual registration and tunnelling sequence.
- Establish a communication route between an ambulance and command centre.
- Simulate packet delivery and handoff events.
- Demonstrate link failure and alternative route availability.
- Test different network sizes and mobility conditions.
- Analyse delay, packet delivery, and routing overhead.

**File:** `emergency_network.py`

**Expected Outputs:**
- Emergency network architecture.
- Emergency communication route.
- Mobile IP registration sequence.
- Packet delivery results.
- Failure recovery analysis.
- Performance test cases.
- Delay, packet delivery, and routing overhead graphs.

## 7. Execution Instructions

All Python simulations can be executed using Google Colab.

### Step 1 – Open Google Colab

Visit:

https://colab.research.google.com/

### Step 2 – Upload the Python File

Upload the required Python file from the corresponding question folder.

### Step 3 – Install Dependencies

Execute:

```python
!pip install -q numpy pandas matplotlib networkx
```

### Step 4 – Execute the Program

For example:

```python
!python q1_wireless_analysis.py
```

Use the corresponding Python filename for each question.

### Step 5 – Generate Results

The programs generate the required diagrams, graphs, CSV files, and summary files.

### Step 6 – Download Outputs

The simulation scripts are configured to create downloadable ZIP archives containing their generated outputs where implemented.

Extract the ZIP files and place the generated folders inside their respective question directories.

## 8. Performance Evaluation Parameters

The assignment uses the following parameters to study network behaviour:

| Parameter | Description |
|---|---|
| Packet Delivery Ratio | Percentage of transmitted packets successfully delivered |
| Packet Loss | Number or percentage of packets not delivered |
| Transmission Delay | Time taken for packets to reach their destination |
| Handoff Delay | Interruption caused when a mobile node changes its point of attachment |
| Routing Overhead | Control information required for routing and route maintenance |
| Route Availability | Whether a valid route exists between source and destination |
| Mobility | Effect of mobile-node movement on communication |
| Network Size | Effect of increasing the number of nodes |

## 9. Student Responsibilities and Pair-Work Requirements

Both students are responsible for understanding the complete assignment. Primary contribution does not mean exclusive knowledge.

| Question | Student A – Primary Contribution | Student B – Primary Contribution |
|---|---|---|
| Q1 | Network architecture | Mobility analysis |
| Q2 | Mobile IP operation | Mobile IP challenges |
| Q3 | Cellular network | Ad hoc network |
| Q4 | Performance analysis | Application architecture |
| Q5 | Protocol design | Performance investigation |
| Q6 | Reactive routing | DSDV–AODV comparison |
| Q7 | Analytical validation | Experimental validation |

### Collaborative Requirements

- Both students must participate in every question.
- Q7 must be developed collaboratively.
- Both independent Q7 proposals must be retained.
- The two proposals must be compared before producing the final design.
- Both students must understand the complete submitted work.
- Each student must be prepared to explain their partner's contribution.

## 10. Q7 Design Challenge – Required Submission Evidence

The Q7 submission must include all six stages:

1. **Independent Design Proposal:** Student A and Student B prepare separate initial proposals.
2. **Design Comparison:** Identify agreements, differences, strengths, weaknesses, Mobile IP requirements, routing suitability, overhead, delay, and mobility handling.
3. **Joint Final Design:** Present the architecture, Mobile IP components, registration, tunnelling, routing protocol, and failure handling.
4. **Validation:** Student A performs analytical validation; Student B performs experimental validation.
5. **Cross-Defence:** Both students explain the technical responsibilities primarily handled by their partner.
6. **Joint Evaluation:** Justify the architecture, Mobile IP, routing selection, overhead, mobility impact, connectivity loss, and limitations.

## 11. Simulation Scope and Limitations

The Python programs are educational simulations designed to demonstrate mobile computing concepts and analyse network behaviour.

They do not constitute complete implementations of the corresponding wireless standards or routing protocols.

- NetworkX is used for topology representation and graph-based route calculations.
- Some delay, packet-loss, handoff, and routing-overhead values are simulated or estimated.
- Mobile IP registration and tunnelling are represented conceptually in the relevant programs.
- AODV and DSDV behaviour is simplified for educational comparison.
- Results should be interpreted according to the assumptions implemented in each simulation.

The generated outputs should not be interpreted as measurements from physical wireless devices or a real-world network deployment.

## 12. Conclusion

This assignment provides practical exposure to wireless communication, mobility management, Mobile IP, cellular and ad hoc networks, and proactive and reactive routing protocols.

Through the seven questions, the assignment explores network architecture, routing behaviour, mobility-related challenges, and performance evaluation.

The final emergency communication network design combines the concepts studied throughout the assignment to demonstrate how mobile communication systems can support emergency-response operations in dynamic environments.

---

**Mobile Computing – Assignment 3 (CO3)**  
**Pair Work Submission**  
**CH. Rama Krishna – 192372280**  
**K. Navadeep Reddy – 192311305**