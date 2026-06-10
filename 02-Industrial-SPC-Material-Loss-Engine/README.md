# Real-Time Statistical Process Control (SPC) & Closed-Loop Material Loss Engine

## 📖 Table of Contents

1. [Problem Statement](#1-problem-statement)
2. [Solution Overview](#2-solution-overview)
3. [System Deployment & Implementation](#3-System-Deployment--Implementation)
4. [Key Concepts & Data Model](#4-key-concepts--data-model)
5. [Statistical Process Control (SPC) & Early-Warning Logic](#5-Statistical-Process-Control-(SPC)--Early-Warning-Logic)
6. [Dashboards & Visualizations](#6-dashboards--visualizations)
7. [Operational Playbooks & Alerts](#7-operational-playbooks--alerts)
8. [Testing, Validation & Metrics](#8-testing-validation--metrics)
9. [Security, Access Control & IP](#9-security-access-control--ip)
10. [Roadmap & Next Steps](#10-roadmap--next-steps)
11. [Contributing](#11-contributing)
12. [License & Attribution](#12-license--attribution)
13. [Appendices](#13-appendices)

---

### Executive Summary
In continuous plastic extrusion and manufacturing, untracked raw material variance and delayed quality feedback directly erode gross margins. This project delivers an enterprise-grade Decision Intelligence system deployed for a major PVC manufacturing plant in Kenya.

The engine introduces a **two-tier inventory validation gate** combined with live **Statistical Process Control (SPC)**. It shifts the facility from lagging weekly retrospective reporting to active, real-time variance detection, protecting intellectual property and isolating hidden process losses within a 24-hour window.

---

## 1. Problem Statement
Most manufacturing operations do not have a data problem—they have a latency problem. At this PVC extrusion facility, material loss was tracked only via lagging weekly percentage averages, which were narrow, retrospective, and raised alarms only after significant waste had already accumulated.

The business pain was threefold:
* **Invisible Giveaway:** Operators running machines heavy to stay within spec rather than on target.
* **Cross-Department Blame:** Production, Finance, and Quality each holding different numbers with no single source of truth.
* **Margin Erosion:** Engineering over-weight giveaway silently compounding into tens of thousands of dollars per year. The Quality team bore the brunt of the blame without the data tools to defend or improve their position.

We deployed a real-time Closed-Loop Material Loss & SPC Engine with two-tier reconciliation—a **Store Gate** (weekly macro-inventory) and a **Floor Gate** (daily micro-consumption)—and an early-warning evaluation of the first 10 production samples per run to catch process spikes before they generate significant scrap.

---

## 2. Solution Overview

### Architecture & System Data Flow
PLC/SCADA and manual floor logs feed the stream processor, which drives the SPC Engine, Reconciliation Engine, and Data Warehouse. Outputs surface on role-gated dashboards for floor, quality, and executive audiences.

### Component Map
| Component | Purpose | Inputs | Outputs | Stack | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Data Ingest** | Collect raw production, scrap, and store-issue data | PLC/SCADA signals, manual floor logs, ERP store gate issues | Normalized event records | Kafka / Airflow, Python | Target ingest latency < 5 min per batch |
| **Stream Processing** | Validate, deduplicate, and route events | Raw ingest events | Clean records to warehouse | Apache Kafka, dbt | Handles late-arriving manual entries |
| **SPC Engine** | Compute X-bar, Moving Range, UCL/LCL | 10-piece subgroup sample weights per product line | SPC events, control limit alerts | Python (NumPy/Pandas) | Recalculates limits dynamically per settings sheet |
| **Early-Warning Lookback** | Flag process spikes on the first 10 samples of a run | First subgroup per shift/run | Early-warning flag | Python | Prevents thousands of kg of scrap before shift completes |
| **Reconciliation Engine** | Store Gate vs. Floor Gate analysis | Weekly store issues (kg), daily floor consumption (kg), inline mass, floor scrap | Process loss %, variance window | Python, SQL (Postgres) | Two-tier: macro weekly + micro daily |
| **Process Capabilities** | Calculate Cp, Cpk per product line | SPC data, LSL/USL settings | Capability status, recommendations | Python (SciPy) | Flags "INCAPABLE" lines for immediate DOE action |
| **Dashboard & Alerts** | Surface KPIs and tables | Live charts, daily variance tables, alerts | Role-gated dashboard environments | Grafana / Power BI / Dash | Role-gated; no download/formula access for exec view |
| **Data Warehouse** | Single source of truth for all data | All pipeline outputs | Queryable analytical tables | PostgreSQL | 90-day hot retention; 2-year cold storage |
| **Access Controls** | Enforce role-based permissions | User roles (floor, quality, exec, finance) | Scoped views, stripped export rights | Postgres RLS, dashboard RBAC | Protects IP and prevents formula duplication |

---

## 3. System Deployment & Implementation

To maximize operational adoption and completely eliminate standard enterprise software licensing and IT infrastructure costs, the entire engine is architected natively within the Google Workspace ecosystem. This allows for an ultra-low friction, zero-downtime deployment.

### 📋 Enterprise Requirements
* **Platform:** Google Workspace / Google Sheets (Zero local server footprints or database upkeep required).
* **Security:** Integrated OAuth 2.0 with native Google Identity Access Management (IAM).
* **Deployment Time:** < 2 Hours from template provisioning to live floor data capture.

### 🚀 Strategic Implementation Blueprint
1. **Master Architecture Provisioning:** The core analytical workbook, including the automated mass-balance matrices and SPC early-warning engines, is copied directly into the organization's secure corporate Google Drive.
2. **Floor Input Mapping:** Data entry cells are designated on standard floor tablets or terminals, enabling supervisors to log raw metrics natively with automated input validation to block typos or data corruption.
3. **Executive Dashboard Routing:** Role-gated views are instantly generated for Plant Directors, Finance, and Quality Teams, delivering real-time operational transparency without exposing underlying master formulas or proprietary IP.

## 4. Key Concepts & Data Model

### Core Terminology
* **Subgrouping (10-piece):** Every 10 consecutive pieces from a product line form one subgroup. This cadence is the foundation of valid X-bar SPC charting, enables early-shift spike detection, and gives floor supervisors an actionable signal without waiting for end-of-shift summaries.
* **Store Gate:** The weekly macro-reconciliation layer. Physical bulk raw material (kg) issued from the store to the floor is logged weekly and forms the upper boundary of material accountability.
* **Floor Gate:** The daily micro-reconciliation layer. Machine supervisor consumption (kg) is matched against calculated total output—inline good mass plus tracked floor scrap—to isolate process loss within a 24-hour window.
* **Inline Good Mass:** The total calculated mass of conforming product produced in a shift, derived from `piece count × target BOM weight per unit`.
* **Floor Scrap:** Physically weighed and logged scrap material (trims, purges, rejects) collected on the production floor each shift.
* **Engineering Giveaway:** The mass produced above the BOM target weight—product given to customers for free due to machine over-weight setting. Classified as an unbilled profit loss.
* **Unaccounted Process Loss:** The residual variance after all tracked categories (BOM mass, regrind/scrap, giveaway) are subtracted from total material input. Attributable to dust, fluff, moisture, and purge losses.
* **The Ingest Layer (Floor Logs):** Raw shift counts, scrap weights, and 10-piece sample measurements are captured via optimized data-entry logs with built-in data validation to prevent entry errors.
* **The Reference & Calculation Engine (`Gutters New`):** Houses the master product specifications, nominal BOM targets, and historical statistical constants. It runs the automated `MAP` + `LAMBDA` array formulas to instantly compute control boundaries and process deviations across thousands of rows without manual dragging.
* **The Audit Layer (Master PM Workbook):** Aggregates weekly warehouse store issues against daily aggregated floor outputs to calculate the final mass balance and output the precise financial classifications.

---
## 5. Statistical Process Control (SPC) & Early-Warning Logic

Instead of waiting for a weekly or monthly inventory audit to reveal that a product line has been running heavy, the engine utilizes real-time Statistical Process Control (SPC) to capture and flag machine drift the moment it occurs on the floor.

### 📈 X-Bar & Moving Range (MR) Framework

To eliminate tracking noise and isolate true structural process variation, the system groups raw weight samples into highly disciplined analytical frameworks:

* **Subgroup Optimization (10-Piece Cadence):** For each 10-piece sample cycle, the engine automatically computes the subgroup mean ($\bar{X}$ / X-bar) and the Moving Range ($MR$) between consecutive subgroup averages.
* **Dynamic Control Limits:** Upper and Lower Control Limits (UCL / LCL) are dynamically calculated at $\pm3\sigma$ (sigma) of within-subgroup variation, using historical process baselines and standard industrial engineering constants. 
* **Process Capability Anchors:** The system charts the process center line against the grand mean of all subgroup averages, while simultaneously overlaying Upper and Lower Specification Limits (USL / LSL). This supports live $C_p$ and $C_{pk}$ capability analysis to ensure the lines are physically capable of hitting target metrics.

---

### 🛑 Proactive Early-Warning Lookback

The highest financial leverage of this engine comes from its predictive capability at the absolute start of an extrusion run, bypassing the standard operational lag that plagues traditional plants.

* **Instantaneous Validation:** At the initialization of any product run, the engine evaluates the very first 10 samples (the first complete subgroup) and instantly scores the mean against established control boundaries.
* **Pre-Emptive Deficit Prevention:** If the initial subgroup mean breaches the UCL or LCL, the dashboard immediately triggers a critical validation flag. 
* **The Business Impact:** This alert empowers the floor supervisor to halt operations and recalibrate the extruder barrel *before* the run generates significant over-weight giveaway or under-weight structural scrap. By correcting the process drift at piece 10 instead of piece 10,000, **the system actively prevents thousands of kilograms of material waste per shift.**

## 6. Operational Playbooks & Alerts

### Automated Alert Rules
| Trigger Condition | Alert | Audience | Priority |
| :--- | :--- | :--- | :--- |
| First subgroup X-bar > UCL or < LCL | Early-Warning Spike | Floor Supervisor, Quality Lead | **Critical** |
| Any subgroup mean outside control limits | UCL/LCL Breach (mid-run) | Quality Lead | **Critical** |
| `daily_floor_material_variance_kg` > 500 kg or `pct_floor_mat_variance` > 5% | Daily Variance Threshold | Production Manager, Finance | **High** |
| Cpk < 1.0 | Process Capabilities tab flags "INCAPABLE" | Quality Lead, Engineering | **High** |
| % process loss > 2% on Weekly Material Logs | Weekly Process Loss | Plant Manager, Finance | **Medium** |

### On-Call Playbook (For Floor Supervisors)
1. **Pause** the current run at the next natural break point if an Early-Warning or UCL/LCL breach occurs.
2. **Check** machine die/tooling temperature and screw speed settings against the Settings sheet targets.
3. **Recalibrate** to the target weight center line—not just within specification limits.
4. **Log** the intervention in the `floor_scrap` table with an operational note.
5. **Restart** and confirm the next subgroup mean falls within UCL/LCL before resuming full production.

---

## 7. Security, Access Control & IP
We enforce a strict role-based access control (RBAC) model across all data surfaces to protect proprietary logic:
* **Floor Operators:** Read-only access to their product line's current SPC chart and shift sample entry forms. No access to financial data or control limit settings.
* **Quality Leads:** Full read access to all SPC data, Process Capabilities, and alert history. Write access to floor scrap logs and operational notes.
* **Finance & Executive:** Secure, view-only dashboard access to daily variance, weekly process loss, and executive summary KPIs. Zero access to underlying formulas, schemas, or raw data exports.

All dashboard instances have download and duplication permissions disabled for non-admin roles to protect core system IP, including control limit derivation logic and the capability index decision matrix.

---

## 8. License & Attribution
This project is released under the **MIT License**.

Built and deployed in partnership with the plant operations and quality team at a major PVC manufacturing facility in Kenya. Special recognition to the Plant Quality Lead and the production floor team for rapid collaboration, immediate floor execution, and trust in data-driven process management.

### System Maintainers
* **Fred** | Data Engineer | pipeline & systems architecture
* **J.N.S** | Plant Quality Lead | SPC chart validation & floor implementation
