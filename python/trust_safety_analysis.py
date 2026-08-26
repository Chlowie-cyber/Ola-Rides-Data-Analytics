"""
Trust & Safety Analysis - Ola Rides Dataset
Flags potentially suspicious booking patterns for further review.
Author: Lehlogonolo Mpye
"""

import pandas as pd

# ---- Load data ----
df = pd.read_csv("C:/Users/hlogi/BroCabs_DataAnalyst_Project/data/Ola_ride_data.csv", sep=";")

# Make sure Date/Time are proper types
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Booking_Value"] = pd.to_numeric(df["Booking_Value"], errors="coerce")
df["Ride_Distance"] = pd.to_numeric(df["Ride_Distance"], errors="coerce")

print(f"Total rows loaded: {len(df)}")

# ---------------------------------------------------------
# FLAG 1: Customers with unusually high same-day cancellations
# ---------------------------------------------------------
cancelled = df[df["Booking_Status"].isin(["Canceled by Customer", "Canceled by Driver"])]

rapid_cancellers = (
    cancelled.groupby(["Customer_ID", "Date"])
    .size()
    .reset_index(name="Cancellations_That_Day")
)

suspicious_customers = rapid_cancellers[rapid_cancellers["Cancellations_That_Day"] >= 3]

print(f"\n[Flag 1] Customers with 3+ cancellations in a single day: {suspicious_customers['Customer_ID'].nunique()}")
print(suspicious_customers.sort_values("Cancellations_That_Day", ascending=False).head(10))

# ---------------------------------------------------------
# FLAG 2: Fare-per-km outliers (possible fare manipulation or data errors)
# ---------------------------------------------------------
completed = df[df["Booking_Status"] == "Success"].copy()
completed = completed[(completed["Ride_Distance"] > 0) & (completed["Booking_Value"] > 0)]
completed["Fare_Per_KM"] = completed["Booking_Value"] / completed["Ride_Distance"]

# Flag rides more than 3 standard deviations from the mean fare/km
mean_fpk = completed["Fare_Per_KM"].mean()
std_fpk = completed["Fare_Per_KM"].std()
upper_bound = mean_fpk + 3 * std_fpk
lower_bound = max(mean_fpk - 3 * std_fpk, 0)

fare_outliers = completed[
    (completed["Fare_Per_KM"] > upper_bound) | (completed["Fare_Per_KM"] < lower_bound)
]

print(f"\n[Flag 2] Fare-per-km outliers: {len(fare_outliers)} rides "
      f"(normal range: {lower_bound:.2f} - {upper_bound:.2f} per km)")
print(fare_outliers[["Booking_ID", "Vehicle_Type", "Ride_Distance", "Booking_Value", "Fare_Per_KM"]].head(10))

# ---------------------------------------------------------
# FLAG 3: "Diver Not Found" clusters by pickup location
# ---------------------------------------------------------
driver_not_found = df[df["Booking_Status"] == "Driver Not Found"]

driver_not_found_by_location = (
    driver_not_found.groupby("Pickup_Location")
    .size()
    .reset_index(name="Driver_Not_Found_Count")
    .sort_values("Driver_Not_Found_Count", ascending=False)
)

print(f"\n[Flag 3] Top pickup locations for 'Driver Not Found':")
print(driver_not_found_by_location.head(10))

#---------------------------------------------------------
# Export flagged records for the write-up
#---------------------------------------------------------
suspicious_customers.to_csv("C:/Users/hlogi/BroCabs_DataAnalyst_Project/data/flagged_rapid_cancellers.csv", index=False)
fare_outliers.to_csv("C:/Users/hlogi/BroCabs_DataAnalyst_Project/data/flagged_fare_outliers.csv", index=False)
driver_not_found_by_location.to_csv("C:/Users/hlogi/BroCabs_DataAnalyst_Project/data/driver_not_found_by_location.csv", index=False)

print("\nFlagged results exported to /data folder for review.")