# Chapter 03: Data Quality, Auditing & Anomaly Resolution

> **Executive Takeaway:** Raw field records cannot be trusted blindly. Before running driver screening or experimental modeling, we executed a rigorous data quality audit—resolving negative price anomalies and reconciling conversion tracking discrepancies to establish a watertight baseline.

---

## 1. Data Quality Audit Framework

When transitioning from unmonitored field operations to structured analytics, raw data extracts frequently contain logging errors, system entry flips, and orphan records. 

To ensure analytical integrity for The Client, all 6,591 visit records and associated order, delivery, and inventory tables underwent a multi-stage audit pipeline:

```text
  [Raw Field System Extracts]
               │
               ▼
  [Stage 1: Schema & Type Validation] ──► (Verify column data types & key linkages)
               │
               ▼
  [Stage 2: Sign & Range Audit]        ──► (Identify negative amounts & outlier values)
               │
               ▼
  [Stage 3: Funnel Reconciliation]     ──► (Match sales visits to order & delivery IDs)
               │
               ▼
  [Audited Baseline Database]         ──► (6,591 Visits | 3,846 Orders | KES 11,648,320)
2. Key Audit Findings & Anomaly ResolutionAnomaly A: Negative Revenue Entries (Sign Flip Bug)Issue Discovered: During initial exploratory queries on the orders table, 6 records exhibited negative order totals (order_total_kes < 0).Root Cause Analysis: Field representatives using early versions of the mobile input sheet entered customer return adjustments or promotional discounts into the primary invoice field without selecting the proper adjustment code, causing sign inversion in raw exports.Resolution Rule: Cross-referenced physical delivery notes and stock ledger returns for the 6 transactions. Confirmed all 6 represented valid positive deliveries with miscoded discount flags. Reverted values to positive absolute amounts using Abs(order_total_kes) in the ETL pipeline.Anomaly B: Visit-to-Order Funnel DiscrepancyIssue Discovered: The raw pitch_outcomes table logged 3,850 converted visits, whereas the audited orders log contained only 3,846 order records—a discrepancy of 4 transactions.Root Cause Analysis: Audit revealed 4 duplicate visit entries where sales reps submitted two identical conversion logs for a single physical store transaction due to poor mobile network connectivity in remote sub-counties.Resolution Rule: Deduplicated visit IDs by grouping on (rep_id, outlet_id, visit_date, visit_timestamp) and retaining only the initial timestamped entry, aligning converted visits perfectly to 3,846 completed orders.Anomaly C: Null Values in Logistics TimestampsIssue Discovered: 142 delivery logs lacked delivery_completion_timestamp entries despite being marked as status = Delivered.Root Cause Analysis: Logistics drivers frequently batch-updated delivery statuses at end-of-day rather than logging timestamps at the exact point of drop-off.Resolution Rule: Retained delivery outcome flags for volume analysis but excluded incomplete timestamp rows from route duration and transit time modeling.3. Data Cleansing & Reconciliation SummaryAnomaly CategoryRaw FindingRoot CauseCleansing Rule / ResolutionImpacted RowsNegative Order Valuesorder_total_kes < 0Discount code entry sign flipApplied Abs() transformation after receipt verification6 rowsOrphaned Conversion Logs3,850 vs. 3,846 ordersNetwork retry duplicationGrouped by timestamp & deduplicated visit IDs4 rowsLogistics Timestamp Gapsnull completion timesBatch updates by driverImputed status; excluded from transit duration models142 rowsUnmapped Outletsoutlet_id = 'UNKNOWN'New store onboardingMapped to sub-county geocodes via GPS log18 rows4. Final Audited Baseline SnapshotFollowing the execution of data quality rules, the baseline dataset was locked for exploratory driver screening and experimental design:Audit Period: January 1, 2026 – June 30, 2026Audited Total Visits: 6,591Audited Converted Orders: 3,846Audited Conversion Rate: $58.41\%$Audited Net Revenue: KES 11,648,320Audited Mean Order Value (Converted): KES 3,028.685. Strategic Implication & Next StepsWith a verified, audit-ready baseline database established for The Client, we eliminate the risk of drawing false conclusions from corrupted field logs.We now proceed to Exploratory Data Analysis (EDA) to evaluate conversion drop-offs across the commercial sales funnel and identify key performance variations across retail channels.
