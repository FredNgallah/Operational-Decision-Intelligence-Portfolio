# Appendix B: Analytical Boundaries & Dataset Constraints

> **Executive Summary:** While the multi-response optimization framework provides actionable insights for commercial field strategy, several analytical, geographical, and data-inherent constraints apply. This document outlines these boundaries to ensure appropriate interpretation and risk governance during market deployment.

---

## 1. Synthetic Data & Simulation Constraints

To develop the multi-response optimization framework and DOE response surfaces prior to live field deployment, pilot responses were synthetically generated in JMP based on baseline transactional parameters.

* **Assumed Synergy**: The response surface assumes a positive interactive lift ($\beta_{12} = +\text{KES } 645.80$) between 35-minute pitch duration and 7-day credit terms. Actual field dynamics may exhibit non-linear saturation effects or behavioral variance among retail operators.
* **Controlled Noise**: Synthetic models enforce a standard error of $\sigma = \text{KES } 1,842.10$. Live field conditions may introduce higher variance due to external macroeconomic factors, local cash-flow cycles, or competitor promotions.

---

## 2. Geographic & Seasonal Scope Boundaries

The dataset and field parameters reflect retail dynamics specific to Kilifi County and coastal FMCG distribution environments:

```text
                           GEOGRAPHIC & SEASONAL BOUNDARIES
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ GEOGRAPHIC BOUNDS                                                                         │
│ • High density coastal urban centers (Malindi, Kilifi Town) vs. rural interiors            │
│ • Logistics access constraints vary by sub-county road network condition                  │
└─────────────────────────────────────────────┬─────────────────────────────────────────────┘
                                              │
                                              ▼
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ SEASONAL & TOURISM VARIANCE                                                               │
│ • High hospitality demand in HORECA during peak coastal tourist seasons (Aug, Dec)         │
│ • Agricultural income cycles impacting rural kiosk liquidity post-harvest                 │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

* **Regional Specificity**: Retail channel dynamics in Kilifi County (e.g., high density of resort/hotel accounts and rural micro-kiosks) may not directly generalize to inland urban centers like Nairobi or Nakuru without recalibrating baseline parameters.
* **Seasonality**: Experimental runs do not explicitly model macroeconomic shocks, fuel price spikes, or extreme weather disruptions (e.g., rainy season delivery delays).

---

## 3. Behavioral & Human Factor Assumptions

Field execution relies on human behavior and compliance from both sales representatives and retail shopkeepers:

1. **Rep Compliance**: Models assume sales representatives accurately log pitch durations, strictly adhere to assigned target route durations, and perform scheduled product audits without cutting corners.
2. **Credit Repayment Behavior**: Simulated default probabilities ($1.5\%$ target cap) rely on historical compliance in structured retail channels. Micro-kiosk repayment reliability under credit stress requires real-time monitoring during Phase 1 rollout.
3. **Product Perishability**: Cold-chain freshness for dairy products assumes baseline refrigeration capabilities at retail outlets. Outlets without reliable power grid connections may experience inventory spoilage independent of sales levers.

---

## 4. Risk Mitigation & Model Maintenance

To address these analytical limitations during live deployment, the following governance protocol is established:

| Boundary / Risk Area | Operational Risk | Mitigation & Governance Protocol |
| :--- | :--- | :--- |
| **Model Drift** | Changing retail liquidity conditions over time. | Re-estimate parameter estimates quarterly using live transaction logs. |
| **Credit Non-Payment** | Over-extension of credit to high-risk micro-kiosks. | Enforce hard 14-day default lockouts via mobile app system gates. |
| **Route Fatigue** | Rep burn-out from overly compressed visit schedules. | Conduct monthly rep feedback sessions to recalibrate route capacity. |
| **Cold-Chain Failure** | Product spoilage reducing retail reorder rates. | Implement mandatory temperature checks at dispatch and delivery points. |

---

## 5. Strategic Implication & Next Steps

Acknowledging these limitations ensures that candidate recommendations are treated as calibrated baseline hypotheses to be validated and refined during Phase 1 live market rollout.

---

*Next Appendix:* [`data-dictionary.md`](data-dictionary.md) — *Full 20-Domain Field Schema & Taxonomy.*
