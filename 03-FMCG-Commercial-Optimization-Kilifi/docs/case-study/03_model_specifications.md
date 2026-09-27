# Model Specifications & Parameter Documentation

## Path A: Order Value Fit Model (`order_total_kes`)

### Model Overview
* **Model Type:** Standard Least Squares Regression
* **Target Variable:** `order_total_kes`
* **Dataset:** Grain 1 (`30_Orders_Enriched`)

### Fit Statistics
| Metric | Value |
| :--- | :--- |
| **$R^2$** | 0.4870 |
| **$R^2_{\text{adj}}$** | 0.4852 |
| **Root Mean Square Error (RMSE)** | 2,436.74 |
| **Observations ($N$)** | 3,846 |

### Effect Summary
| Source | LogWorth | P-Value | F Ratio |
| :--- | :--- | :--- | :--- |
| `size_tier` | 300.00 | $< 0.00001$ | 1,344.54 |
| `shop_type` | 5.82 | $< 0.00001$ | 6.91 |
| `shop_type * size_tier` | 2.68 | 0.00210 | 2.77 |

---

## Path B: Spoilage Rate Fit Model (`spoilage_rate`)

### Model Overview
* **Model Type:** Standard Least Squares Regression
* **Target Variable:** `spoilage_rate`
* **Dataset:** Grain 6 (`20_Inventory_Enriched`)

### Fit Statistics
| Metric | Value |
| :--- | :--- |
| **$R^2$** | 0.00145 |
| **$R^2_{\text{adj}}$** | -0.00355 |
| **Root Mean Square Error (RMSE)** | 0.1612 |
| **Model P-Value** | 0.9777 |

### Technical Interpretation
The linear interaction model incorporating `cold_room_temp_c` and product `category` shows no statistically significant relationship with overall spoilage rate ($p > 0.05$). Spoilage should be analyzed using inventory velocity models (e.g., turnover rate) rather than ambient temperature parameters alone.

---

## Path C: Nominal Logistic Conversion Model (`Order conversion`)

### Model Overview
* **Model Type:** Nominal Logistic Regression
* **Target Variable:** `Order conversion` (1 = Order Placed, 0 = No Order)
* **Dataset:** Grain 3 (`17_Daily_Visits_Enriched`)

### Model Fit & Test Metrics
| Metric | Value |
| :--- | :--- |
| **Whole Model $\chi^2$** | 18.42 ($p = 0.0048$) |
| **Lack of Fit P-Value** | 0.9522 |
| **Observations ($N$)** | 6,591 |

### Parameter Estimates & Effect Likelihood
| Term / Source | DF | L-R $\chi^2$ | P-Value | Odds Ratio |
| :--- | :--- | :--- | :--- | :--- |
| `prior_fmcg_experience_years` | 1 | 4.12 | 0.0424 | 1.033 |
| `shop_type` | 5 | 16.84 | 0.0048 | N/A (Multi-level) |

### Key Odds Ratios
* **Hotel/Resort vs Duka:**
  * **Odds Ratio:** 1.538
  * **95% Confidence Interval:** $[1.238, 1.911]$
  * **P-Value:** 0.0001
