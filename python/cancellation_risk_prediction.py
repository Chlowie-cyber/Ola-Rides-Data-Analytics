"""
Cancellation Risk Prediction - Ola Rides Dataset
Trains a simple classifier to predict whether a booking will complete successfully or get cancelled, based on booking-time features.
Author: Lehlogonolo Mpye
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# ---- Load data ----
df = pd.read_csv("C:/Users/hlogi/BroCabs_DataAnalyst_Project/data/Ola_ride_data.csv", sep=";")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Time"] = pd.to_datetime(df["Time"], format="%H:%M:%S", errors="coerce")

# ---- Build the target: 1 = completed. 0 = any cancellation/driver-not-found ----
df["Completed"] = (df["Booking_Status"] == "Success").astype(int)

# ---- Feature engineering ----
df["Hour"] = df["Time"].dt.hour
df["DayOfWeek"] = df["Date"].dt.dayofweek    # 0 = Monday, 6 = Sunday

features = ["Vehicle_Type", "Pickup_Location", "Hour", "DayOfWeek"]
model_df = df[features + ["Completed"]].copy()

# Fill any genuinely values in feature columns rather than drooping rows
model_df["Hour"] = model_df["Hour"].fillna(model_df["Hour"].median())
model_df["DayOfWeek"] = model_df["DayOfWeek"].fillna(model_df["DayOfWeek"].median())
model_df["Vehicle_Type"] = model_df["Vehicle_Type"].fillna("Unknown")
model_df["Pickup_Location"] = model_df["Pickup_Location"].fillna("Unknown")

print(f"Rows available for modeling: {len(model_df)}")
print(f"Completion rate in modeling data: {model_df['Completed'].mean():.2%}")

# ---- Encode categorical features ----
encoders = {}
X = model_df[features].copy()
for col in ["Vehicle_Type", "Pickup_Location"]:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    encoders[col] = le

y = model_df["Completed"]

# ---- Train/Test Split ----
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ---- Train a shallow decision tree (easy to explain to non-technical stakeholders) ----
model = DecisionTreeClassifier(max_depth=4, class_weight="balanced", random_state=42)
model.fit(X_train, y_train)

# ---- Evaluate ----
y_pred = model.predict(X_test)

print("\n=== Model Preformance ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["Cancelled/Not Found", "Completed"]))
print("Confusion Matrix (rows=actual, cola=predicated):")
print(confusion_matrix(y_test, y_pred))

# ---- Feature importance ----
importances = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)
print("\n=== Feature Importance (what drives completion risk) ===")
print(importances)

# ---- Save a visual of the tree ----
plt.figure(figsize=(34,18))
plot_tree(model, feature_names=features, class_names=["Cancelled", "Completed"],
          filled=True, rounded=True, fontsize=8, impurity=False, proportion=False)
plt.title("Cancelltion Risk Decision Tree")
plt.savefig("C:/Users/hlogi/BroCabs_DataAnalyst_Project/assets/cancelltion_risk_tree.png", dpi=200, bbox_inches="tight")
print("\nDecision tree diagram saved to ../assets/cancellation_risk_tree.png")

# ---- Save feature importance chart ----
plt.figure(figsize=(8, 5))
importances.plot(kind="barh", color="#6B2FB3")
plt.xlabel("Importance")
plt.title("What Predicts Whether a Booking Completes?")
plt.tight_layout()
plt.savefig("C:/Users/hlogi/BroCabs_DataAnalyst_Project/assets/cancellation_risk_feature_importance.png", dpi=150)
print("Feature importance chart saved to ../assets/cancellation_risk_feature_importance.png")