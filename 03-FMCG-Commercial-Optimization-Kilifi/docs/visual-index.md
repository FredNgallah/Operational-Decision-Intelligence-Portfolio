# Appendix D: Visual Index & Chart Catalog

> **Executive Summary:** This visual index serves as a comprehensive catalog of all figures, profilers, decision trees, and diagnostic plots embedded across the Kilifi Commercial Optimization Case Study. It details the underlying plot specs, data sources, and analytical takeaways for each visualization.

---

## 1. Catalog of Case Study Visualizations

| Figure # | Title & Description | Chapter / Section | Relative Path in Repository | Primary Visual Type |
| :---: | :--- | :--- | :--- | :--- |
| **01** | **EDA Variable Correlation Matrix**<br>Heatmap of Pearson correlation coefficients across numeric variables. | Chapter 03 (EDA) | `plots/fig-01-correlation-matrix.png` | Seaborn Correlation Heatmap |
| **02** | **Visit Duration Distribution**<br>Histogram showing baseline pitch duration clustering at 15–20 minutes. | Chapter 03 (EDA) | `plots/fig-02-duration-distribution.png` | Distribution Histogram + KDE |
| **03** | **Channel Conversion & Revenue Boxplots**<br>Comparative revenue yield and conversion probability by `shop_type`. | Chapter 03 (EDA) | `plots/fig-03-channel-performance.png` | Categorical Boxplots |
| **04** | **CHAID Decision Tree**<br>Non-linear segmentation tree identifying high-yield retail clusters. | Chapter 04 (Segmentation) | `plots/fig-04-chaid-tree.png` | Decision Tree Diagram |
| **05** | **DOE Main Effects Plot**<br>Steepness comparison of Credit Terms ($x_1$) vs. Pitch Duration ($x_2$). | Chapter 06 (DOE) | `plots/fig-05-doe-main-effects.png` | Linear Main Effects Plot |
| **06** | **Two-Factor Interaction Profiler**<br>Interaction plot demonstrating non-parallel synergy curves. | Chapter 06 (DOE) | `plots/fig-06-interaction-profiler.png` | JMP Interaction Matrix |
| **07** | **Response Surface Contour Plot**<br>3D surface mapping revenue yield across credit terms and duration. | Chapter 07 (Response Surface)| `plots/fig-07-response-surface.png` | 3D Contour & Mesh Surface |
| **08** | **Model Residual Diagnostics**<br>Normal Q-Q plot and Residuals vs. Fitted plot confirming model assumptions. | Chapter 07 (Response Surface)| `plots/fig-08-residual-diagnostics.png` | 2x2 Diagnostic Panel |
| **09** | **JMP Multi-Response Profiler**<br>Desirability profiler balancing revenue, conversion, and credit risk. | Chapter 08 (Optimization) | `plots/fig-09-profiler.png` | JMP Prediction Profiler |
| **10** | **Monte Carlo Risk Distribution**<br>10,000-run simulation histogram demonstrating downside protection. | Chapter 08 (Optimization) | `plots/fig-10-monte-carlo.png` | Simulated Probability Density |

---

## 2. Selected ASCII Schematic Profiles

### 2.1 Figure 07: Response Surface Contour

```text
                           RESPONSE SURFACE REVENUE CONTOUR
  Visit Duration (x2)
    35 Mins ┤                              [ KES 12,000+ ]  ███████
            │                       [ KES 8,000 ]    ██████████████
            │                [ KES 4,000 ]    █████████████████████
    15 Mins ┴───────────────[ KES 1,500 ]─────█████████████████████
                         Cash                      7 Days Credit
                               Credit Terms (x1)
```

* **Takeaway**: Maximum revenue yield (top right) is unlocked exclusively when combining **7-Day Credit Terms** with **35-Minute Pitch Durations**.

---

### 2.2 Figure 09: Multi-Response Prediction Profiler

```text
                               JMP PREDICTION PROFILER
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

* **Takeaway**: Desirability peaks when credit terms are enabled for Large/Medium accounts while keeping pitch durations tightly structured.

---

## 3. Technical Specifications & Plotting Standards

All visualizations in the `plots/` directory adhere to the following technical rendering guidelines:

* **Resolution**: Rendered at high-density **300 DPI** for publication quality.
* **Color Palette**: Standardized corporate palette:
  * Primary Navy (`#1B365D`) for baseline/observed data.
  * Teal (`#008080`) for model-fitted response surfaces.
  * Amber/Coral (`#E06D53`) for risk limits, thresholds, and default alerts.
* **Export Format**: Lossless `.png` with embedded metadata for web rendering across GitHub pages and technical documentation.

---

*Case Study Repository Documentation Complete.*
