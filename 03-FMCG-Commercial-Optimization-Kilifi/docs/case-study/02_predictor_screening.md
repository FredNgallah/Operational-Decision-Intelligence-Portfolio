# Predictor Screening & Grain Directory

## Overview
To isolate key variables across the business, predictor screening was conducted across six distinct analytical grains (Grains 1–6). Each grain isolates a specific operational level, from order totals down to individual stockouts and inventory balances.

---

## Predictor Screening Summary Table

| Grain | Scope / Dataset | Response Variable | Top Ranked Predictors | Contribution (%) | Key Insight |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Grain 1** | Order Level (`30_Orders`) | `order_total_kes` | 1. `size_tier`<br>2. `shop_type`<br>3. `credit_terms` | **92.5%**<br>3.1%<br>1.7% | Physical outlet scale dominates revenue contribution. |
| **Grain 2** | Line Item SKU (`16_daily_sales`) | `line_amount_kes` | 1. `unit_price_kes`<br>2. `unit_cost_kes`<br>3. `pack_size_ml` | **50.8%**<br>45.8%<br>2.6% | Product price tiering dictates transaction line values. |
| **Grain 3** | Visit Level (`17_Daily_Visits`) | `Order conversion` | 1. `visit_duration_min`<br>2. `shop_type`<br>3. `distance_km` | **35.8%**<br>16.9%<br>12.2% | Channel type and time spent correlate most strongly with conversion probability. |
| **Grain 4** | Delivery Level (`18_Delivery_Log`) | `delay_days` | 1. `order_total_kes`<br>2. `route_id`<br>3. `item_count` | **66.5%**<br>11.9%<br>9.0% | Heavy order payloads directly increase fulfillment delays. |
| **Grain 5** | Stockout Level (`29_Stockouts`) | `duration_days` | 1. `category`<br>2. `cause`<br>3. `shelf_life_days` | **81.2%**<br>13.5%<br>5.4% | Category supply chain dynamics dictate stock replenishment speed. |
| **Grain 6** | Inventory Level (`20_Inventory`) | `spoiled_units` | 1. `opening_stock_units`<br>2. `closing_stock_units`<br>3. `sold_units` | **61.6%**<br>30.2%<br>2.6% | Total volume on hand drives unit spoilage far more than temperature. |

---

## Detailed Notes by Grain

### Grain 1: Order Level
* **Sample Size ($N$):** 3,846
* **Key Finding:** Non-linear differences between `size_tier` groups mean pricing/discount strategies must be tiered strictly by store size.

### Grain 3: Visit Level
* **Sample Size ($N$):** 6,591
* **Key Finding:** While `visit_duration_min` tops predictor ranking for overall variation, conversion models show duration alone does not guarantee a sale ($p = 0.8142$). Focus must remain on outlet profiling (`shop_type`).

### Grain 6: Inventory Level
* **Key Finding:** Stock movement velocity (`sold_units` vs `opening_stock_units`) is the primary lever for reducing product spoilage.
