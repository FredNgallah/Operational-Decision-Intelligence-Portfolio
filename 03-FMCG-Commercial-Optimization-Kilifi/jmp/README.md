# JMP Statistical Scripts & DOE Model Assets

> **Executive Overview:** This directory contains JMP Scripting Language (`.jsl`) files used to construct the custom 32-run experimental design matrix, fit the response surface model, and render the multi-response Prediction Profiler.

---

## 1. Directory Contents

| Script Name | Purpose | Target Response | Primary Visual Output |
| :--- | :--- | :--- | :--- |
| **`01_custom_doe_design.jsl`** | Generates the 32-run custom experimental design matrix with context stratification | Experimental Allocation | JMP Design Evaluation & Power Analysis |
| **`02_rsm_profiler_fit.jsl`** | Fits Response Surface Regression & renders Multi-Response Desirability Profiler | `revenue_per_visit`, `Order_conversion` | JMP Prediction Profiler & Interaction Plots |

---

## 2. JMP Workflow Execution Guide

1. Open **JMP Pro 17+**.
2. File $\rightarrow$ Open $\rightarrow$ Select `jmp/01_custom_doe_design.jsl` and click **Run**.
3. Load `data/kilifi_sales_visits_baseline.csv` as the underlying data source.
4. Execute `jmp/02_rsm_profiler_fit.jsl` to display interactive profiler optimization models.

---

*Note: All optimization outputs generated via these JMP scripts represent **simulated/model-based predictions** subject to live 6-month field validation.*
