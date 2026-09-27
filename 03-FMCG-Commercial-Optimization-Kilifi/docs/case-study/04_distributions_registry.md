# Univariate & Bivariate Distribution Registry

## Financial Metrics Summary (KES)

### Order Values (`order_total_kes`)
* **Mean:** KES 3,030.38
* **Std Dev:** KES 3,388.12
* **Median:** KES 1,732.00
* **25th Percentile:** KES 885.00
* **75th Percentile:** KES 3,920.00
* **Maximum:** KES 32,910.00

### Gross Margin & Revenue
* **Gross Margin % (`gross_margin_pct`):**
  * **Mean:** 36.75%
  * **Median:** 37.20%
  * **Std Dev:** 4.12%
* **Net Contribution Relationship:**
  $$\text{Net Contribution (KES)} = -147.05 + 0.3691 \times \text{Revenue (KES)}$$
  * **Fit Strength:** $R^2 = 0.978$

---

## Operational & Logistic Metrics

### Field Visits (`visit_duration_min`)
* **Mean Duration:** 9.52 minutes
* **Std Dev:** 3.11 minutes
* **Outcome Comparison:**
  * **Order Converted Mean:** 9.54 minutes
  * **No Order Mean:** 9.50 minutes
  * **ANOVA Test:** $F = 0.055$, $p = 0.8142$ (No statistically significant difference)

### Delivery Delays (`delay_days`)
* **Mean Delay:** 0.146 days
* **On-Time Rate:** 97.6% of deliveries incur 0 delay days.
* **Delay Distribution:**
  * **0 Days:** 97.6%
  * **1 Day:** 1.8%
  * **2+ Days:** 0.6%

### Cold Chain Monitoring (`cold_chain_temp_excursion`)
* **Overall Excursion Rate:** 2.38% of tracked movements exceed temperature thresholds.
* **Vehicle Comparison:** No statistically significant difference between vehicle units V01 and V02 ($\chi^2 = 0.824$, $p = 0.364$).

---

## Baseline Lookup Targets for Future Benchmarking
1. **Order Target Baseline:** Maintain average order value above **KES 3,000** across all mid-tier routes.
2. **Delivery Target:** Maintain delay occurrence under **2.5%** of total deliveries.
3. **Margin Floor:** Maintain threshold gross margins above **35.0%** across core SKU bundles.
