# FMCG Commercial Optimization & Experimental Design: Kilifi Market Expansion

**Client:** A major dairy business, expanding to the Kilifi (Coast) market after establishing operations in Meru Kenya.  
**Domain:** FMCG / Commercial Operations / Field Sales Analytics  
**Methodology:** Operational Standardization, Exploratory Data Analysis, Multivariate Driver Screening, Custom $2^2$ Factorial Design of Experiments (DOE), Multi-Response Prediction Profiler Optimization  
**Tooling:** JMP, Python, Operational Data Architecture  

---

## Executive Summary

When the client. expanded its yogurt line into Kilifi County, field operations faced severe structural opacity. A team of 5 sales representatives and 2 vehicles operated without defined territory boundaries, pitching products via paper brochures to arbitrary retail outlets based on gut feel.

This case study documents the transformation of an unstructured, opaque market expansion into a measurable, evidence-based commercial growth engine. By deploying a 20-domain operational data capture system, we audited 6,591 sales visits, isolated core commercial drivers, designed a custom $2^2$ factorial DOE in JMP, and established candidate operating settings optimized for both transaction scale and conversion probability.

```text
[Operational Chaos] ──► [System Standardization] ──► [Driver Screening] ──► [Custom DOE & Profiling] ──► [6-Month Field Validation]
 Ad-hoc pitches &        20-domain data capture       Isolated scale vs.        Simulated optimum:         Live market testing
 intuitive routes        system (6,591 visits)        conversion drivers        7D Credit / 35m Visit      across Kilifi County

# Kilifi Field Sales Analytics & Optimization

**From zero operational visibility to a data-driven commercial operating model — baseline audit, driver analysis, experimental design, and a live six-month field validation plan.**

![Status](https://img.shields.io/badge/status-field%20validation%20active-yellow)
![Data](https://img.shields.io/badge/baseline-Jan–Jun%202026-blue)
![Tooling](https://img.shields.io/badge/modeling-JMP%20DOE-lightgrey)

---

## Key Baseline Metrics

| Metric / Dimension | Baseline Value (Jan 1 – Jun 30, 2026) | Strategic / Analytical Significance |
|---|---|---|
| Field Execution Scope | 6,591 Sales Visits | Baseline sales pitch opportunities captured |
| Sales Conversion | 3,846 Orders (58.41% Conversion) | Baseline visit-to-order closing efficiency |
| Audited Revenue | KES 11,648,320 Net Sales | Total order-level revenue baseline |
| Field Constraints | 5 Sales Reps / 2 Vehicles | Fixed operational resource allocation |
| Primary Scale Driver | Customer `size_tier` (p < 0.0001) | Accounts for primary variance in order value |
| Primary Conversion Driver | Outlet `shop_type` (p = 0.0091) | Dictates binary visit closing probability |
| Candidate DOE Levers | 7-Day Credit + 35-Min Visit Duration | Model-predicted settings for field validation |

---

## Act I — The Business Problem: Expansion Without Visibility

The initial challenge in Kilifi was not simply "low sales" — it was a complete lack of operational structure and visibility:

- **Zero Execution Visibility** — Leadership lacked data on sales force time allocation, store visit outcomes, route productivity, and delivery cold-chain integrity.
- **Unstructured Field Operations** — Sales representatives conducted random, unmapped store visits, offering arbitrary pitches without commercial guardrails.
- **Unclear Growth Levers** — Management could not determine whether revenue bottlenecks stemmed from low closing rates or small order sizes.

> **Core Philosophy:** We did not start by optimizing the business. We first made the business measurable.

---

## Act II — Making the Operation Measurable

We built and deployed an integrated operational data capture system spanning **20 operational domains** — linking visits, orders, inventory movements, logistics, time tracking, and customer feedback.

\`\`\`
                               FIELD OPERATIONS (5 Reps / 2 Vehicles)
                                                 │
                                                 ▼
                              20-DOMAIN OPERATIONAL DATA CAPTURE SYSTEM
                                                 │
            ┌────────────────────────────────────┼────────────────────────────────────┐
            ▼                                    ▼                                    ▼
    [Sales Visits Table]                 [Orders & Line Items]                [Logistics & Inventory]
    • 6,591 Pitch Records                • 3,846 Orders                       • 1,807 Delivery Logs
    • Duration & Conversion              • KES 11.65M Net Revenue             • Stockouts & Spoilage
            │                                    │                                    │
            └────────────────────────────────────┼────────────────────────────────────┘
                                                 ▼
                                     AUDITED BASELINE DATABASE
\`\`\`

---

## Act III — What the Baseline Data Revealed

Exploratory analysis across 6,591 visits revealed that commercial performance is governed by two distinct mechanisms:

1. **Transaction Scale is Segment-Driven** — Order value (`order_total_kes`) is heavily dictated by customer `size_tier` (p < 0.0001). Large store tiers generate **+KES 11,087.37** over model averages.
2. **Conversion Velocity is Channel-Driven** — Binary conversion (`Order_conversion`) is dictated by outlet format (`shop_type`, p = 0.0091). Formats like Kiosks and Mini-Marts convert reliably, whereas Hotels/Resorts fail to convert consistently.

**Hypothesis Pruning:** Operational factors such as sales rep prior FMCG experience and delivery vehicle type showed no statistically significant relationship with sales revenue and were dropped prior to experimental design.

---

## Act IV — Experimental Design & Optimization (JMP 2² Custom DOE)

To evaluate controllable commercial levers, we constructed a custom **N = 32** design in JMP, stratifying across store context:

- **Factor 1** (`credit_terms`): Cash vs. 7 Days Credit
- **Factor 2** (`visit_duration_min`): 15 Minutes vs. 35 Minutes
- **Blocking Context**: `shop_type` (6 levels) and `size_tier` (3 levels)

> **Note:** Experimental responses were generated synthetically in JMP to demonstrate the multi-response optimization framework. Results represent model-based hypotheses for field validation.

### Simulated Prediction Profiler

| `credit_terms` | `visit_duration_min` | Model-Predicted Output |
|---|---|---|
| Cash → **7 Days** (Lift: +KES 2,408.10, p = 0.2705) | 15 min → **35 min** (Lift: +KES 3,512.78, p = 0.1151) | Revenue/Visit: Max Lift · Conversion Rate: Maintained |

### Simulated Model Results Summary

- `revenue_per_visit` Model: **R² = 0.7513**, Adjusted **R² = 0.6329**, **p = 0.0002**
- **Candidate Settings:** The JMP Prediction Profiler identified **7-Day Credit combined with 35-Minute Visit Durations** as the candidate operating condition to maximize revenue per visit without degrading closing rates.

---

## Act V — Six-Month Real-World Validation Plan

The project transitions from simulated modeling to live market testing across Kilifi County:

\`\`\`
  [Map & Segment] ──► [Prioritize Routes] ──► [Deploy 7D / 35m Levers]
         ▲                                                │
         │                                                ▼
  [Refine Strategy] ◄─── [Evaluate Outcomes] ◄─── [Track Weekly KPIs]
\`\`\`

- **Route Prioritization** — Align sales schedules to Large and Medium accounts within high-converting channels (Mini-Marts, Kiosks).
- **Time Allocation** — Enforce 35-minute structured pitches for priority accounts; cap cold prospecting at 15 minutes.
- **Credit Governance** — Extend 7-day credit selectively to Large accounts with verified purchase history, enforcing a 1.5% default threshold.

---

## Enabling Organizational Capabilities

In addition to analytical models, the project delivered foundational standard operating procedures (SOPs):

- **Field Sales SOP** — Standardized pitch routines, visit duration caps, and daily logging workflows.
- **Warehouse & Inventory SOP** — Standardized stock ledger, replenishment triggers, and spoilage tracking.
- **Commercial Terms SOP** — Credit allocation matrix decoupling credit approval from individual rep discretion.

---

## Repository Documentation Index

| Document | Description |
|---|---|
| [`docs/01-business-problem.md`](docs/01-business-problem.md) | Market Context & Operational Baseline |
| [`docs/02-data-foundation.md`](docs/02-data-foundation.md) | 20-Domain Architecture & Workbook Design |
| [`docs/03-data-quality.md`](docs/03-data-quality.md) | Audit, Sign Anomaly Resolution & Reconciliation |
| [`docs/04-eda.md`](docs/04-eda.md) | Baseline Sales Funnel & Segment Analysis |
| [`docs/05-driver-screening.md`](docs/05-driver-screening.md) | Multivariate Driver Reduction & Pruning |
| [`docs/06-doe-design.md`](docs/06-doe-design.md) | 2² Custom Experimental Design Formulation |
| [`docs/07-doe-results.md`](docs/07-doe-results.md) | Simulated DOE Regression & Logistic Models |
| [`docs/08-optimization.md`](docs/08-optimization.md) | JMP Prediction Profiler Candidate Settings |
| [`docs/09-six-month-validation.md`](docs/09-six-month-validation.md) | Live Field Testing & KPI Governance |
| [`docs/10-business-impact.md`](docs/10-business-impact.md) | Operational SOPs & Capability Framework |
| [`docs/methodology.md`](docs/methodology.md) | Statistical Equations & Technical Workflow |
| [`docs/limitations.md`](docs/limitations.md) | Dataset Boundaries & Analytical Constraints |
| [`docs/data-dictionary.md`](docs/data-dictionary.md) | Schema Definitions & Field Taxonomy |
| [`docs/visual-index.md`](docs/visual-index.md) | Complete Image & Graphic Catalog |

---

## Project Status

**Baseline audited · Custom DOE modeled · Field validation phase active**
