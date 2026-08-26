# Ola Rides — Trust & Safety Analysis
**Prepared by:** Lehlogonolo Mpye
**Purpose:** Extension of the core Ola Rides analysis, applying a fraud/anomaly-detection lens to the same 103,024-row booking dataset — demonstrating the intersection of data analysis and security thinking.

---

## Approach

Using Python, the dataset was screened for three categories of suspicious or anomalous patterns commonly monitored in e-hailing trust & safety programs:

1. Customers with unusually high same-day cancellation counts (potential abuse pattern)
2. Fare-per-kilometre statistical outliers (potential pricing manipulation or data quality issues)
3. Geographic concentration of "Driver Not Found" incidents (potential supply gaps or system issues)

---

## Findings

**1. No evidence of abusive rapid-cancellation behavior.**
Screening for customers with 3 or more cancellations in a single day returned zero matches across all 103,024 bookings. This is a clean result — it suggests cancellation behavior in this dataset is organic rather than driven by bulk/abusive booking-and-cancelling patterns. Worth re-checking periodically as a standing monitor rather than a one-time check.

**2. 966 bookings (0.9%) show fare-per-kilometre outliers.**
Using a statistical threshold (3 standard deviations from the mean fare-per-km), 966 rides fell outside the normal range. Several examples are striking — for instance, a 2km Mini ride billed at ₹2,542 (₹1,271/km), against a dataset-wide average fare of ₹548.75 total. These outliers likely represent a mix of:
- Data entry or logging errors (distance or fare captured incorrectly)
- Edge-case pricing (surge pricing, cancellation fees folded into the fare field)
- A smaller number of cases warranting manual fraud review

Recommendation: cross-reference this flagged list against surge-pricing logs and cancellation-fee records before treating any individual case as suspicious — but the pattern as a whole is worth a recurring automated check.

**3. "Driver Not Found" incidents are spread across many zones, not concentrated in one.**
The top 10 affected pickup locations (Hennur, Marathahalli, Mysore Road, Peenya, Hosur Road, Cox Town, Sahakar Nagar, Kengeri, Nagarbhavi, Kammanahalli) each show a similar incident count (215-228). This even spread suggests a systemic driver-supply shortfall across the city rather than a localized problem — a different fix than what a single-hotspot pattern would call for.

---

## Why This Matters

This analysis shows that the same booking dataset used for revenue and operations reporting can also support a lightweight trust & safety monitoring layer — using standard data analysis tools (Python, pandas) rather than specialized fraud-detection software. For a role spanning data analysis and security-adjacent thinking, this demonstrates the ability to look at operational data through a risk lens, not just a performance lens.

---

*Full script (`trust_safety_analysis.py`) and flagged record exports are included in the project's `python/` and `data/` folders.*