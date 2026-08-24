# Ola Rides — Business Insight Summary
**Prepared by:** Lehlogonolo "Chlowie" Mpye
**Purpose:** Portfolio analysis submitted in support of application for the Data Analyst (E-Hailing) role at Bro Cabs

---

## Overview

This analysis covers 50,000 ride records from the Ola Ride Booking dataset, examining booking outcomes, revenue by vehicle type, cancellation patterns, booking trends over time, payment behavior, and service quality across a one-month period. The goal was to surface insights that mirror the kind of operational and executive reporting Bro Cabs runs internally, and to show how the same techniques could apply to its own trip and driver data.

**Headline numbers:**
- **103K total bookings**
- **₹56.53M total revenue**
- **₹548.75 average fare**
- **62.09% completion rate**

---

## Key Findings

**1. Nearly 4 in 10 bookings never complete a successful ride.**
Only 62.09% of bookings result in a completed trip. The remainder splits across driver cancellations (17.89%), customer cancellations (10.19%), and "driver not found" (9.81%). This is the single biggest lever for revenue growth — closing even a few points of this gap would meaningfully lift completed rides without needing to grow demand.

**2. Cancellations are a steady, ongoing pattern — not a one-off spike.**
Tracking bookings by status across the month shows successful rides holding consistently around 2,000/day, while cancellation volumes stay fairly flat alongside them. This means cancellations aren't tied to a single bad day or event — they're a persistent operational issue worth addressing structurally, not reactively.

**3. Driver-side cancellations are dominated by controllable causes.**
Among rides cancelled by drivers, the leading reasons were personal/car-related issues and customer-related issues, followed by smaller categories like passenger illness or exceeding the permitted number of passengers. Because these are largely process or communication issues rather than demand problems, they're addressable through driver support, vehicle maintenance programs, or clearer passenger-count rules at booking time.

**4. Revenue is broadly balanced across vehicle types, with Prime Sedan slightly ahead.**
Prime Sedan led total revenue, closely followed by eBike, Auto, Prime Plus, Mini, Bike, and Prime SUV — all within a tight band. This suggests no single vehicle category is significantly under- or over-performing, meaning fleet-mix decisions can be driven more by cost-to-serve and availability than by revenue potential alone.

**5. Demand is concentrated in a handful of pickup zones.**
A small set of pickup locations account for a disproportionate share of bookings. Concentrating driver availability and incentive campaigns in these zones during peak windows would likely improve both completion rate and driver earnings simultaneously.

**6. Cash remains the dominant payment method, even in a digital-first market.**
For completed rides, about 55% are paid in cash, 40% via UPI, with card payments making up a small remainder. This has operational implications for driver cash-handling and reconciliation processes.

**7. Service quality is strong and balanced.**
Average driver and customer ratings both sit around 4 out of 5, suggesting that when rides do complete, the experience on both sides is generally positive — reinforcing that the priority opportunity is completion rate, not service quality.

---

## Recommendations for Bro Cabs

- Investigate the top driver-cancellation reasons directly with drivers (vehicle maintenance support, clearer trip details before acceptance) to reduce avoidable cancellations.
- Set a passenger-count confirmation step at booking to cut "more than permitted people" cancellations.
- Use pickup-zone concentration data to guide driver positioning and surge/incentive timing.
- Track completion rate as a standalone KPI alongside revenue — a small improvement here compounds directly into revenue without new customer acquisition cost.
- Since cancellations are steady rather than spiky, treat the fix as an ongoing operational program rather than a one-time intervention.

---

*Full SQL queries, Power BI dashboard (2 pages), and Python EDA supporting this summary are included in the accompanying project files.*