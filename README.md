# Ola Rides — E-Hailing Data Analyst Portfolio Project

A self-directed portfolio project analyzing 50,000 ride-booking records from the Ola Ride Booking dataset, built to demonstrate the skills required for a Data Analyst (E-Hailing) role — SQL querying, data cleaning, dashboarding, and translating data into business decisions.

🎥 **Video walkthrough:** [link coming soon]
📄 **Insight write-up:** [Ola_Rides_Insight_Summary.md](./Ola_Rides_Insight_Summary.md)

---

## Project Overview

| Area | Tools Used |
|---|---|
| Data cleaning & preparation | Excel, Power Query, Python (pandas) |
| Database querying | MySQL |
| Exploratory data analysis | Python (Jupyter) |
| Dashboarding | Power BI (2 pages) |
| Reporting | Markdown write-up |

**Headline results:**
- 103K total bookings analyzed
- ₹56.53M total revenue
- ₹548.75 average fare
- 62.09% completion rate

---

## Repository Structure

```
BroCabs_DataAnalyst_Project/
├── data/                    # Raw and cleaned CSV extracts
├── sql/                     # SQL analysis scripts
│   └── 01_ola_analysis.sql
├── python/                  # Exploratory data analysis
│   └── eda_analysis.py
├── assets/                  # Exported chart images
├── Ola Rides Dashboard.pbix # Power BI dashboard file (2 pages)
├── Ola_Rides_Insight_Summary.md
└── README.md
```

---

## Dashboard Pages

**Page 1 — Overview:** KPI cards (bookings, revenue, average fare, completion rate), revenue by vehicle type, booking outcomes, top pickup locations, top driver-cancellation reasons.

**Page 2 — Trends & Service Quality:** Daily booking trends by status, payment method breakdown (completed rides only), average driver and customer ratings.

---

## Key Findings

1. **Completion rate is 62.09%** — driver cancellations, customer cancellations, and "driver not found" account for the remaining ~38% of bookings, representing the largest opportunity to grow revenue without new demand.
2. **Cancellations are a steady daily pattern, not a spike** — visible across the full month of trend data, meaning the fix needs to be an ongoing operational program.
3. **Driver-side cancellations are mostly controllable** — personal/vehicle issues and customer-related issues are the top causes, both addressable through operational changes.
4. **Revenue is evenly spread across vehicle types**, with Prime Sedan slightly leading — fleet decisions can prioritize cost-to-serve over revenue potential.
5. **Booking demand is concentrated in a small number of pickup zones**, suggesting targeted driver positioning could improve completion rate and driver earnings together.
6. **Cash remains the dominant payment method (55%)**, even ahead of UPI (40%) — relevant for driver cash-handling processes.
7. **Service quality is strong** — average driver and customer ratings both sit around 4/5.

Full detail in [the insight write-up](./Ola_Rides_Insight_Summary.md).

---

## Dashboard Preview

*(embed dashboard screenshots here)*

---

## About This Project

This project was built to apply for the Data Analyst (E-Hailing) role at Bro Cabs, following guidance from the hiring team that personal projects and evidence of applied skills are welcome from candidates without formal industry experience.

**Contact:** Lehlogonolo Mpye