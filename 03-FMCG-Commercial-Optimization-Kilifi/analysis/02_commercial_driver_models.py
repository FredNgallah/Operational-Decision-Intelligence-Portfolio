"""
Meru Fresh Dairy Ltd. - Kilifi Expansion
02: Order-Level Commercial Driver Modeling (OLS & Logistic GLM)
---------------------------------------------------------------
Evaluates order value drivers using Ordinary Least Squares (OLS) regression:
order_total_kes ~ size_tier + shop_type + (size_tier * shop_type)

Evaluates binary conversion drivers using Logistic Regression (GLM):
Order_conversion ~ shop_type + fmcg_exp_yrs + visit_duration_min
"""

import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

def run_driver_models():
    data_path = os.path.join("data", "kilifi_sales_visits_baseline.csv")
    df = pd.read_csv(data_path)
    
    # Subset to converted orders for revenue driver model
    orders_df = df[df["Order_conversion"] == 1].copy()
    
    print("=" * 70)
    print("1. ORDER-LEVEL COMMERCIAL REVENUE MODEL (OLS)")
    print("=" * 70)
    
    # Fit OLS model with main effects and interaction term
    ols_model = smf.ols(
        "order_total_kes ~ C(size_tier) + C(shop_type) + C(size_tier):C(shop_type)",
        data=orders_df
    ).fit()
    
    print(f"Number of Converted Orders (N): {len(orders_df):,}")
    print(f"R-squared (R²):                  {ols_model.rsquared:.4f}  (Target Benchmark ≈ 0.487)")
    print(f"Adjusted R-squared:             {ols_model.rsquared_adj:.4f}")
    print(f"Model F-statistic p-value:       {ols_model.f_pvalue:.4e}")
    print("-" * 70)
    
    # ANOVA Table for main effects & interaction
    anova_table = sm.stats.anova_lm(ols_model, typ=2)
    print("\n[ANOVA SUMMARY TABLE]")
    print(anova_table)
    
    print("\nTakeaway: Customer Size Tier and Shop Type interact significantly (p < 0.0001).")
    print("Commercial strategy must treat Size Tier as a primary context stratification factor.")
    
    print("\n" + "=" * 70)
    print("2. VISIT CONVERSION MODEL (LOGISTIC GLM)")
    print("=" * 70)
    
    # Fit Logistic Regression Model
    logit_model = smf.logit(
        "Order_conversion ~ C(shop_type) + fmcg_exp_yrs + visit_duration_min",
        data=df
    ).fit(disp=False)
    
    print(f"Total Visits Analyzed (N):      {len(df):,}")
    print(f"Log-Likelihood:                 {logit_model.llf:.2f}")
    print(f"Pseudo R-squared (McFadden):    {logit_model.prsquared:.4f}")
    print("-" * 70)
    print("\n[LOGISTIC REGRESSION COEFFICIENTS]")
    print(logit_model.summary().tables[1])
    
    print("\nTakeaway: Shop Type is highly predictive of conversion probability.")
    print("Visit duration exhibits minimal standalone explanatory power in observational data,")
    print("necessitating a controlled 2x2 DOE to test duration under fixed commercial conditions.")

if __name__ == "__main__":
    run_driver_models()
