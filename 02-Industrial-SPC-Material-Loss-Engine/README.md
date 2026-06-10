# Real-Time Statistical Process Control (SPC) & Closed-Loop Material Loss Engine

## 📖 Table of Contents

1. [Problem Statement](#1-problem-statement)
2. [Solution Overview](#2-solution-overview)
3. [Getting Started](#3-getting-started)
4. [Key Concepts & Data Model](#4-key-concepts--data-model)
5. [SPC & Early-Warning Logic](#5-spc--early-warning-logic)
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

## 3. Key Concepts & Data Model

### Core Terminology
* **Subgrouping (10-piece):** Every 10 consecutive pieces from a product line form one subgroup. This cadence is the foundation of valid X-bar SPC charting, enables early-shift spike detection, and gives floor supervisors an actionable signal without waiting for end-of-shift summaries.
* **Store Gate:** The weekly macro-reconciliation layer. Physical bulk raw material (kg) issued from the store to the floor is logged weekly and forms the upper boundary of material accountability.
* **Floor Gate:** The daily micro-reconciliation layer. Machine supervisor consumption (kg) is matched against calculated total output—inline good mass plus tracked floor scrap—to isolate process loss within a 24-hour window.
* **Inline Good Mass:** The total calculated mass of conforming product produced in a shift, derived from `piece count × target BOM weight per unit`.
* **Floor Scrap:** Physically weighed and logged scrap material (trims, purges, rejects) collected on the production floor each shift.
* **Engineering Giveaway:** The mass produced above the BOM target weight—product given to customers for free due to machine over-weight setting. Classified as an unbilled profit loss.
* **Unaccounted Process Loss:** The residual variance after all tracked categories (BOM mass, regrind/scrap, giveaway) are subtracted from total material input. Attributable to dust, fluff, moisture, and purge losses.

---

## 4. Operational Playbooks & Alerts

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

## 5. Security, Access Control & IP
We enforce a strict role-based access control (RBAC) model across all data surfaces to protect proprietary logic:
* **Floor Operators:** Read-only access to their product line's current SPC chart and shift sample entry forms. No access to financial data or control limit settings.
* **Quality Leads:** Full read access to all SPC data, Process Capabilities, and alert history. Write access to floor scrap logs and operational notes.
* **Finance & Executive:** Secure, view-only dashboard access to daily variance, weekly process loss, and executive summary KPIs. Zero access to underlying formulas, schemas, or raw data exports.

All dashboard instances have download and duplication permissions disabled for non-admin roles to protect core system IP, including control limit derivation logic and the capability index decision matrix.

---

## 6. License & Attribution
This project is released under the **MIT License**.

Built and deployed in partnership with the plant operations and quality team at a major PVC manufacturing facility in Kenya. Special recognition to the Plant Quality Lead and the production floor team for rapid collaboration, immediate floor execution, and trust in data-driven process management.

### System Maintainers
* **Fred** | Data Engineer | pipeline & systems architecture
* **Jotham** | Plant Quality Lead | SPC chart validation & floor implementation
