# Ola Rides — E-Hailing Data Analyst Portfolio Project

A self-directed portfolio project analyzing 103,024 ride-booking records from the Ola Ride Booking dataset, built to demonstrate the skills required for a Data Analyst (E-Hailing) role — SQL querying, data cleaning, dashboarding, machine learning, and translating data into business decisions.

📄 **Insight write-up:** [Insight Summary.md](./Dashboard/Insight%20Summary.md)
🛡️ **Trust & Safety analysis:** [Trust_and_Safety_Notes.md](https://github.com/Chlowie-cyber/Ola-Rides-Data-Analytics/blob/main/Dashboard/Trust%20and%20Safety%20Notes.md)
🤖 **Cancellation risk model:** [Cancellation_Risk_Prediction_Notes.md](https://github.com/Chlowie-cyber/Ola-Rides-Data-Analytics/blob/main/Dashboard/Cancellation%20Risk%20Predication%20Notes.md)
🎥 **Video walkthrough:** included in `assets/Ola Rides Video.mp4`

---

## Project Overview

| Area | Tools Used |
|---|---|
| Data cleaning & preparation | Excel, Power Query, Python (pandas) |
| Database querying | MySQL |
| Exploratory data analysis | Python (pandas) |
| Machine learning | Python (scikit-learn) — decision tree classifier |
| Anomaly / fraud detection | Python (pandas) — rule-based flagging |
| Dashboarding | Power BI (2 pages) |
| Reporting | Markdown write-ups |

**Headline results:**
- 103K total bookings analyzed
- ₹56.53M total revenue
- ₹548.75 average fare
- 62.09% completion rate

---

## Repository Structure

```
Ola-Rides-Data-Analytics/
├── Dashboard/
│   ├── Insight Summary.md
│   ├── Trust_and_Safety_Notes.md
│   ├── Cancellation_Risk_Prediction_Notes.md
│   └── Ola Rides Dashboard.pbix
├── assets/                          # Exported chart images + video walkthrough
├── data/                            # Raw and cleaned CSV extracts
├── excel/                           # Data cleaning workbook
├── python/
│   ├── eda_analysis.py
│   ├── trust_safety_analysis.py     # Fraud / anomaly detection
│   └── cancellation_risk_prediction.py  # ML cancellation risk model
├── sql/
Ola Rides Analytics Project/
├── data/                    # Raw and cleaned CSV extracts
├── sql/                     # SQL analysis scripts
│   └── 01_ola_analysis.sql
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
8. **No evidence of abusive rapid-cancellation behavior** — a rule-based fraud screen found zero customers with 3+ same-day cancellations across all 103K bookings.
9. **966 bookings (0.9%) show fare-per-km outliers** — flagged for review as potential data errors or pricing anomalies.
10. **Vehicle Type and Hour of Day are the strongest predictors of cancellation risk** (decision tree model, 68% recall on cancellations) — Day of Week has zero predictive weight, reinforcing that cancellations aren't tied to specific days.

Full detail in the [Insight Summary](./Dashboard/Insight%20Summary.md), [Trust & Safety Notes](https://github.com/Chlowie-cyber/Ola-Rides-Data-Analytics/blob/main/Dashboard/Trust%20and%20Safety%20Notes.md), and [Cancellation Risk Prediction Notes](https://github.com/Chlowie-cyber/Ola-Rides-Data-Analytics/blob/main/Dashboard/Cancellation%20Risk%20Predication%20Notes.md).

---

## Dashboard Preview

<img width="1288" height="727" alt="image" src="https://github.com/user-attachments/assets/cbfed50b-5527-410a-ab1c-b96b5f2f23e3" />
<img width="1220" height="639" alt="image" src="https://github.com/user-attachments/assets/9719b564-3ab5-445c-b90d-748229dfb6fe" />

---

## About This Project

This project was built to apply for the Data Analyst (E-Hailing) role at Bro Cabs, following guidance from the hiring team that personal projects and evidence of applied skills are welcome from candidates without formal industry experience. It was later extended with fraud/anomaly detection and a cancellation risk prediction model to demonstrate the intersection of data analysis and security-minded thinking.

**Contact:** [Lehlogonolo Mpye](mailto:lehlogonolo189@gmail.com)
