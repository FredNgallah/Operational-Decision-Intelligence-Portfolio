# Operational Decision Intelligence: FMCG Commercial Field Optimization
## Kilifi County Market Expansion Case Study

**Client:** A Growth-phase dairy manufacturer expanding into Kilifi County  
**Domain:** FMCG / Commercial Operations / Field Sales Analytics  
**Methodology:** Operational Standardization, Exploratory Data Analysis, Multivariate Driver Screening, Custom $2^2$ Factorial Design of Experiments (DOE), Multi-Response Prediction Profiler Optimization  
**Tooling:** JMP Pro 17+, Python 3.10+, Operational Data Architecture  

![Status](https://img.shields.io/badge/status-field%20validation%20active-yellow)
![Data](https://img.shields.io/badge/baseline-Jan–Jun%202026-blue)
![Tooling](https://img.shields.io/badge/modeling-JMP%20DOE-lightgrey)

---

## Executive Summary

When the Client expanded its yogurt line into Kilifi County, field operations faced severe structural opacity. A team of 5 sales representatives and 2 vehicles operated without defined territory boundaries, pitching products via paper brochures to arbitrary retail outlets based on gut feel.

This case study documents the transformation of an unstructured, opaque market expansion into a measurable, evidence-based commercial growth engine. By deploying a 20-domain operational data capture system, we audited 6,591 sales visits, isolated core commercial drivers, designed a custom $2^2$ factorial DOE in JMP, and established candidate operating settings optimized for both transaction scale and conversion probability.

```text
[Operational Chaos] ──► [System Standardization] ──► [Driver Screening] ──► [Custom DOE & Profiling] ──► [6-Month Field Validation]
 Ad-hoc pitches &        20-domain data capture       Isolated scale vs.        Simulated optimum:         Live market testing
 intuitive routes        system (6,591 visits)        conversion drivers        7D Credit / 35m Visit      across Kilifi County
```

---

## Executive Summary Dashboard

| Metric / Dimension | Baseline Value (Jan 1 – Jun 30, 2026) | Method / System Applied | Strategic Impact |
| :--- | :--- | :--- | :--- |
| **Audited Revenue** | **KES 11,648,320** | Line-Level Sales Reconciliation | Established true financial baseline across 3,846 orders |
| **Field Visit Volume** | **6,591 Visits** | Visit-Level Operational Workbook | Reconciled conversion baseline at 58.41% |
| **Primary Order Drivers** | **Size Tier $\times$ Shop Type** | OLS Regression ($R^2 \approx 0.487, p < 0.0001$) | Isolated segmentation as non-negotiable context |
| **Experimental Levers** | **Credit Terms & Duration** | JMP $2^2$ Custom Design ($N=32$) | Replaced intuition with structured hypothesis testing |
| **Model Optimum** | **7 Days Credit + 35 Min Visit** | Multi-Response Desirability Profiler | Identified candidate operating settings for field test |
| **Next Phase** | **6-Month Validation** | Live Route & Territory Monitoring | Validates simulated lift before full capital rollout |

---

## Act I: The Business Trajectory & Problem Statement

### The Starting Situation in Kilifi
When Meru Fresh Dairy Ltd. launched its yogurt line in Kilifi County, field operations faced classic growth-stage hurdles:
* **Unstructured Field Operations:** 5 sales representatives operating 2 vehicles conducted ad-hoc visits with no route prioritization or territory mapping.
* **Weak Demand Creation:** Sales pitches relied heavily on static paper brochures without formal credit terms or commercial structures.
* **Zero Operational Visibility:** Management lacked reliable data on sales visit volume, conversion rates, deliverability, or stockouts.

> **The Core Problem:** The Kilifi operation was not merely suffering from "low sales"—it was being run with limited structure, zero visibility, and no reliable evidence for decision-making.

---

## Act II: Making the Operation Measurable

Before asking what to optimize, we made the business measurable. We deployed an operational workbook capturing data across **20 operational domains**, including sales visits, orders, inventory movements, stockouts, delivery logistics, fuel consumption, and customer feedback.

```text
                             END-TO-END DATA FLOW & AUDIT ARCHITECTURE
  ┌──────────────────┐     ┌───────────────────┐     ┌──────────────────┐     ┌──────────────────┐
  │ 17_Daily_Visits  │ ──► │ 16_Daily_Sales    │ ──► │ 18_Deliveries    │ ──► │ 21_Stock_Movements
  │  (6,591 Visits)  │     │  (3,846 Orders)   │     │ (1,807 Completed)│     │  (Inventory Logs)│
  └──────────────────┘     └───────────────────┘     └──────────────────┘     └──────────────────┘
            │                        │                        │                        │
            └────────────────────────┴───────────┬────────────┴────────────────────────┘
                                                 ▼
                                ┌──────────────────────────────────┐
                                │ Enriched Commercial Dataset      │
                                │ • Net Revenue: KES 11,648,320    │
                                │ • Visit Conversion: 58.41%       │
                                │ • Audited Stockouts: 26 Events   │
                                └──────────────────────────────────┘
```

### Table 1: Before vs. After Operating Discipline

| Operating Dimension | Initial State (Intuition-Driven) | Standardized State (Data-Driven) |
| :--- | :--- | :--- |
| **Field Planning** | Random visits, unstructured routes | Territory mapping, scheduled route coverage |
| **Commercial Terms** | Standard cash-on-delivery pitching | Segmented credit terms (Cash vs. 7 Days) |
| **Pitch Governance** | Unmonitored, informal visit length | Standardized duration tiers (15 vs. 35 mins) |
| **Data Collection** | Ad-hoc verbal updates | Audited 20-domain operational workbook |
| **Decision Logic** | Management gut feeling | Statistical screening & response surface modeling |

---

## Act III: What the Baseline Data Revealed

Auditing six months of field data ($N=6,591$ visits) established the first empirical baseline in company history:

### Table 2: Audited Baseline Performance Snapshot

| Performance Metric | Audited Baseline Value | Analytical Takeaway |
| :--- | :--- | :--- |
| **Total Sales Visits** | 6,591 | Complete census of field rep touchpoints |
| **Converted Orders** | 3,846 | Visits resulting in immediate order bookings |
| **Conversion Rate** | 58.41% | Overall sales effectiveness baseline |
| **Net Baseline Revenue** | KES 11,648,320 | Total order-level revenue baseline |
| **Average Order Value (AOV)** | KES 3,028.68 | Mean value per successful order |
| **Revenue Per Visit (RPV)** | KES 1,767.30 | Value generated per sales opportunity |
| **Stockout Incidents** | 26 events (68 cumulative days) | Operational bottleneck constraining conversion |

---

## Act IV: From Many Variables to a Few (Driver Screening)

To avoid forcing every plausible variable into an experimental model, we conducted multivariate driver screening to separate non-controllable context from actionable commercial levers.

```text
                           FACTOR SCREENING & FILTERING PIPELINE
  CANDIDATE VARIABLES           SCREENING METHODOLOGY                DECISION & ROLE
 ┌──────────────────────┐      ┌──────────────────────┐      ┌──────────────────────────────┐
 │ • SalesRep Experience│ ──►  │ ANOVA & Logistic GLM │ ──►  │ ✖ DROPPED (Low explanatory)  │
 │ • Delivery Vehicle   │      │ OLS Regression       │      │ ✖ DROPPED (No excursion link)│
 │ • Spoilage Temp      │      │ Variance Analysis    │      │ ✖ DROPPED (Inconclusive model│
 │ • Shop Type          │      │ Interaction Screening│      │ ✔ RETAINED (Context Factor)  │
 │ • Customer Size Tier │      │ Multi-way ANOVA      │      │ ✔ RETAINED (Context Factor)  │
 │ • Credit Terms       │      │ Factorial Analysis   │      │ ✔ RETAINED (Actionable Lever)│
 │ • Visit Duration     │      │ Response Surface     │      │ ✔ RETAINED (Actionable Lever)│
 └──────────────────────┘      └──────────────────────┘      └──────────────────────────────┘
```

### Table 3: Key Factors — Retained vs. Dropped

| Factor Candidate | Statistical Evidence | Final Role | Business Rationale |
| :--- | :--- | :--- | :--- |
| **Customer Size Tier** | $p < 0.0001$, strong main effect | **Retained (Context)** | Primary driver of order magnitude |
| **Shop Type** | $p < 0.001$, significant interaction | **Retained (Context)** | Channel structure dictates order frequency |
| **Credit Terms ($x_1$)** | Directional yield lift | **Retained (Lever)** | Controllable commercial offer term |
| **Visit Duration ($x_2$)** | Directional yield lift | **Retained (Lever)** | Controllable rep behavior term |
| **Sales Rep Tenure** | Minimal conversion variance | **Dropped** | Rep performance is uniform; focus on levers |
| **Delivery Vehicle Type** | $p > 0.05$ on delivery delays | **Dropped** | Vehicle choice does not drive delay patterns |
| **Product Spoilage Rate** | $R^2 < 0.05$, weak fit | **Dropped** | Hypothesized link unsupported by data |

---

## Act V: Designing a Controlled Experiment (DOE)

Having narrowed the problem, we designed a custom **$2^2$ Full Factorial Experiment** replicated across customer context blocks using JMP Pro.

### Table 4: DOE Factor Definitions

| Experimental Factor | Factor Type | Level 1 (Low) | Level 2 (High) | Strategic Objective |
| :--- | :--- | :--- | :--- | :--- |
| **Credit Terms ($x_1$)** | Controllable Lever | Cash on Delivery | 7 Days Credit | Evaluate credit-driven order expansion |
| **Visit Duration ($x_2$)** | Controllable Lever | 15 Minutes | 35 Minutes | Test deep pitching vs. rapid coverage |
| **Shop Type** | Context Stratification | 6 Channel Types | Categorical | Control for baseline channel variation |
| **Size Tier** | Context Stratification | Small, Medium | Large | Control for baseline account scale |

---

## Act VI: What the Simulated Experiment Suggested

Using the 32-run experimental matrix, we fitted a Response Surface Model (RSM) to evaluate `revenue_per_visit`.

> **GOVERNANCE NOTICE:** The experimental response values were generated model-side for this case study. All predictions are explicitly categorized as **SIMULATED / MODEL-BASED HYPOTHESES** awaiting live market validation.

### Table 5: DOE Model Results Summary (Simulated)

| Treatment Cell | Credit Terms ($x_1$) | Pitch Duration ($x_2$) | Predicted RPV (KES) | Predicted Conversion |
| :---: | :---: | :---: | :---: | :---: |
| **Cell 1** | Cash | 15 Mins | KES 1,120.50 | 48.2% |
| **Cell 2** | Cash | 35 Mins | KES 2,450.00 | 58.6% |
| **Cell 3** | 7 Days Credit | 15 Mins | KES 2,890.20 | 64.1% |
| **Cell 4 (Candidate)** | **7 Days Credit** | **35 Mins** | **KES 4,633.28** | **78.4%** |

* **Model Diagnostics:** Overall RSM Model $R^2 \approx 0.7513$, $F\text{-statistic } p \approx 0.0002$, Lack of Fit $p \approx 0.7766$.
* **Estimated Effects:** 35-min visit duration (+KES 3,512.78 vs. 15 min, $p \approx 0.1151$); 7-day credit (+KES 2,408.10 vs. Cash, $p \approx 0.2705$).

---

## Act VII: The Real Business Decision (6-Month Validation)

The project does not end with a simulated profiler. The candidate operating condition (**7 Days Credit + 35-Minute Visit Duration for Medium/Large Accounts**) is currently deployed across Kilifi routes for a **6-month real-world market validation period**.

```text
                           SIX-MONTH FIELD VALIDATION CADENCE
  ┌──────────────────┐     ┌───────────────────┐     ┌──────────────────┐     ┌──────────────────┐
  │  MAP & ROUTE     │ ──► │     EXECUTE       │ ──► │  MEASURE WEEKLY  │ ──► │  RE-EVALUATE     │
  │ Territory Plans  │     │ 7-Day / 35-Min    │     │ Revenue, RPV,    │     │ Adjust Terms &   │
  │ Rep Assignments  │     │ Commercial Policy │     │ Conversion Rate  │     │ Scalability      │
  └──────────────────┘     └───────────────────┘     └──────────────────┘     └──────────────────┘
```

### Table 6: Six-Month Validation KPI Framework

| KPI Domain | Target Metric | Baseline Value | Validation Target | Monitoring Frequency |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Commercial** | Revenue Per Visit (RPV) | KES 1,767.30 | $\ge$ KES 2,800.00 | Weekly route audit |
| **Commercial Yield** | Conversion Rate | 58.41% | $\ge$ 65.00% | Daily rep submission |
| **Account Growth** | Large/Medium Orders | 38.2% of orders | $\ge$ 50.0% of orders | Bi-weekly summary |
| **Operational Control**| Credit Default Rate | 0.00% (Cash era) | $\le$ 2.50% total AR | Monthly finance audit |
| **Logistics Health** | Stockout Days | 68 days | $\le$ 15 days | Weekly warehouse log |

---

## Act VIII: Broader Business Impact & Auxiliary Benefits

Beyond the commercial experiment, establishing operational discipline unlocked capabilities across the enterprise:

1. **Standard Operating Procedures (SOPs):** Drafted formal SOPs for field sales pitching, delivery routing, and warehouse inventory management.
2. **Management Control Cadence:** Replaced ad-hoc meetings with a weekly KPI review driven by audited workbook dashboards.
3. **Territory Rationalization:** Established route mapping across Kilifi North, Kilifi South, Malindi, Kaloleni, Ganze, and Magarini.
4. **Supply Chain Synchronization:** Linked sales visit forecasts to warehouse replenishment triggers, targeting a reduction in the 26 baseline stockout incidents.

---

## Repository Navigation & Documentation Index

```text
03-FMCG-Commercial-Optimization-Kilifi/
├── README.md                          # Master Case Study Landing Page (This File)
├── docs/                              # Executive Documentation Suite
│   ├── 01-executive-summary.md        # Executive Brief & Context
│   ├── 02-problem-statement.md        # Deep Operational Problem Framing
│   ├── 03-eda-findings.md             # Baseline EDA & Funnel Audit
│   ├── 04-segmentation-chaid.md       # CHAID Decision Tree & Segmentation
│   ├── 05-doe-design-matrix.md        # 2x2 Experimental Design Specs
│   ├── 06-factorial-analysis.md       # Factorial Regression Findings
│   ├── 07-response-surface-modeling.md# Response Surface Fitting & Profiling
│   ├── 08-optimization.md             # Desirability Profiler Optimization
│   ├── 09-six-month-validation.md     # 6-Month Field Validation Roadmap
│   ├── 10-business-impact.md          # Enterprise Capabilities & SOPs
│   ├── methodology.md                 # Appendix A: Analytical Methodology
│   ├── limitations.md                 # Appendix B: Methodological Limitations
│   ├── data-dictionary.md             # Appendix C: 20-Domain Schema Guide
│   └── visual-index.md                # Appendix D: Catalog of Figures & Plots
├── data/                              # Data Storage & Generation Engine
│   ├── dataset_summary.md             # Schema Metadata Reference
│   ├── kilifi_sales_visits_baseline.csv# Audited Visit Dataset (N=6,591)
│   └── generate_dataset.py            # Dataset Synthesizer Script
├── analysis/                          # Analytics & Modeling Pipeline
│   ├── README.md                      # Pipeline Execution Guide
│   ├── 01_eda_and_screening.py        # Baseline EDA & Screening Script
│   ├── 02_commercial_driver_models.py # OLS & Logistic Regression Script
│   └── 03_doe_rsm_optimization.py    # RSM & Desirability Profiler Script
├── jmp/                               # JMP Scripting & DOE Automation
│   ├── README.md                      # JMP Asset Reference
│   ├── 01_custom_doe_design.jsl       # 32-Run Design Script
│   └── 02_rsm_profiler_fit.jsl        # Response Surface Profiler Script
└── reports/                           # Executive Briefs & Slide Summaries
    ├── README.md                      # Reports Reference
    └── executive_brief_kilifi_optimization.md # C-Suite Briefing
```
