# Executive Summary & Operational Recommendations

## Overview
This case study evaluates FMCG sales operations, distribution efficiency, inventory stability, and order conversions across six analytical grains. Using statistical modeling and predictor screening in JMP, the objective is to isolate operational drivers, optimize route performance, and improve sales conversion rates.

---

## Key Statistical Findings

### 1. Order Value Drivers (Grain 1)
* **Primary Driver:** Outlet `size_tier` explains over **92.5%** of the variance in total order value (`order_total_kes`).
* **Scale Differences:** Large outlets average **KES 6,675.77** per order, compared to Small outlets at **KES 885.99**.
* **Secondary Drivers:** `shop_type` (3.1%) and `credit_terms` (1.7%) exert minor influence compared to physical store size.

### 2. Conversion Insights (Grain 3)
* **Channel Performance:** Order conversion odds are highest in `Hotel/Resort` channels compared to traditional `Duka` outlets ($\text{Odds Ratio} = 1.538$, $p = 0.0001$).
* **Sales Rep Experience:** Prior FMCG experience shows a statistically significant positive effect ($\chi^2 = 4.12$, $p = 0.0424$), adding a ~3.3% increase in conversion odds per year of experience.
* **Visit Duration:** Average visit duration is uniform across successful and unsuccessful visits (~9.5 minutes, $p = 0.8142$), indicating visit length alone does not drive conversions.

### 3. Supply Chain & Logistics Delays (Grain 4)
* **Payload Impact:** Delivery delays (`delay_days`) are primarily driven by overall order size (`order_total_kes`, 66.5% contribution).
* **Route Variance:** Specific routes (RT03 and RT04) carry significantly higher mean order totals and encounter higher delivery delay variance compared to RT07 and RT09.

### 4. Spoilage & Cold Chain Performance (Grains 5 & 6)
* **Spoilage Predictors:** Inventory volume balances (`opening_stock_units` at 61.6% and `closing_stock_units` at 30.2%) drive unit spoilage significantly more than ambient or cold room temperature variance.
* **Linear Spoilage Model:** Temperature interactions ($p = 0.9777$) show negligible linear predictive power on percentage spoilage rates, indicating spoilage is driven by holding time and stock rotation rather than minor thermal fluctuations.

---

## Operational Recommendations

1. **Tiered Field Rep Allocation:** Reallocate senior sales representatives (high FMCG experience) to high-volume `Hotel/Resort` channels and Large `size_tier` accounts to maximize conversion values.
2. **Route Payload Balancing:** Split deliveries on high-volume routes (RT03, RT04) to reduce vehicle payload bottlenecks and decrease delivery delay days.
3. **Inventory Rotation Protocols:** Shift focus from temperature tuning to strict First-In, First-Out (FIFO) inventory controls and stock holding limits to mitigate spoilage losses.
