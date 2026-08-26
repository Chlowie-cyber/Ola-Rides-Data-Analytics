# Ola Rides — Cancellation Risk Prediction
**Prepared by:** Lehlogonolo "Chlowie" Mpye
**Purpose:** Extension of the core Ola Rides analysis, using a machine learning model to predict which bookings are at risk of cancellation, based on booking-time features.

---

## Approach

A decision tree classifier was trained on 103,024 bookings to predict whether a ride would complete successfully or not, using only information available **at the moment of booking**: vehicle type, pickup location, hour of day, and day of week.

`Payment_Method` was deliberately excluded from the model. It's only recorded *after* a ride completes, so including it would be data leakage — the model would simply learn "no payment method recorded = cancelled," which is true by definition and offers no real predictive value.

Because only 62% of bookings complete successfully, the model was trained with **balanced class weighting** — instructing it to treat catching cancellations as equally important as catching completions, rather than defaulting to the easy (but useless) strategy of always predicting "Completed."

---

## Results

| Metric | Cancelled/Not Found | Completed |
|---|---|---|
| Precision | 0.38 | 0.62 |
| Recall | 0.68 | 0.32 |
| F1-score | 0.49 | 0.43 |

**Overall accuracy: 45.81%**

At first glance this looks low — a model that always predicted "Completed" would score 62% accuracy. But that model would catch **zero** cancellations, which is useless for an operations team trying to flag at-risk bookings. This model instead catches **68% of actual cancellations** (recall), trading some overall accuracy for the ability to actually surface the bookings that matter most to intervene on. For a trust & safety or dispatch use case, missing a real cancellation risk is more costly than a false alarm — so this trade-off is the right one, not a failure of the model.

## What Predicts Completion Risk

| Feature | Importance |
|---|---|
| Vehicle Type | 38.8% |
| Hour of Day | 35.1% |
| Pickup Location | 26.1% |
| Day of Week | 0.0% |

**Vehicle Type and Hour of Day are the strongest predictors** of whether a booking completes. **Day of Week carries zero predictive weight** — cancellations don't cluster on particular days, which reinforces the earlier finding from the trend analysis that cancellations are a steady, ongoing pattern rather than tied to specific days.

---

## Business Implication

Rather than treating cancellations as random noise, this model shows they're at least partially predictable from booking-time information alone — particularly vehicle type and time of day. A production version of this model could flag high-risk bookings in real time, allowing Bro Cabs to proactively offer incentives, prioritize driver matching, or send a confirmation nudge on bookings most likely to fall through.

---

*Full script (`cancellation_risk_prediction.py`), the decision tree diagram, and the feature importance chart are included in the project's `python/` and `assets/` folders.*