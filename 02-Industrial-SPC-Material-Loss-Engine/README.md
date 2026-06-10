# Real-Time Statistical Process Control (SPC) & Closed-Loop Material Loss Engine

## 📖 Table of Contents

1. [Problem Statement](#1-problem-statement)
2. [Solution Overview](#2-solution-overview)
3. [System Deployment & Implementation](#3-system-deployment--implementation)
4. [Key Concepts & Data Model](#4-key-concepts--data-model)
5. [Statistical Process Control (SPC) & Early-Warning Logic](#5-statistical-process-control-spc--early-warning-logic)
6. [Dashboards & Executive Visualizations](#6-dashboards--executive-visualizations)
7. [Operational Playbooks & Alerts](#7-operational-playbooks--alerts)
8. [Strategic Key Performance Indicators (KPIs)](#8-strategic-key-performance-indicators-kpis)
9. [Security, Access Control & IP](#9-security-access-control--ip)
10. [Strategic Roadmap & Next Steps](#10-strategic-roadmap--next-steps)
11. [Organizational Scaling & Adaptability](#11-organizational-scaling--adaptability)
12. [License & Attribution](#12-license--attribution)

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
Manual floor logs and quality samples are routed directly into a centralized calculation engine. This engine drives the SPC metrics, daily reconciliations, and the Master PM database. Outputs are surfaced on role-gated, read-only dashboard surfaces for floor supervisors, quality leads, and executive audiences.

### Component Map
| Component | Purpose | Inputs | Outputs | Stack | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Data Ingest** | Collect raw production, scrap, and weight samples | Floor tablets, optimized entry forms | Cleaned event records | Google Sheets Forms / Data Validation | Enforces strict input rules to prevent data corruption |
| **Processing Engine** | Validate, deduplicate, and calculate metrics | Raw ingest entries | Formatted records to Master PM | Google Apps Script / Array Formulas | Eliminates manual data entry lag |
| **SPC Engine** | Compute X-bar, Moving Range, UCL/LCL | 10-piece subgroup sample weights per line | SPC charting, control limit boundaries | `Gutters New` Ref Tab (`MAP`/`LAMBDA`) | Recalculates limits dynamically based on active targets |
| **Early-Warning Lookback** | Flag process spikes on the first 10 samples of a run | First subgroup per shift/run | Early-warning flag | Dynamic Cell Formatting / Logic | Prevents thousands of kg of scrap before shift completes |
| **Reconciliation Engine** | Store Gate vs. Floor Gate analysis | Weekly store issues (kg), daily floor consumption | Process loss %, variance window | Master PM Workbook | Two-tier: macro weekly + micro daily |
| **Process Capabilities** | Calculate Cp, Cpk per product line | SPC data, LSL/USL settings | Capability status, actionable recommendations | Statistical Array Logic | Flags "INCAPABLE" lines for immediate mechanical action |
| **Dashboards & Alerts** | Surface KPIs and operational tables | Live charts, daily variance metrics | Role-gated dashboard environments | Google Workspace Gated Views | Executive metrics without exposing raw formulas |

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

---

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

```text
[Start of Production Run] 
         │
         ▼
[Sample First 10 Pieces] ──> [Automated Formula Scan]
                                     │
                    ┌────────────────┴────────────────┐
                    ▼                                 ▼
         [Within Control Limits]             [Breaches UCL / LCL]
                    │                                 │
                    ▼                                 ▼
         🟢 RUN AUTHORIZED                    🚨 IMMEDIATE FLAG RAISED
                                             (Supervisor Recalibrates 
                                              BEFORE Material Waste)
```

* **Instantaneous Validation:** At the initialization of any product run, the engine evaluates the very first 10 samples (the first complete subgroup) and instantly scores the mean against established control boundaries.
* **Pre-Emptive Deficit Prevention:** If the initial subgroup mean breaches the UCL or LCL, the dashboard immediately triggers a critical validation flag. 
* **The Business Impact:** This alert empowers the floor supervisor to halt operations and recalibrate the extruder barrel *before* the run generates significant over-weight giveaway or under-weight structural scrap. By correcting the process drift at piece 10 instead of piece 10,000, **the system actively prevents thousands of kilograms of material waste per shift.**

---

## 6. Dashboards & Executive Visualizations

The system features a multi-tiered, role-gated reporting architecture designed to provide immediate operational visibility to floor supervisors while serving high-level financial health metrics directly to the executive suite.

### 📊 Strategic Information Architecture

The workbook is organized into four dedicated operational control layers:

#### 1. Real-Time Process Visibility (Production Control Surface)
* **X-Bar Control Tracking:** The top row features live, dynamically updating control charts for every active product line (**Gutter, 140mm Casings, 160mm Casings, 160mm PN6, Downpipes, 200mm Casings**).
* **Metric Overlays:** Each chart visualizes shift averages against nominal targets, the statistical center line, operational boundaries (UCL/LCL), and strict engineering tolerances (USL/LSL). 
* **Temporal Tracking:** Integrated weekly separators allow supervisors to immediately isolate batch performance variations across different shift teams.

#### 2. Daily Material Consumption Variance (Floor Summary Layer)
* **Micro-Reconciliation Ledger:** A daily audit table that automatically aggregates material metrics across the plant floor.
* **Core Metrics Tracked:** Tracks raw mass consumption, inline good mass output, and physically weighed floor scrap.
* **Automated Yield Analysis:** Instantly computes physical floor variance (kg) and percentage deviations, serving as the primary diagnostic tool for catching unaccounted material drift before the week concludes.

#### 3. Mass Balance KPI Surface (Executive Financial View)
* **Executive KPI Cards:** A macro-level command center displaying high-level operational health indicators: *Total Pieces Extruded, Actual Mass Consumed, Total Scrap (kg),* and *Engineering Giveaway Mass/Percentage.*
* **Material Destination Breakdown:** A clean, visual financial classification matrix that segments every kilogram of raw material into its true economic endpoint:
  * **Conforming BOM Weight:** Revenue-generating mass shipped to customers.
  * **Regrind/Scrap Weight:** Material caught on the floor to be recycled or written off.
  * **SPC Over-Weight Giveaway:** Profit margin quietly lost to running heavy.
  * **Unaccounted Process Loss:** True material deficits needing operational investigation.

#### 4. Process Capability & Optimization (Continuous Improvement Engine)
* **Capability Matrix:** A automated per-product $C_p$ and $C_{pk}$ capability table that mathematically scores how reliably a machine line can hold its structural targets without drifting.
* **Process Sigma Scores:** Dynamically evaluates current machine capability status (e.g., *Capable, Marginally Capable, Action Required*).
* **Auto-Generated Operational Recommendations:** Translates statistical variances into plain-English directives for the engineering team (e.g., *"Initiate die-centering calibration on Line 3"* or *"Review raw material blend consistency"*).

---

## 7. Operational Playbooks & Alerts

A premium data architecture is only as effective as the operational discipline it enforces. To ensure real-time insights translate directly into margin protection, the system establishes mandatory, step-by-step action playbooks for floor personnel and quality managers.

### Automated Alert Rules
| Trigger Condition | Alert | Audience | Priority |
| :--- | :--- | :--- | :--- |
| First subgroup X-bar > UCL or < LCL | Early-Warning Spike | Floor Supervisor, Quality Lead | **🔴Critical** |
| Any subgroup mean outside control limits | UCL/LCL Breach (mid-run) | Quality Lead | **🔴Critical** |
| Daily variance > 500 kg or > 5% | Daily Variance Threshold | Production Manager, Finance | **🟠High** |
| Cpk < 1.0 | Capability Matrix flags "INCAPABLE" | Quality Lead, Engineering | **🟠High** |
| % process loss > 2% on Weekly Logs | Weekly Process Loss | Plant Manager, Finance | **🟡Medium** |

### 🚨 On-Call Playbook (For Floor Supervisors)
1. **Pause** the current run at the next natural break point if an Early-Warning or UCL/LCL breach occurs.
2. **Check** machine die/tooling temperature and screw speed settings against the target parameters.
3. **Recalibrate** to the target weight center line—not just within specification limits.
4. **Log** the intervention in the **Floor Scrap Log** tab with an operational note.
5. **Restart** and confirm the next subgroup mean falls within UCL/LCL before resuming full production.

### 🚨 On-Call Playbook (Quality Leads)
When the automated engine flags a process deviation—such as a critical capability breach ($C_{pk} < 1.0$) or an X-bar control limit violation—the team executes the following mandatory containment protocol:

1. **Isolate & Audit:** Immediately pull the *Process Capabilities* report on the centralized dashboard for the flagged product line.
2. **Execute First-Line Diagnostics:** Review the system's auto-generated operational recommendation (e.g., *"Initiate mechanical Design of Experiments (DOE). Inspect screw wear profile, audit barrel temperature cycling zones, or verify raw material blend consistency"*).
3. **Engineering Escalation:** If the system-generated diagnostic requires a mechanical inspection or a complex adjustment, immediately escalate the ticket to the plant engineering department.
4. **Institutional Logging:** Document the exact root cause, timestamps, and mechanical interventions directly into the centralized **SPC Event Log** tab to build a historical maintenance baseline.

---

### 📋 Shift Handover Checklist (SPC Event Active)
To completely eliminate operational blind spots during shift changeovers—a major source of material waste in traditional manufacturing—supervisors must complete this rigorous data verification before signing off:

* [ ] **Active Event Verification:** Confirm that the active SPC event type and affected product line are fully logged in the **SPC Event Log** tab.
* [ ] **Statistical Baseline Note:** Document the exact X-bar deviation value, active UCL/LCL boundaries, and the precise subgroup number where the initial breach was captured.
* [ ] **Intervention Logging:** Record every physical machine adjustment made during the shift with an exact timestamp.
* [ ] **Financial Threshold Check:** Flag the daily variance entry if the calculated material mass loss has breached the company's maximum cost tolerance threshold.
* [ ] **Relief Briefing:** Conduct a face-to-face brief with the incoming shift supervisor regarding the open event, current machine drift trend, and active stabilization attempts.
* [ ] **Gatekeeper Sign-off:** Physically verify that the first 10-piece subgroup of the incoming shift passes the *Early-Warning Lookback* check before officially transferring control of the production line.

---

## 8. Strategic Key Performance Indicators (KPIs)

To maintain absolute operational control and safeguard corporate margins, executive leadership and plant directors monitor the engine through a strictly defined operational scorecard. 

| Core Business Metric | Target Benchmark | Data Source (Workbook Layer) | Strategic Objective |
| :--- | :--- | :--- | :--- |
| **Data Reconciliation Window** | $< 24$ Hours | `Daily Variance` Tab | Minimizes operational lag; guarantees that material drift is caught before it impacts the weekly P&L. |
| **Engineering Giveaway %** | Optimized toward $0\%$ | `Master PM Workbook` / `Gutters New` | Eradicates silent margin erosion from running profiles heavier than nominal specification limits. |
| **Regrind Recovery Efficiency** | Maximized vs. Total Scrap | `Floor Scrap Log` Tab | Ensures floor purges and startup trims are systematically recycled back into production, lowering virgin resin costs. |
| **Potential Process Capability ($C_p$)** | $\ge 1.33$ | `Process Capabilities` Tab | Measures the theoretical capability of the extrusion machinery under optimized conditions. |
| **Actual Process Capability ($C_{pk}$)** | $\ge 1.0$ | `Process Capabilities` Tab | Tracks the real-world, shift-by-shift performance of the line, accounting for machine drift and operator adjustments. |
| **Data Entry Compliance Rate** | $\ge 99.5\%$ of active shifts | Master Audit Trail | Tracks floor supervisor compliance in submitting shift validation metrics on time. |
| **Early-Warning Response Latency** | $< 15$ Minutes | `SPC Event Log` Tab | Measures organizational agility—the exact time elapsed between an automated control limit breach and documented corrective action. |

---

## 9. Security, Access Control & IP

We enforce a strict role-based access control (RBAC) model across all data surfaces to protect proprietary logic:
* **Floor Operators:** Read-only access to their product line's current SPC chart and shift sample entry forms. No access to financial data or control limit settings.
* **Quality Leads:** Full read access to all SPC data, Process Capabilities, and alert history. Write access to floor scrap logs and operational notes.
* **Finance & Executive:** Secure, view-only dashboard access to daily variance, weekly process loss, and executive summary KPIs. Zero access to underlying formulas, schemas, or raw data exports.

All dashboard instances have download and duplication permissions disabled for non-admin roles to protect core system IP, including control limit derivation logic and the capability index decision matrix.

---

## 10. Strategic Roadmap & Next Steps

To transition the manufacturing floor from a reactive data posture to a fully predictive, automated operating environment, the next phase of the architecture focuses on scaling insights into automated operational actions.

### 🎯 Phase 2 Implementation Initiatives

#### 1. Financial Pareto Analysis (The 80/20 Margin Filter)
* **Objective:** Architect dynamic Pareto models that instantly slice and rank the root causes of engineering giveaway and process loss.
* **Impact:** Allows management to isolate exactly which machine, product line, or raw material formulation is responsible for the top 80% of financial variance, optimizing resource allocation.

#### 2. Advanced Process Optimization (Design of Experiments - DOE)
* **Objective:** Run structured, data-driven DOEs correlating machine settings (screw speed, multi-zone temperature profiles, die geometries) with physical PVC formulation variables.
* **Impact:** Systematically uncovers and institutionalizes the absolute "operating sweet spot" for each product line, guaranteeing high-margin runs regardless of operator experience.

#### 3. Real-Time Closed-Loop Regrind Integration
* **Objective:** Develop an automated decision-rule engine that programmatically categorizes floor scrap into regrind-eligible versus true waste streams.
* **Impact:** Automatically routes eligible recycled mass back into the active material balance log in real time, drastically lowering virgin material consumption metrics.

#### 4. Predictive Asset Maintenance (Cpk to CapEx Correlation)
* **Objective:** Build an analytics pipeline that cross-references continuous downward trends in Cpk with physical maintenance logs.
* **Impact:** Flags structural die wear and extrusion screw degradation *weeks before* they breach engineering limits, shifting capital asset management from emergency downtime to proactive scheduling.

#### 5. Pareto-Driven Calibration Automation
* **Objective:** Programmatically trigger precision machine-recalibration work orders based on the ranked giveaway contributors identified in the Pareto engine.
* **Impact:** Removes human guesswork or arbitrary scheduling from toolroom maintenance, ensuring the highest-bleeding assets are prioritized first.

---

## 11. Organizational Scaling & Adaptability

While this engine was custom-built to solve structural material control issues on our primary extrusion lines, the underlying information architecture is fully modular and designed for multi-plant deployment.

* **Internal Collaboration:** We welcome cross-functional collaboration between Plant Operations, Quality Assurance Leads, and Corporate Finance teams to further customize alert thresholds and reporting cadences.
* **Framework Adaptability:** The master calculation engines, reference schema layouts, and SPC charting matrices can be seamlessly cloned and re-mapped to support parallel manufacturing operations (e.g., injection molding, compounding lines, or secondary packaging facilities) with minimal configuration changes.

---

## 12. License & Attribution

This project is released under the **MIT License**.

Built and deployed in partnership with the plant operations and quality team at a major PVC manufacturing facility in Kenya. Special recognition to the Plant Quality Lead and the production floor team for rapid collaboration, immediate floor execution, and trust in data-driven process management.

### System Maintainers
* **Fred** | Data Engineer | pipeline & systems architecture
* **J.N.S** | Plant Quality Lead | SPC chart validation & floor implementation
