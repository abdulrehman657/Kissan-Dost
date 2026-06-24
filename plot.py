import matplotlib.pyplot as plt
import pandas as pd
import joblib

# 1. Load your generated data and trained AI brain
df = pd.read_csv('pak_crop_data.csv')
model = joblib.load('crop_model.pkl')

# 2. Define the exact features used during training
features = [
    'Rainfall_mm', 'GDD_HeatUnits', 'Solar_Radiation', 'Soil_pH', 
    'Clay_Percent', 'Sand_Percent', 'Organic_Carbon', 'Nitrogen_Base', 
    'Phosphorus_Base', 'Urea_Bags', 'DAP_Bags', 'Water_Source', 
    'Seed_Type', 'Land_Size_Acres'
]

X = df[features]
y_actual = df['Yield_Maunds']

# 3. Generate predictions using the loaded model
y_pred = model.predict(X)

# 4. Initialize a clean, side-by-side Matplotlib figure
plt.figure(figsize=(14, 6))

# --- CHART 1: Actual vs. Predicted Scatter ---
plt.subplot(1, 2, 1)
plt.scatter(y_actual, y_pred, alpha=0.4, color='#2ca02c', label='Farm Data Points')

# Draw a red dashed line representing a perfect prediction mapping
ideal_line = [y_actual.min(), y_actual.max()]
plt.plot(ideal_line, ideal_line, color='red', linestyle='--', linewidth=2, label='Perfect Prediction (Y=X)')

plt.title('Model Accuracy: Actual vs. Predicted Yield', fontsize=12, fontweight='bold')
plt.xlabel('Actual Yield (Maunds)', fontsize=10)
plt.ylabel('Predicted Yield (Maunds)', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# --- CHART 2: Feature Impact (Coefficients) ---
plt.subplot(1, 2, 2)
coefficients = model.coef_

# Convert to pandas series and sort by absolute impact size for a cleaner look
coef_series = pd.Series(coefficients, index=features)
sorted_coefs = coef_series.reindex(coef_series.abs().sort_values().index)

# Plot horizontal bars (Green for positive impact, Red/Orange for negative impact)
colors = ['#d62728' if x < 0 else '#1f77b4' for x in sorted_coefs]
sorted_coefs.plot(kind='barh', color=colors)

plt.title('Feature Impact Weights (Model Coefficients)', fontsize=12, fontweight='bold')
plt.xlabel('Mathematical Coefficient Value', fontsize=10)
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8) # Zero line anchor
plt.grid(axis='x', linestyle=':', alpha=0.6)

# 5. Render and display the dashboard window
plt.tight_layout()
plt.show()