# Chapter 02: Building the Operational Data Foundation — The 20-Domain Architecture

> **Executive Takeaway:** To eliminate field opacity, we engineered a relational 20-domain operational data capture system that transformed unstructured store visits, orders, and logistics into a standardized, audit-ready data asset.

---

## 1. Architecture Overview & System Strategy

To move Meru Fresh Dairy Ltd. from gut-feel decision-making to data-driven commercial execution, we constructed a unified 20-domain operational data infrastructure. 

Rather than deploying isolated tools for sales, inventory, and delivery, this relational workbook framework connects every point-of-sale interaction back to underlying logistics, product SKUs, and sales rep performance metrics.

```text
                               20-DOMAIN OPERATIONAL DATA ARCHITECTURE
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                                   CORE ENTITY REGISTRIES                                  │
│  • Sales Rep Profiles     • Customer Master (Accounts)   • Vehicle Fleet Registry         │
│  • Product SKU Catalog    • Retail Outlet Master         • Territory & Route Mapping      │
└─────────────────────────────────────────────┬─────────────────────────────────────────────┘
                                              │
                                              ▼
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                                 FIELD EXECUTION TRACKING                                  │
│  • Sales Visits Log       • Route Schedules              • Time Tracking & Duration       │
│  • Pitch Outcome Log      • Product Price Matrix          • Credit Terms & Approvals       │
└─────────────────────────────────────────────┬─────────────────────────────────────────────┘
                                              │
                                              ▼
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                                FULFILLMENT & FINANCIALS                                   │
│  • Orders Master          • Delivery Logs                • Cold-Chain Temperature Logs   │
│  • Order Line Items       • Inventory & Stock Ledger     • Returns & Spoilage Ledger      │
│  • Rep Performance        • Customer Feedback Register                                    │
└───────────────────────────────────────────────────────────────────────────────────────────┘
Figure 2: Conceptual overview of the 20-domain relational data architecture powering the Kilifi sales optimization framework.2. Key Operational Domains & Schema BreakdownThe system tracks 6,591 field visits and 3,846 converted orders across 20 interconnected domains. The table below highlights the primary relational tables powering the analytics pipeline:Domain #Table NameKey Primary FieldsStrategic Purpose01sales_repsrep_id, rep_name, fmcg_exp_yrsTracks rep profiles and prior sales experience.02vehiclesvehicle_id, vehicle_type, capacity_kgMonitors logistics allocation and vehicle efficiency.03outletsoutlet_id, shop_type, location_subcountyClassifies retail channel formats across Kilifi.04customerscustomer_id, size_tier, credit_limit_kesTiers accounts into Large, Medium, and Small.05sales_visitsvisit_id, rep_id, outlet_id, duration_minPrimary log capturing field activity and pitch duration.06pitch_outcomesoutcome_id, visit_id, Order_conversionRecords binary conversion outcomes (Converted vs. Declined).07ordersorder_id, visit_id, order_total_kesMaster transaction register capturing total invoice value.08order_itemsitem_id, order_id, sku_id, quantity_unitsLine-item SKU breakdown for demand analysis.09deliveriesdelivery_id, order_id, delivery_statusTracks fulfillment success, delays, and rejections.10stock_ledgerentry_id, sku_id, stock_on_handMaintains warehouse inventory levels and stockout flags.11–20Auxiliary DomainsRoutes, Pricing, Credit, Spoilage, Temperature, etc.Supports cold-chain audits, credit policy, and route efficiency.3. Normalization & Relational IntegrityTo ensure raw field entries could be queried seamlessly in Python and JMP, the database enforces strict relational rules:Visit-to-Order Linkage: Every order (orders.order_id) must originate from a valid visit log (sales_visits.visit_id). Unlinked orders are flagged immediately as audit exceptions.Channel & Size Segmentation: Outlets are strictly mapped to one of 6 shop_type categories (e.g., Kiosk, Mini-Mart, Supermarket, Hotel/Resort) and customers to one of 3 size_tier levels (Large, Medium, Small).Time Integrity: Field duration (visit_duration_min) is calculated using timestamp logging to prevent self-reported rep bias.4. Operational Summary (Jan 1 – Jun 30, 2026)Total Captured Visits: 6,591Total Converted Orders: 3,846Conversion Rate: $58.41\%$Total Order Value: KES 11,648,320Average Order Value (Converted): KES 3,028.685. Strategic Implication & Next StepsEstablishing this 20-domain system created the foundational dataset required for formal analytics. However, raw field data often contains entry errors, negative line items, or missing fields.Before running statistical driver screening, the dataset must undergo a thorough data quality audit and reconciliation process.
