# Appendix C: 20-Domain Data Dictionary & Field Taxonomy

> **Executive Summary:** This data dictionary documents the schema, primary keys, foreign keys, data types, and operational definitions across the 20 relational domains engineered for The Client's commercial optimization database.

---

## 1. Relational Entity-Relationship Summary

The data architecture connects point-of-sale field interactions with inventory, financial, and logistics records.

```text
  [sales_reps] ────┐
                   ├───► [sales_visits] ───► [pitch_outcomes] ───► [orders] ───► [order_items]
  [outlets] ───────┤         │                                       │
  [vehicles] ──────┘         ▼                                       ▼
                     [routes_schedule]                          [deliveries] ──► [stock_ledger]
```

---

## 2. Core Domain Schema Definitions

### Domain 01: `sales_reps`
*Tracks sales representative profiles, experience levels, and territory assignments.*

| Field Name | Data Type | Key Type | Description & Operational Range |
| :--- | :--- | :---: | :--- |
| `rep_id` | `VARCHAR(10)` | **PK** | Unique identifier for sales representative (e.g., `REP001`). |
| `rep_name` | `VARCHAR(50)` | - | Full legal name of sales representative. |
| `fmcg_exp_yrs` | `FLOAT` | - | Years of prior FMCG sales experience ($0.0$ to $12.5$ years). |
| `assigned_zone` | `VARCHAR(30)` | - | Primary sub-county assigned (e.g., `Malindi`, `Kilifi North`). |

---

### Domain 02: `vehicles`
*Monitors delivery fleet assets, capacity, and route assignments.*

| Field Name | Data Type | Key Type | Description & Operational Range |
| :--- | :--- | :---: | :--- |
| `vehicle_id` | `VARCHAR(10)` | **PK** | Unique identifier for delivery vehicle (e.g., `VEH01`). |
| `vehicle_type` | `VARCHAR(20)` | - | Vehicle class (`Tuk-Tuk`, `3-Ton Truck`, `Motorbike`). |
| `capacity_kg` | `INT` | - | Maximum cargo payload capacity in kilograms. |

---

### Domain 03: `outlets`
*Classifies retail channel formats and physical geographic locations across Kilifi.*

| Field Name | Data Type | Key Type | Description & Operational Range |
| :--- | :--- | :---: | :--- |
| `outlet_id` | `VARCHAR(12)` | **PK** | Unique identifier for retail outlet (e.g., `OUT10042`). |
| `shop_type` | `VARCHAR(25)` | - | Channel format: `Kiosk`, `Duka`, `Mini-Mart`, `Supermarket`, `Wholesaler`, `Hotel/Resort`. |
| `subcounty` | `VARCHAR(30)` | - | Sub-county location (`Malindi`, `Kilifi South`, `Ganzi`, etc.). |
| `gps_lat` / `gps_lon`| `DECIMAL(9,6)` | - | Geofenced spatial coordinates for route verification. |

---

### Domain 04: `customers`
*Account master storing commercial scale tiers and credit limits.*

| Field Name | Data Type | Key Type | Description & Operational Range |
| :--- | :--- | :---: | :--- |
| `customer_id` | `VARCHAR(12)` | **PK** | Unique commercial account identifier. |
| `outlet_id` | `VARCHAR(12)` | **FK** | Linked retail outlet location. |
| `size_tier` | `VARCHAR(10)` | - | Account volume tier: `Large`, `Medium`, `Small`. |
| `credit_limit_kes`| `DECIMAL(10,2)` | - | Approved credit cap in KES ($0.00$ to $50,000.00$). |

---

### Domain 05: `sales_visits`
*Primary transactional log capturing all 6,591 field pitch interactions.*

| Field Name | Data Type | Key Type | Description & Operational Range |
| :--- | :--- | :---: | :--- |
| `visit_id` | `VARCHAR(15)` | **PK** | Unique sales visit tracking ID (e.g., `VIS20260312-041`). |
| `rep_id` | `VARCHAR(10)` | **FK** | Sales representative making the visit. |
| `outlet_id` | `VARCHAR(12)` | **FK** | Retail outlet visited. |
| `visit_date` | `DATE` | - | Date of visit interaction (`YYYY-MM-DD`). |
| `duration_min` | `INT` | - | Pitch duration in minutes ($5$ to $60$ mins). |

