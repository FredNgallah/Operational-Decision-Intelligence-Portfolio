# Chapter 07: DOE Experimental Results & Regression Modeling

> **Executive Takeaway:** Fitting Least Squares and Logistic Regression models on the custom $N=32$ DOE dataset reveals that both
>  7-Day Credit and 35-Minute Pitch Durations generate positive revenue lifts. While main effects are strong, their combined interaction shows that credit acts as a major catalyst when paired with sufficient pitch time.

---

## 1. Response Surface Model Fit & Summary of Fit

We evaluated response surface models across the custom 32-run factorial design to model revenue per visit (`revenue_per_visit`) and 
visit-to-order 
conversion (`Order_conversion`) as functions of controllable levers, while controlling for store context (`shop_type` and `size_tier`).

*Note: Experimental responses were generated synthetically in JMP to demonstrate the multi-response optimization framework prior to live market 
validation.*

### Model Fit Metrics (`revenue_per_visit`)

$$\text{revenue\_per\_visit} = \beta_0 + \beta_1(\text{credit\_terms}) + \beta_2(\text{visit\_duration\_min}) + 
\beta_{12}(\text{credit\_terms}\times \text{visit\_duration\_min}) + \text{Blocks} + \varepsilon$$

| Metric | Model Value | Statistical Interpretation |
| :--- | :---: | :--- |
| **R-Square ($R^2$)** | **0.7513** | Explains $75.13\%$ of total revenue variance per visit across treatment runs. |
| **Adjusted R-Square ($R^2_{\text{adj}}$)** | **0.6329** | Robust model fit after accounting for model degrees of freedom. |
| **Root Mean Square Error (RMSE)** | **KES 1,842.10** | Standard deviation of model residuals across experimental runs. |
| **Mean Response** | **KES 3,840.25** | Average modeled revenue per visit across all DOE treatment combinations. |
| **Model ANOVA F-Ratio** | **6.3412** | Model overall statistical significance. |
| **Model p-Value ($p$)** | **0.0002** | Statistically significant relationship between factors and revenue outcome. |

---

## 2. Parameter Estimates & Treatment Effects

The Least Squares parameter estimates isolate the main effects and two-factor interaction of our controllable levers:

| Term | Estimate (KES) | Std Error | t Ratio | p-Value ($p$) | Statistical Status |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Intercept** | $3,840.25$ | $325.60$ | $11.79$ | $< 0.0001$ | Statistically Significant |
| **`credit_terms[7 Days]`** | $+1,204.05$ | $381.20$ | $3.16$ | **$0.0047$** | **Statistically Significant** |
| **`visit_duration_min[35]`** | $+1,756.39$ | $381.20$ | $4.61$ | **$0.0002$** | **Statistically Significant** |
| **`credit_terms[7 Days]` $\times$ `visit_duration_min[35]`** | $+645.80$ | $381.20$ | $1.69$ | **$0.1042$** | 
*Directional Lift (Marginal)* |

```text
                               PARAMETER ESTIMATES & EFFECT SIZES
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ visit_duration_min [35 vs. 15]   ██████████████████████████ (+KES 1,756.39, p=0.0002)     │
│ credit_terms [7 Days vs. Cash]   ██████████████████ (+KES 1,204.05, p=0.0047)             │
│ credit_terms * duration          █████████ (+KES 645.80, p=0.1042)                        │
└───────────────────────────────────────────────────────────────────────────────────────────┘
Figure 8: Parameter estimate effect sizes showing main effects and interaction lifts for Credit Terms and Visit Duration

## 3.Interaction Analysis: Credit Terms $\times$ Visit Duration
The interaction plot reveals a critical operational dynamic between pitch duration and credit terms:
1. Short Pitch (15 Minutes): Offering 7-Day Credit provides only a minor revenue lift ($+\text{KES } 558.25$) when sales pitches are rushed.
2. Extended Pitch (35 Minutes): Offering 7-Day Credit during a structured 35-minute pitch unlocks a substantial combined revenue lift ($+\text{KES }
 2,495.65$).
3. Operational Interpretation: Credit terms require adequate pitch time for sales reps to explain repayment terms, verify store
eligibility, and build sufficient retailer trust to expand order sizes.Plaintext

 INTERACTION PROFILE: REVENUE PER VISIT (KES)
  KES 6,000 ┬─────────────────────────────────────────────────────────── (7 Days Credit)
            │                                                      /
  KES 4,500 ┼─────────────────────────────────────────────────────/───── (Cash)
            │                                                  /
  KES 3,000 ┼─────────────────────────-------────────────────/
            │                       /
  KES 1,500 ┴──────────────────────/────────────────────────
                          15 Minutes                    35 Minutes
                                      VISIT DURATION
## 4. Conversion Probability Response (Order_conversion)
Nominal Logistic Regression was fitted to evaluate whether offering credit or extending
visit duration negatively impacted closing rates:

FactorOdds Ratio95% Confidence IntervalChi-Square (χ2)p-Value (p)credit_terms[7 Days]1.84$[1.18, 2.87]$7.14$0.0075$visit_duration_min[35]2.12$
[1.35, 3.32]$10.45$0.0012$

Key Finding: Neither factor reduced conversion rates.
In fact, offering 7-Day Credit increased the odds of closing an order by $84\%$ ($\text{Odds Ratio} = 1.84$), as store owners were significantly more willing to place initial yogurt orders when immediate cash outlay was not required.

## 5. Strategic Implication & Next Steps
The regression models demonstrate that both controllable levers drive positive commercial returns,
with no adverse impact on closing probability.We now proceed to Chapter 08 to run JMP's Multi-Response Prediction Profiler,
finding the precise joint candidate operating conditions that maximize revenue while maintaining strict credit risk controls for The Client.
