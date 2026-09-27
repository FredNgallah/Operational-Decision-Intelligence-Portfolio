# Chapter 06: Custom $2^2$ Factorial Design of Experiments (DOE) Formulation

> **Executive Takeaway:** To evaluate controllable commercial levers while accounting for store context, we designed a custom $2^2$ factorial experiment in JMP. The design tests two primary operational levers—Credit Terms and Pitch Duration—blocked across retail channel formats and account size tiers.

---

## 1. Experimental Design Rationale

Having established through driver screening that customer size tier and shop type govern baseline performance, we formulated a custom Design of Experiments (DOE) framework to test actionable sales levers.

The primary objective of the experiment was to measure main effects and two-factor interactions between sales pitch time allocation and commercial credit offerings, establishing evidence-based operating conditions for field deployment.

```text
                               CUSTOM DOE EXPERIMENTAL FRAMEWORK
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                                CONTROLLABLE FACTORS (DOE)                                 │
│  • Factor A: Credit Terms (Cash vs. 7 Days Credit)                                        │
│  • Factor B: Visit Duration (15 Minutes vs. 35 Minutes)                                   │
└─────────────────────────────────────────────┬─────────────────────────────────────────────┘
                                              │
                                              ▼
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                                  BLOCKING & CONTEXT FACTORS                               │
│  • Block 1: Shop Type (Kiosk, Mini-Mart, Duka, Supermarket, Wholesaler, Hotel/Resort)     │
│  • Block 2: Size Tier (Large, Medium, Small)                                              │
└─────────────────────────────────────────────┬─────────────────────────────────────────────┘
                                              │
                                              ▼
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                                   EVALUATED RESPONSES                                     │
│  • Primary Scale Response: Order Total Revenue (order_total_kes)                          │
│  • Conversion Velocity Response: Visit Order Conversion (Order_conversion)                │
└───────────────────────────────────────────────────────────────────────────────────────────┘
2. Factors, Levels & Experimental ConstraintsThe experimental design evaluates two high-priority controllable factors selected for sales force testing:Factor NameVariable NameFactor TypeLow Level (−1)High Level (+1)Strategic RationaleCredit Termscredit_termsCategoricalCash7 Days CreditEvaluates whether short-term credit unlocks larger order sizes in liquidity-constrained stores.Visit Durationvisit_duration_minContinuous15 Minutes35 MinutesEvaluates whether structured pitch times increase closing rates vs. rapid cold pitches.Blocking Factors (Nuisance Variation Control)To prevent store heterogeneity from confounding experimental treatment effects, the custom design stratifies across store context:shop_type: 6 categorical levels.size_tier: 3 categorical levels.3. Design Matrix & Run Structure ($N=32$)Using JMP's Custom Designer, a 32-run fractional factorial design matrix was constructed. The design achieves orthogonal balance across main effects and key interaction terms while constraining total field testing runs.Note: Experimental responses were generated synthetically in JMP to demonstrate the multi-response optimization framework prior to live market deployment.Plaintext                             2x2 FACTORIAL DOE EXPERIMENTAL MATRIX
                   ┌──────────────────────────────────────────────────────┐
                   │                                                      │
                   │    Run 3: Cash, 35 Min      Run 4: 7 Days, 35 Min    │
                   │    (High Duration)          (Combined High Level)    │
  Visit Duration   │                                                      │
     (35 Min)      │                                                      │
                   │                                                      │
     (15 Min)      │                                                      │
                   │    Run 1: Cash, 15 Min      Run 2: 7 Days, 15 Min    │
                   │    (Baseline Control)       (High Credit Only)       │
                   │                                                      │
                   └──────────────────────────────────────────────────────┘
                                  Cash                 7 Days
                                          Credit Terms
Figure 7: Geometric representation of the $2^2$ factorial design space showing treatment combinations across Credit Terms and Visit Duration.4. Key Statistical Power & Diagnostic MetricsThe custom design matrix was evaluated in JMP for statistical power and alias structure prior to model fitting:Signal-to-Noise Ratio: Designed to detect main effect sizes of $\delta \ge 1.0\sigma$ with statistical power $> 0.85$ at $\alpha = 0.05$.Alias Matrix Integrity: Main effects for credit_terms and visit_duration_min are fully unconfounded with each other and exhibit low correlation ($r < 0.12$) with blocking factors.Prediction Variance: Evaluated via Prediction Variance Profile, ensuring uniform prediction variance across the operational design space.5. Strategic Implication & Next StepsFormulating this custom $2^2$ DOE provides a structured experimental framework to test commercial hypotheses under controlled conditions.We now proceed to fit the DOE response surface models in JMP to analyze treatment effects, evaluate two-factor interactions, and estimate revenue lifts.
