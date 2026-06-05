# Engineering System Architecture

The core data pipeline functions as a closed-loop system capturing real-time extrusion measurements, executing automated Statistical Process Control alerts, and matching floor consumption against bulk store balances.

### Data Flow Diagram
1. Raw Scale Weight Data Entry / PLC Signals
2. Ingest Layer (Deduplication & Validation)
3. Analytics Engine (Control Limit Check & Capability Scores)
4. Persistent Storage Layer (PostgreSQL Warehouse)
5. Access-Controlled Visualization Interfaces
