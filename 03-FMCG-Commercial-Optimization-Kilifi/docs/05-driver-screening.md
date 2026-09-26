# Chapter 05: Multivariate Driver Screening & Factor Pruning

> **Executive Takeaway:** Statistical screening separates true operational performance drivers from noise. Multivariate ANOVA and Logistic Regression confirmed that customer `size_tier` and `shop_type` drive commercial outcomes, while operational variables like sales rep prior experience and delivery vehicle assignment have no statistically significant impact and were pruned.

---

## 1. Driver Screening Methodology

To move from exploratory insights to rigorous experimental design, we evaluated the baseline dataset ($N=6,591$ visits) using multivariate regression modeling in JMP and Python.

The goal of driver screening was twofold:
1. **Identify Statistically Significant Factors**: Determine which operational, geographic, and store variables drive variance in `order_total_kes` and `Order_conversion`.
2. **Prune Non-Performing Levers**: Eliminate non-significant variables prior to constructing our $2^2$ factorial Design of Experiments (DOE), ensuring experimental resources focus exclusively on high-impact controllable levers.

---

## 2. Order Revenue Screening (`order_total_kes`)

We fitted an Analysis of Variance (ANOVA) model evaluating order total revenue across converted transactions ($N=3,846$):

$$\text{order\_total\_kes} = \beta_0 + \beta_1(\text{size\_tier}) + \beta_2(\text{shop\_type}) + \beta_3(\text{fmcg\_exp\_yrs}) + \beta_4(\text{vehicle\_type}) + \varepsilon$$

### ANOVA & Parameter Estimates Summary

| Factor / Source | Degrees of Freedom (DF) | Sum of Squares | F Ratio | p-Value ($p$) | Significance Status |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **`size_tier`** | 2 | $1.428 \times 10^{10}$ | $2,142.15$ | **$< 0.0001$** | **Statistically Significant** |
| **`shop_type`** | 5 | $8.412 \times 10^8$ | $50.48$ | **$< 0.0001$** | **Statistically Significant** |
| **`fmcg_exp_yrs`** | 1 | $1.241 \times 10^6$ | $0.37$ | **$0.5421$** | *Not Significant (Pruned)* |
| **`vehicle_type`** | 1 | $8.950 \times 10^5$ | $0.27$ | **$0.6034$** | *Not Significant (Pruned)* |

```text
                               EFFECT SUMMARY LOG LIKELIHOOD / F RATIO
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ size_tier             ████████████████████████████████████████████████ (p < 0.0001)       │
│ shop_type             ████████████████ (p < 0.0001)                                       │
│ fmcg_exp_yrs          █ (p = 0.5421 - Insignificant)                                      │
│ vehicle_type          █ (p = 0.6034 - Insignificant)                                      │
└───────────────────────────────────────────────────────────────────────────────────────────┘
Figure 6: Parameter effect summary chart showing log-worth significance for primary commercial predictors.3. Conversion Probability Screening (Order_conversion)To evaluate binary conversion (Converted = 1, Declined = 0) across all 6,591 pitch visits, we constructed a Nominal Logistic Regression model:$$\text{logit}(P(\text{Conversion})) = \ln\left(\frac{P}{1-P}\right) = \alpha_0 + \alpha_1(\text{shop\_type}) + \alpha_2(\text{size\_tier}) + \alpha_3(\text{visit\_duration\_min})$$Nominal Logistic Regression SummaryPredictorLikelihood Ratio Chi-Square (χ2)Degrees of Freedomp-Value (p)Commercial Interpretationshop_type$412.84$5$< 0.0001$Outlet format is the primary determinant of pitch conversion.size_tier$28.14$2$< 0.0001$Account size secondary effect on decision-maker willingness to buy.visit_duration_min$6.81$1$0.0091$Pitch time allocation impacts closing probability.fmcg_exp_yrs$0.45$1$0.5023$Prior sales rep tenure does not predict visit conversion.4. Hypothesis Pruning MatrixBased on statistical screening thresholds ($\alpha = 0.05$), operational hypotheses were formally evaluated for inclusion in subsequent experimental design:Tested HypothesisVariable EvaluatedStatistical OutcomeStrategic DecisionH1: Store Size ScaleCustomer size_tier$p < 0.0001$ (Significant)Retain as Blocking Factor in DOE.H2: Channel Format VelocityOutlet shop_type$p < 0.0001$ (Significant)Retain as Blocking Factor in DOE.H3: Sales Rep Experiencefmcg_exp_yrs$p = 0.5421$ (Insignificant)Prune from experimental design.H4: Delivery Fleet Typevehicle_type$p = 0.6034$ (Insignificant)Prune from experimental design.H5: Pitch Time Allocationvisit_duration_min$p = 0.0091$ (Significant)Retain as Controllable Factor in DOE.Key Takeaway: Management previously believed hiring senior representatives with more FMCG experience (fmcg_exp_yrs) was essential for market penetration in Kilifi. Screening proved experience had no statistical effect on transaction volume or conversion probability once outlet channel and store size were controlled.5. Strategic Implication & Next StepsWith non-performing variables pruned, we focus our experimental efforts on controllable levers: Pitch Duration (visit_duration_min) and Credit Terms (credit_terms).We now proceed to formulate a custom $2^2$ Factorial Design of Experiments (DOE) in JMP, blocking across store size and channel format to isolate optimal operational settings for The Client.