---

### Domain 06: `pitch_outcomes`
*Records conversion decisions and decline reasons for field visits.*

| Field Name | Data Type | Key Type | Description & Operational Range |
| :--- | :--- | :---: | :--- |
| `outcome_id` | `VARCHAR(15)` | **PK** | Pitch outcome record identifier. |
| `visit_id` | `VARCHAR(15)` | **FK** | Linked sales visit ID. |
| `Order_conversion`| `INT` | - | Binary outcome flag ($1 =$ Converted Order, $0 =$ Declined). |
| `decline_reason` | `VARCHAR(50)` | - | Categorical reason if declined (`Stock Full`, `Price High`, `Cash Flow`). |

---

### Domain 07: `orders`
*Master invoice log recording 3,846 converted sales transactions.*

| Field Name | Data Type | Key Type | Description & Operational Range |
| :--- | :--- | :---: | :--- |
| `order_id` | `VARCHAR(15)` | **PK** | Unique invoice/order ID (e.g., `ORD-2026-0891`). |
| `visit_id` | `VARCHAR(15)` | **FK** | Associated visit generating the order. |
| `credit_terms` | `VARCHAR(15)` | - | Commercial payment terms (`Cash`, `7 Days Credit`). |
| `order_total_kes` | `DECIMAL(10,2)` | - | Net invoice total in KES (Audited positive amount). |

---

### Domain 08: `order_items`
*Line-item product breakdown per transaction.*

| Field Name | Data Type | Key Type | Description & Operational Range |
| :--- | :--- | :---: | :--- |
| `item_id` | `VARCHAR(18)` | **PK** | Line item record ID. |
| `order_id` | `VARCHAR(15)` | **FK** | Master order identifier. |
| `sku_id` | `VARCHAR(10)` | **FK** | Product SKU ID (e.g., `YOG-250ML-VAN`). |
| `quantity_units` | `INT` | - | Number of units ordered ($1$ to $500$ crates). |
| `unit_price_kes` | `DECIMAL(8,2)` | - | Wholesale unit price in KES. |

---

### Auxiliary Domains (09–20) Summary

| Domain # | Table Name | Key Primary Fields | Primary Operational Scope |
| :--- | :--- | :--- | :--- |
| **09** | `deliveries` | `delivery_id`, `order_id` | Fulfillment status (`Delivered`, `Delayed`, `Rejected`). |
| **10** | `stock_ledger` | `ledger_id`, `sku_id` | Real-time warehouse balance and stockout alerts. |
| **11** | `routes_schedule` | `schedule_id`, `rep_id` | Assigned route plan and planned vs. actual stop sequence. |
| **12** | `price_matrix` | `price_id`, `sku_id` | Volume discount tiers and promotional pricing locks. |
| **13** | `credit_approvals`| `approval_id`, `customer_id`| Credit limit review logs and manager sign-off flags. |
| **14** | `spoilage_log` | `spoilage_id`, `sku_id` | Dairy expiration and damaged return tracking. |
| **15** | `temp_logs` | `log_id`, `vehicle_id` | Cold-chain refrigeration logs ($\text{Target } \le 4^\circ\text{C}$). |
| **16** | `rep_performance` | `perf_id`, `rep_id` | Weekly aggregate sales, conversion rates, and revenue yield. |
| **17** | `feedback_reg` | `feedback_id`, `outlet_id`| Store owner survey responses and product preference tags. |
| **18** | `payments_log` | `payment_id`, `order_id` | Collections, M-Pesa transaction reference, and cash balance. |
| **19** | `territory_map` | `zone_id`, `subcounty` | Sub-county boundary definitions and route clusters. |
| **20** | `audit_trail` | `event_id`, `user_id` | System change logs, manual data overrides, and error flags. |

---

*Next Appendix:* [`visual-index.md`](visual-index.md) — *Catalog of All Charts, Profilers & Visualizations.*
