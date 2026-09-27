# Appendix A: Technical Methodology & Mathematical Formulation

> **Executive Summary:** This technical appendix details the mathematical equations, statistical foundations, regression models, and simulation algorithms used across the Kilifi Commercial Optimization framework.

---

## 1. Baseline Driver Screening Models

### 1.1 Binary Logistic Regression (Order Conversion)

To identify structural drivers of visit-to-order conversion, we modeled the log-odds of a visit resulting in a completed sale ($Y = 1$):

$$\operatorname{logit}(P(Y=1)) = \ln\left(\frac{P(Y=1)}{1 - P(Y=1)}\right) = \beta_0 + \sum_{i=1}^{k} \beta_i X_i + \varepsilon$$

Where:
* $P(Y=1)$ is the probability of a visit converting to an order.
* $X_i$ represents categorical context factors (`shop_type`, `size_tier`, `delivery_vehicle`).
* $\beta_i$ represents the maximum likelihood parameter estimates.

### 1.2 CHAID Decision Tree Segmentation

To uncover non-linear interactions and segment store hierarchies, Decision Tree splits were evaluated using adjusted Chi-square ($\chi^2$) test statistics:

$$\chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

Where $O_{ij}$ and $E_{ij}$ are observed and expected cell counts across categorical store attributes.

---

## 2. Custom DOE Design Matrix & Orthogonality

### 2.1 Factorial Design Space ($2^2$ Design)

The controllable experimental levers were coded into normalized orthogonal scale $[-1, +1]$:

$$x_1 = \frac{\text{credit\_terms} - \text{Baseline}}{\Delta \text{Credit}}, \quad x_2 = \frac{\text{visit\_duration\_min} - 25}{10}$$

### 2.2 Model Matrix ($X$)

The $N=32$ design matrix incorporates blocking terms for store context:

$$Y = X\beta + \varepsilon, \quad \text{where } X \in \mathbb{R}^{32 \times p}$$

The variance-covariance matrix of the parameter estimates is minimized via D-optimality criterion:

$$\max \det(X^T X)$$

---

## 3. Response Surface Regression Equations

### 3.1 Multiple Linear Regression (`revenue_per_visit`)

The response surface for order revenue per visit is specified as:

$$\hat{Y}_{\text{rev}} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_{12} (x_1 x_2) + \sum_{j} \gamma_j B_j$$

Where:
* $x_1$: Coded indicator for Credit Terms (Cash vs. 7 Days).
* $x_2$: Coded continuous factor for Visit Duration (15 to 35 Mins).
* $x_1 x_2$: Two-factor interaction term capturing synergy.
* $B_j$: Fixed block effects for `shop_type` and `size_tier`.

---

## 4. Multi-Response Desirability Optimization

### 4.1 Derringer-Suich Desirability Functions

Individual desirability functions $d_i(Y_i)$ map each response variable onto a scale $[0, 1]$:

$$d_1(Y_{\text{rev}}) = \begin{cases} 0 & \text{if } Y < L \\ \left(\frac{Y - L}{T - L}\right)^s & \text{if } L \le Y \le T \\ 1 & \text{if } Y > T \end{cases}$$

Where $L = \text{KES } 2,500$ (lower bound), $T = \text{KES } 10,000$ (target), and $s = 1.0$ (linear weight).

### 4.2 Overall Desirability Index ($D$)

$$\text{Overall Desirability } D = \left( \prod_{i=1}^{k} d_i(Y_i)^{w_i} \right)^{\frac{1}{\sum w_i}}$$

---

## 5. Monte Carlo Simulation Framework

To quantify downside risk under market uncertainty, parameter estimates were sampled using multivariate Gaussian distributions:

$$\boldsymbol{\beta}_{\text{sim}} \sim \mathcal{N}\left(\hat{\boldsymbol{\beta}}, \, s^2 (X^T X)^{-1}\right)$$

Across 10,000 stochastic iterations, predicted revenue yields and credit default probabilities were aggregated to generate empirical confidence bounds.

---

*Next Appendix:* [`limitations.md`](limitations.md) — *Analytical Boundaries & Dataset Constraints.*
