# Chapter 08: Multi-Response Profiler Optimization & Candidate Operating Settings

> **Executive Takeaway:** Using JMP's Multi-Response Prediction Profiler and desirability functions, we identified optimal commercial settings that maximize revenue per visit while establishing strict credit risk controls across store segments.

---

## 1. Multi-Response Desirability Formulation

To move from regression models to actionable field execution rules, we configured a multi-response desirability framework in JMP. 

Rather than maximizing revenue in isolation, the optimization function balances revenue upside against credit risk exposure and rep time constraints:

$$\text{Overall Desirability } D = \left( d_1(\text{revenue}) \times d_2(\text{conversion}) \times d_3(\text{credit\_risk}) \right)^{\frac{1}{3}}$$

### Desirability Constraints & Objectives

1. **Revenue per Visit (`revenue_per_visit`)**: Maximize desirability ($d_1$) with a lower target bound of KES 2,500 and upper target of KES 10,000.
2. **Order Conversion Rate (`Order_conversion`)**: Maintain probability ($d_2$) $\ge 0.60$ across high-velocity retail channels.
3. **Credit Exposure (`credit_risk`)**: Constrain 7-Day Credit terms ($d_3$) exclusively to verified Large and Medium account size tiers to prevent non-performing debt in micro-kiosks.

```text
                               MULTI-RESPONSE PREDICTION PROFILER
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ REVENUE PER VISIT (KES)                                                                   │
│ KES 8,000 ┤                                                       /                       │
│ KES 4,000 ┤                             /------------------------/                        │
│ KES 1,000 ┴----------------------------/                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────┤
│ CONVERSION PROBABILITY                                                                    │
│     1.00  ┤                             /------------------------/                        │
│     0.50  ┤----------------------------/                                                  │
│     0.00  ┴───────────────────────────────────────────────────────────────────────────────┤
│                Cash                7 Days Credit     15 Minutes          35 Minutes       │
│                           CREDIT TERMS                            VISIT DURATION          │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

![Figure 9: JMP Multi-Response Prediction Profiler](../plots/fig-09-profiler.png)  
*Figure 9: JMP Multi-Response Prediction Profiler showing optimal trade-off curves for Credit Terms and Visit Duration.*

---

## 2. Segment-Specific Candidate Operating Settings

Optimization reveals that a one-size-fits-all sales strategy underperforms. Optimal candidate settings vary significantly by channel format and store scale:

| Outlet Channel (`shop_type`) | Account Scale (`size_tier`) | Recommended Credit Terms | Recommended Pitch Duration | Expected Revenue / Visit (KES) | Predicted Conversion (%) |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **Supermarket / Wholesaler** | **Large** | **7 Days Credit** | **35 Minutes** | **KES 12,450** | **68.5%** |
| **Mini-Mart** | **Medium** | **7 Days Credit** | **25 Minutes** | **KES 4,820** | **78.2%** |
| **Duka** | **Medium / Small** | **Cash / 3 Days** | **15 Minutes** | **KES 1,850** | **62.4%** |
| **Kiosk** | **Small** | **Strict Cash** | **10–15 Minutes** | **KES 820** | **71.0%** |
| **Hotel / Resort** | **Large / Medium** | **Pre-Approved Credit** | **35 Minutes** | **KES 6,200** | **45.0%** |

---

## 3. Monte Carlo Risk & Sensitivity Simulation

To test the robustness of candidate settings under real-world market volatility, we executed a 10,000-run Monte Carlo simulation in Python/JMP across the optimization surface.

### Key Simulation Findings

* **Downside Revenue Protection**: Under candidate settings, $95\%$ of field visits to Medium/Large accounts yield at least KES 3,200 per visit, compared to a baseline 5th-percentile yield of KES 1,100.
* **Credit Risk Sensitivity**: Unrestricted credit rollout to Small-tier kiosks increases predicted 30-day default probability by $14.2\%$, validating our recommendation to restrict credit terms to vetted accounts.
* **Time Allocation Efficiency**: Capping pitch duration at 15 minutes for Small kiosks frees up an estimated **1.8 sales hours per rep daily**, enabling reps to complete 3 additional high-value visit pitches per route.

```text
                        MONTE CARLO SIMULATED REVENUE DISTRIBUTION
  Frequency
    ┌─────────────────────────────────────────────────────────────────────────────────┐
    │                                              ▲                                  │
    │                                             ███                                 │
    │                                            █████                                │
    │                                           ███████                               │
    │                                          █████████                              │
    │                                         ███████████                             │
    │                                     █████████████████                           │
    └─────────────────────────────────────────────────────────────────────────────────┘
    KES 0                   KES 2,500             KES 5,000             KES 10,000+
                                   Simulated Revenue per Visit
```

![Figure 10: Monte Carlo Risk Simulation Distribution](../plots/fig-10-monte-carlo.png)  
*Figure 10: Simulated revenue outcome distribution under optimized candidate settings demonstrating downside protection.*

---

## 4. Operational Governance & Guardrails

To ensure field execution matches theoretical optimization, candidate operating rules must be enforced through system guardrails:

1. **Automated Credit Eligibility Gates**: The mobile sales tool automatically locks 7-Day Credit options for accounts flagged as `Small` tier or with unpaid balances exceeding 14 days.
2. **Dynamic Pitch Timers**: Route navigation software schedules 35-minute allocations for Large/Medium visits while compressing Small kiosk routes to rapid 15-minute reorder stops.
3. **Audit Triggers**: Any visit exceeding 45 minutes or overriding credit terms generates an automated compliance review flag for territory management.

---

## 5. Strategic Implication & Next Steps

Multi-response optimization provides The Client with a mathematically backed, segment-differentiated operating playbook.

---

*Next Chapter:* [`09-six-month-validation.md`](09-six-month-validation.md) — *Live Field Testing & KPI Governance.*
