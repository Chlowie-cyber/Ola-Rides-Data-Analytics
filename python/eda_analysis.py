import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")

# 1. Load Data
csv_path = "../data/Ola_ride_data.csv"
if not os.path.exists(csv_path):
    csv_path = "Ola_ride_data.csv"
if not os.path.exists(csv_path):
    csv_path = "../Ola_ride_data.csv"

print(f"Loading data from: {csv_path}...")

try:
    df = pd.read_csv(csv_path, sep=None, engine="python")
except Exception:
    df = pd.read_csv(csv_path, sep=";")

# Clean Booking_Value column if necessary
if df["Booking_Value"].dtype == "object":
    df["Booking_Value"] = (
        df["Booking_Value"]
        .astype(str)
        .str.replace("R", "", regex=False)
        .str.replace(" ", "", regex=False)
        .str.replace(",", ".", regex=False)
    )
    df["Booking_Value"] = pd.to_numeric(df["Booking_Value"], errors="coerce").fillna(0)

# 2. Key Metrics Summary
total_bookings = len(df)
total_revenue = df["Booking_Value"].sum()
avg_fare = df["Booking_Value"].mean()
completed_rides = len(df[df["Booking_Status"] == "Success"])
completion_rate = (completed_rides / total_bookings) * 100

print("\n" + "=" * 45)
print("       BRO CABS - EXECUTIVE EDA SUMMARY      ")
print("=" * 45)
print(f"Total Booking Requests : {total_bookings:,}")
print(f"Total Gross Revenue    : R{total_revenue:,.2f}")
print(f"Average Ride Fare      : R{avg_fare:,.2f}")
print(f"Overall Completion Rate: {completion_rate:.2f}%")
print("=" * 45)

# Ensure output directory exists
output_dir = "../assets"
os.makedirs(output_dir, exist_ok=True)

# 3. Chart 1: Booking Status Breakdown
plt.figure(figsize=(8, 5))
status_counts = df["Booking_Status"].value_counts().reset_index()
status_counts.columns = ["Booking_Status", "Request_Count"]

ax1 = sns.barplot(
    data=status_counts,
    x="Request_Count",
    y="Booking_Status",
    hue="Booking_Status",
    palette="viridis",
    legend=False
)
plt.title("Bro Cabs - Ride Booking Status Breakdown", fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Number of Requests")
plt.ylabel("Booking Status")

for p in ax1.patches:
    width = p.get_width()
    if width > 0:
        ax1.annotate(
            f"{int(width):,}",
            (width / 2, p.get_y() + p.get_height() / 2.),
            ha="center", va="center", color="white", fontweight="bold"
        )

plt.tight_layout()
plt.savefig(f"{output_dir}/booking_status_breakdown.png", dpi=300)
plt.close()

# 4. Chart 2: Revenue by Vehicle Type
plt.figure(figsize=(10, 5))
vehicle_df = df.groupby("Vehicle_Type").agg(
    Total_Requests=("Booking_ID", "count"),
    Total_Revenue=("Booking_Value", "sum")
).reset_index().sort_values(by="Total_Revenue", ascending=False)

ax2 = sns.barplot(
    data=vehicle_df,
    x="Vehicle_Type",
    y="Total_Revenue",
    hue="Vehicle_Type",
    palette="Blues_r",
    legend=False
)
plt.title("Bro Cabs - Gross Revenue by Vehicle Type", fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Vehicle Type")
plt.ylabel("Total Revenue (ZAR)")

for p in ax2.patches:
    height = p.get_height()
    if height > 0:
        # Check scale to avoid zeroed out R0.00M labels
        label = f"R{height/1e6:.2f}M" if height >= 1e6 else f"R{height:,.0f}"
        ax2.annotate(
            label,
            (p.get_x() + p.get_width() / 2., height / 2),
            ha="center", va="center", color="white", fontweight="bold"
        )

plt.tight_layout()
plt.savefig(f"{output_dir}/revenue_by_vehicle_type.png", dpi=300)
plt.close()

print(f"\n[+] EDA complete! Visual assets saved to '{output_dir}/'\n")