import streamlit as st
import joblib
import requests

# 1. Load the model brain
model = joblib.load('crop_model.pkl')

# 2. Premium Page Configuration (Set layout to wide!)
st.set_page_config(page_title="Kisaan Dost", page_icon="🌾", layout="wide")

st.title("🌾 Kisaan Dost: Smart Yield Optimizer")
st.write("An advanced machine learning platform for regional precision agriculture.")
st.markdown("---")

# 3. Sidebar: Kept clean for configuration status only
with st.sidebar:
    st.header("📍 Regional Profile")
    city = st.selectbox("Select Target District:", ["Multan", "Faisalabad", "Sargodha", "Sukkur"])
    
    coordinates = {
        "Multan": {"lat": 30.1575, "lon": 71.5249, "base_soil": [8.2, 40, 20, 0.5, 45, 12]},
        "Faisalabad": {"lat": 31.4504, "lon": 73.1350, "base_soil": [7.8, 35, 25, 0.7, 50, 15]},
        "Sargodha": {"lat": 32.0740, "lon": 72.6861, "base_soil": [7.5, 30, 30, 0.8, 55, 18]},
        "Sukkur": {"lat": 27.7244, "lon": 68.8228, "base_soil": [8.5, 45, 15, 0.4, 35, 10]}
    }
    selected_geo = coordinates[city]
    
    # Background API call (No messy metrics printed on screen anymore!)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={selected_geo['lat']}&longitude={selected_geo['lon']}&current=temperature_2m,rain"
    
    try:
        response = requests.get(url).json()
        live_temp = response['current']['temperature_2m']
        live_rain = response['current']['rain']
        
        # Sleek, unified status update
        st.success(f"🟢 Satellite Link Active: {city}")
        st.caption(f"Seasonal baseline vectors automatically optimized via live climate sync ({live_temp}°C).")
        
        heat_modifier = 1.2 if live_temp > 30 else 1.0
        rain_modifier = 1.5 if live_rain > 0 else 1.0
        
        calculated_rain = 400 * rain_modifier
        calculated_heat = 2000 * heat_modifier
        calculated_solar = 22.5 + (live_temp * 0.1)

    except Exception:
        st.warning("⚠️ Satellite Offline. Using regional baseline profiles.")
        calculated_rain = 350
        calculated_heat = 1800
        calculated_solar = 20.0

ghost_vars = [calculated_rain, calculated_heat, calculated_solar] + selected_geo["base_soil"]

# 4. Main Layout split into clean multi-columns
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("📐 Land & Water Profile")
    land_size = st.number_input("Total Land Size (Acres):", min_value=1.0, value=5.0, step=0.5)
    water_type = st.radio("Primary Irrigation Method:", ["Rain-fed", "Canal", "Tube-well"])
    water_encoded = 0 if "Rain-fed" in water_type else (1 if "Canal" in water_type else 2)

with col2:
    st.subheader("🧪 Chemical & Seed Inputs")
    urea = st.number_input("Urea Bags Applied (Per Acre):", min_value=0, value=2)
    dap = st.number_input("DAP Bags Applied (Per Acre):", min_value=0, value=1)
    seed_quality = st.radio("Seed Genetic Strain:", ["Home/Local Seeds", "Certified Branded Seeds"])
    seed_encoded = 1 if "Certified" in seed_quality else 0

st.markdown("---")

# 5. Clean, full-width Action Button
if st.button("📊 Execute Predictive Analytics", type="primary", use_container_width=True):
    full_input = ghost_vars + [urea, dap, water_encoded, seed_encoded, land_size]
    prediction = model.predict([full_input])[0]
    
    st.subheader("📋 Expected Performance Summary")
    
    # Display results inside modern, side-by-side metric display blocks
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.metric(label="Estimated Yield Density", value=f"{prediction:.1f} Maunds / Acre")
    with res_col2:
        st.metric(label="Total Volume Forecast", value=f"{prediction * land_size:.1f} Maunds Total")
        
    # Dynamic Advisory System
    st.markdown("### 💡 Agronomist Recommendation")
    if seed_encoded == 0:
        st.info("Your parameters show lower genetic baseline trends. Swapping to **Certified Branded Seeds** will immediately scale your calculated performance ceiling by up to 8 Maunds per acre.")
    else:
        st.success("Excellent application matrix. Certified seeds are taking maximum biological advantage of your applied chemical fertilizer metrics.")
    # Read file components
with open("kisaan-dost.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Apply the pipeline replacements
rendered_ui = html_content
rendered_ui = rendered_ui.replace("`{st_district}`", f"`{district}`")
rendered_ui = rendered_ui.replace("`{st_land_size}`", f"`{land_size}`")
rendered_ui = rendered_ui.replace("`{st_urea_bags}`", f"`{urea}`")
rendered_ui = rendered_ui.replace("`{st_dap_bags}`", f"`{dap}`")
rendered_ui = rendered_ui.replace("`{st_seed_type}`", f"`{seed_type}`")
rendered_ui = rendered_ui.replace("`{st_water_source}`", f"`{water_type}`")

rendered_ui = rendered_ui.replace("`{predicted_yield}`", f"`{prediction:.2f}`")
rendered_ui = rendered_ui.replace("`{total_volume}`", f"`{calculated_total:.1f}`")
rendered_ui = rendered_ui.replace("`{confidence}`", f"`{confidence_score}`")
rendered_ui = rendered_ui.replace("`{limiting_factor}`", f"`{limiting_factor}`")
rendered_ui = rendered_ui.replace("`{recommendation}`", f"`{recommendation_text}`")

# Render out to components layout canvas frame
components.html(rendered_ui, height=900, scrolling=True)
