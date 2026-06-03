# Real-Time Statistical Process Control (SPC) & Closed-Loop Material Loss Engine

## 📌 Executive Summary
In continuous plastic extrusion and manufacturing, untracked raw material variance and delayed quality feedback directly erode gross margins. This project delivers an enterprise-grade Decision Intelligence system deployed for a major PVC manufacturing plant. 

The engine introduces a **two-tier inventory validation gate** combined with live **Statistical Process Control (SPC)**. It shifts the facility from lagging weekly retrospective reporting to active, real-time variance detection, protecting intellectual property and isolating hidden process losses within a 24-hour window.

<img width="930" height="337" alt="image" src="https://github.com/user-attachments/assets/d49f7db7-f921-4ccc-b885-df2a73d692eb" />

<img width="785" height="197" alt="image" src="https://github.com/user-attachments/assets/4b1a5ea2-30d2-497e-b1b1-7a4fe86097f1" />

<img width="706" height="48" alt="image" src="https://github.com/user-attachments/assets/e857ec57-b8c9-477a-8f43-545acee6b896" />



---

## 🛠️ System Architecture & The Two-Tier Gate

The architecture isolates material tracking at two critical physical choke points to eliminate "invisible scrap" and unrecorded floor waste:

1. **The Store Gate (Weekly Macro-Reconciliation):** Tracks bulk raw material movements from main inventory to the production floor bins, establishing the baseline mass-balance ledger.
2. **The Floor Gate (Daily Micro-Reconciliation):** Captures exact supervisor-logged machine inputs ($Consumption$) against automated output calculations ($Good\ Production + Tracked\ Floor\ Scrap$). 

### Core Mathematical Framework for Floor Variance:
* **Total Process Output (kgs):** $\text{Daily Inline Material} + \text{Daily Floor Scrap}$
* **Floor Material Variance (kgs):** $\text{Material Consumption per day} - \text{Total Process Output}$
* **% Floor Variance:** $\frac{\text{Floor Material Variance}}{\text{Material Consumption per day}}$

By separating machine-proven output from physical consumption, the system identifies process discrepancies (e.g., moisture loss, bulk feed calibration issues, or unlogged purges) in under 24 hours.

---

## 📈 Advanced Analytics & SPC Engine

The system features an automated, live-updating SPC chart tracking production weight stability across active shifts.

### Key Capabilities:
* **Early-Warning Spike Detection:** Uses an optimized lookback array evaluating the first 10 production samples of a run to flag immediate process shocks before they generate thousands of kilograms of non-conforming product.
* **Automated Process Capability ($Cp$ & $Cpk$):** Leverages non-collapsing multi-input array mapping (`MAP` + `LAMBDA` optimization) to automatically calculate process capability without manual dragging:
  * **$Cp$ (Process Potential):** Measures the absolute width of the process variation against customer specification limits ($\frac{USL - LSL}{6\sigma}$).
  * **$Cpk$ (Process Capability Index):** Adjusts for process centering ($\min(\frac{USL - \mu}{3\sigma}, \frac{\mu - LSL}{3\sigma})$).
* **Dynamic Engineering Recommendations:** An algorithmic decision matrix evaluates joint $Cp$/$Cpk$ thresholds to spit out live, context-aware operational playbooks (e.g., identifying whether an issue requires a mechanical DOE for screw wear vs. a simple haul-off speed calibration adjustment).
* <img width="711" height="169" alt="image" src="https://github.com/user-attachments/assets/efefad0d-2c8d-425a-8f1a-c1bada5c17eb" />
<img width="466" height="130" alt="image" src="https://github.com/user-attachments/assets/e1cc4246-45ff-44c7-9cc3-12399f4933bd" />



---

## 💼 Business Impact & Corporate Value
* **Finance-Approved Visibility:** Delivers real-time data streaming and auditable operational numbers directly to executive and finance leads, replacing vulnerable monthly physical inventory surprises.
* **Scrap Reduction:** Early spike indicators mitigate long-run extrusion defects, directly saving raw material input costs.
* **Zero-Maintenance Scale:** Engineered completely with dynamic array formulas; the system scales infinitely down the page as operators input logs without risking formula corruption or broken references.
* **Enterprise Security Perimeter:** Implements rigid role-based access controls and customized scope permissions, completely blocking client-side downloading, copying, or printing to protect core operational IP.
