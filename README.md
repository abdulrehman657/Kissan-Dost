# Kisaan Dost: Smart Yield Optimizer 🌾

Kisaan Dost is an end-to-end precision agriculture platform built to practice and demonstrate the deployment of a **Multiple Variable Linear Regression** model. It replaces guesswork with an engineering pipeline that reasons over soil chemistry, fertilizer dosage, and climate variables to forecast — and help optimize — crop yield per acre.

Every number the dashboard shows is traced back to the trained model itself: the predicted yield, the accuracy badge, and the advisory text are all computed live from the model's real coefficients — nothing on screen is scripted or hardcoded.

---

## 📉 The Problem

Traditional farming decisions often ignore three yield-killers that a regression model can quantify precisely:

* **Soil Alkalinity:** Elevated soil pH locks up nutrients in the ground, starving the crop regardless of how much fertilizer is applied.
* **Fertilizer Mismatch:** Getting the Urea (Nitrogen) to DAP (Phosphorus) ratio wrong caps growth even when total fertilizer spend is high.
* **Soil & Climate Blind Spots:** Organic carbon, clay/sand composition, rainfall, and heat accumulation (GDD) all move the yield ceiling — but are rarely tracked or acted on at the field level.

---

## 🧠 The Machine Learning Core

* **The Dataset:** A 1,000-sample matrix spanning 14 environmental, soil, and human-input variables (`pak_crop_data.csv`), generated in `generate_data.py` from real agronomic relationships (rainfall, fertilizer response, soil pH penalty, seed quality boost, etc.).
* **The Model:** A `scikit-learn` `LinearRegression` trained in `train_model.py`, evaluating all 14 features simultaneously to isolate each one's true weight on final yield — serialized to `crop_model.pkl`.
* **Validated, Not Assumed:** On a held-out 20% test split, the model reaches **~98.5% R²** with an RMSE of roughly **1.4 maunds/acre** — both computed live by `app.py` at launch and surfaced directly in the UI, instead of a fabricated "confidence" number.

---

## 🛠️ Tech Stack

* **Data Manipulation:** Pandas
* **Machine Learning & Modeling:** Scikit-Learn
* **Model Serialization:** Joblib (`crop_model.pkl`)
* **Web UI Framework:** Streamlit, rendering a custom Tailwind/vanilla-JS dashboard (`kisaan-dost.html`)

---

## 🎨 UI Engineering & UX Design

The frontend is a dark, glassmorphic dashboard rather than Streamlit's default vertical form layout:

* **Regional Sidebar:** Pick a district (Multan, Faisalabad, Sargodha, Sukkur) to pre-fill realistic starting soil & climate values — every one of those values is still just a regular input feeding the model, so nothing is faked behind the scenes.
* **Field Inputs Panel:** Land size, Urea/DAP dosage (bags per acre), seed quality (standard vs. certified), and water source — clamped to the exact ranges the model was actually trained on, so predictions never extrapolate into nonsense territory.
* **Advanced Soil & Climate Panel:** A collapsible section exposing the remaining trained features (rainfall, GDD heat units, solar radiation, soil pH, clay/sand percent, organic carbon, base nitrogen/phosphorus) for full control over the prediction.
* **Live Yield Meter:** An animated radial gauge scaled to the model's real training-data range, updating instantly as any input changes.

---

## 📊 System Outputs & Features

* **Dual Metric Cards:** Yield Density (maunds/acre) straight from the model, and Total Volume Forecast derived by scaling it against land size.
* **Model Accuracy Badge:** Displays the model's real R² and an honest ± RMSE margin next to the prediction, instead of an invented per-guess "confidence" score.
* **Coefficient-Driven Advisory:** The recommendation engine ranks Urea, DAP, water source, and seed quality by how many maunds/acre of *headroom* each one still has — computed directly from the trained coefficients — then falls back to longer-term soil-health tips (organic carbon, pH amendment) once fertilizer and water are already near-optimal.
* **Dynamic Fertility Index:** A 0–100 soil fertility score built from the same coefficients, weighted by how much yield swing each soil feature is actually responsible for in the model.
