import pandas as pd 
import numpy as np 

np.random.seed(42)
n_samples = 1000

data = {
    'Rainfall_mm': np.random.uniform(150,600,n_samples),
    'GDD_HeatUnits': np.random.uniform(1200, 2500,n_samples),
    'Solar_Radiation' : np.random.uniform(15,30,n_samples),
    'Soil_pH' : np.random.uniform(6.2,8.8,n_samples),
    'Clay_Percent' : np.random.uniform(10,50,n_samples),
    'Sand_Percent': np.random.uniform(10, 45, n_samples),
    'Organic_Carbon': np.random.uniform(0.3, 1.2, n_samples),
    'Nitrogen_Base': np.random.uniform(20, 80, n_samples),
    'Phosphorus_Base': np.random.uniform(5, 25, n_samples),
    'Urea_Bags': np.random.randint(0, 6, n_samples),
    'DAP_Bags': np.random.randint(0, 4, n_samples),
    'Water_Source': np.random.choice([0, 1, 2], n_samples),
    'Seed_Type': np.random.choice([0, 1], n_samples),
    'Land_Size_Acres': np.random.uniform(1, 25, n_samples)    
}

df = pd.DataFrame(data)

# Upgraded "Secret Law of Nature" equation
df['Yield_Maunds'] = (
    15                               # 1. Base minimum yield if nothing else works
    + (df['Rainfall_mm'] * 0.02)     # 2. More rain = more crop growth
    + (df['Urea_Bags'] * 4.5)        # 3. Nitrogen fertilizer boosts height
    + (df['DAP_Bags'] * 3.5)         # 4. NEW: Phosphorus fertilizer boosts root strength
    - (df['Soil_pH'] * 3.0)          # 5. High alkalinity/saltiness actively damages yield
    + (df['Organic_Carbon'] * 12.0)  # 6. NEW: Rich, healthy organic soil adds massive yield
    + (df['Seed_Type'] * 8.0)        # 7. NEW: Using Certified Branded Seeds adds 8 clean Maunds
    + (df['Water_Source'] * 3.5)     # 8. NEW: Canal (1) or Tube-well (2) give a big boost over Rain-fed (0)
    + (df['Clay_Percent'] * 0.1)     # 9. NEW: Clay helps retain moisture slightly
    - (df['Sand_Percent'] * 0.05)    # 10. NEW: Too much sand drains water away completely
    + np.random.normal(0, 1.5, n_samples) # 11. Real-world chaos/unpredictable events
)

df.to_csv('pak_crop_data.csv', index=False)

print("PAK FARM Dataset Created Successfully")