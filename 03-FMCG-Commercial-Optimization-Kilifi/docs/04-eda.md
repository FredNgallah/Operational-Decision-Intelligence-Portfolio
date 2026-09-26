# Chapter 04: Exploratory Data Analysis — Commercial Funnel & Segment Dynamics

> **Executive Takeaway:** Analysis of 6,591 sales visits reveals a critical structural insight: order scale and conversion velocity are governed by completely different commercial mechanisms. Order volume is segment-driven, while closing probability is channel-driven.

---

## 1. Commercial Sales Funnel Analysis

Evaluating the 6-month baseline dataset ($N=6,591$ visits) establishes the enterprise sales funnel for The Client. Out of 6,591 field pitch opportunities, 3,846 converted into paid orders, delivering a baseline conversion rate of **58.41%** and **KES 11,648,320** in net revenue.

```text
                               COMMERCIAL SALES FUNNEL (JAN - JUN 2026)
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ TOTAL FIELD VISITS: 6,591 (100.0%)                                                        │
└─────────────────────────────────────────────┬─────────────────────────────────────────────┘
                                              │
                                              ▼  [58.41% Visit-to-Order Conversion]
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ CONVERTED ORDERS: 3,846 (58.41%)                                                          │
└─────────────────────────────────────────────┬─────────────────────────────────────────────┘
                                              │
                                              ▼  [100% Fulfillment Rate]
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ COMPLETED DELIVERIES: 3,846 Orders  ──►  KES 11,648,320 NET REVENUE                       │
└───────────────────────────────────────────────────────────────────────────────────────────┘
Figure 3: Audited baseline sales funnel showing conversion efficiency and net revenue realization across 6,591 field visits.2. Order Scale is Segment-Driven (size_tier)To understand revenue variance across accounts, visits were analyzed across customer size tiers (Large, Medium, Small).The empirical baseline shows that account size tier dictates transaction scale ($p < 0.0001$). Large-tier retail outlets generate significantly higher order totals per transaction, serving as the foundation of overall revenue volume.Customer Size TierConverted OrdersTotal Revenue (KES)Mean Order Value (KES)Revenue Share (%)Large612KES 6,882,420KES 11,245.7859.09%Medium1,420KES 3,425,040KES 2,412.0029.40%Small1,814KES 1,340,860KES 739.1711.51%Total / Overall3,846KES 11,648,320KES 3,028.68100.00%Plaintext                         REVENUE DISTRIBUTION BY CUSTOMER SIZE TIER
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ LARGE TIER     ████████████████████████████████████████ 59.09% (KES 6.88M)                │
│ MEDIUM TIER    ███████████████ 29.40% (KES 3.43M)                                         │
│ SMALL TIER     ██████ 11.51% (KES 1.34M)                                                  │
└───────────────────────────────────────────────────────────────────────────────────────────┘
Figure 4: Distribution of transaction revenue across Large, Medium, and Small account size tiers.3. Conversion Velocity is Channel-Driven (shop_type)While transaction scale depends on account size, closing probability (Order_conversion) is dictated by outlet channel format (shop_type).High-frequency neighborhood formats convert at high rates during sales pitches, whereas hospitality and high-end accounts exhibit low closing efficiency:Outlet Channel Format (shop_type)Total VisitsConverted OrdersConversion Rate (%)Total Revenue (KES)Mini-Mart1,21091575.62%KES 3,812,400Kiosk2,1501,51070.23%KES 1,812,000Duka1,8201,02056.04%KES 1,622,500Supermarket41021552.44%KES 2,840,100Wholesaler38011229.47%KES 1,120,320Hotel / Resort6217411.92%KES 441,000Total Baseline6,5913,84658.41%KES 11,648,320Figure 5: Visit-to-order conversion rates across retail channel formats, highlighting high conversion velocity in Mini-Marts and Kiosks.4. Key Exploratory InsightsThe Hospitality Trap: Hotel/Resort visits consumed significant rep field time but yielded a dismal 11.92% conversion rate, making unmapped cold prospecting in this segment highly inefficient.Mini-Marts as the Commercial Sweet Spot: Mini-Marts represent the optimal blend of conversion velocity (75.62%) and transaction scale, generating KES 3.81M in revenue.Small Account Volume: Small-tier accounts (mostly Dukas and Kiosks) account for $47.17\%$ of all orders (1,814 transactions) but contribute only $11.51\%$ of net revenue, highlighting the need for efficient, low-cost pitch durations.5. Strategic Implication & Next StepsExploratory data analysis demonstrates that sales strategy must separate route targeting from pitch execution.To prepare for experimental optimization, we must run statistical driver screening to separate significant predictors from irrelevant operational noise (such as rep prior experience or delivery vehicle assignment).
