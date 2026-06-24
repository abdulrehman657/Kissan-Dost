# Kisaan Dost: Smart Yield Optimizer 🌾

Kisaan Dost is an end-to-end precision agriculture platform built to practice and demonstrate the deployment of a **Multiple Variable Linear Regression** model. The application replaces traditional agricultural guesswork with an engineering pipeline that analyzes complex soil chemistry, fertilizer metrics, and real-time satellite telemetry to accurately forecast and optimize crop yields.

---

## 📉 The Problem
Traditional farming practices often fail to mathematically account for three silent yield-killers:
* **Soil Alkalinity:** Elevated soil pH levels actively lock up nutrients in the dirt, starving the crop.
* **Fertilizer Mismatch:** Mismanaging the ratio of Nitrogen (Urea) to Phosphorus (DAP) limits optimal plant growth.
* **Climate Volatility:** Failing to track heat accumulation and seasonal rainfall trends causes massive drop-offs in final harvest volumes.

---

## 🧠 The Machine Learning Core
This project serves as a comprehensive practice in feature evaluation, data simulation, and model deployment using Multiple Variable Linear Regression:
* **The Dataset:** Maps a 1,000-sample matrix containing 14 separate environmental, soil, and human input variables.
* **Isolating Signal from Noise:** The regression engine functions as a mathematical filter, evaluating all 14 parameters simultaneously to strip out background noise and isolate true biological triggers.
* **Mathematical Weighting:** The trained model captures the precise ecological weights of the system—learning how Nitrogen boosts plant height, how Phosphorus expands root structures, and exactly how much elevated pH scales down final outputs.

---

## 🛠️ Tech Stack
* **Data Manipulation:** Pandas
* **Machine Learning & Modeling:** Scikit-Learn
* **Model Serialization:** Joblib (`crop_model.pkl`)
* **Live Telemetry:** Requests API
* **Web UI Framework:** Streamlit

---

## 🎨 UI Engineering & UX Design
The frontend bypasses standard vertical templates in favor of a clean, enterprise-grade **wide-layout dashboard** engineered for maximum usability:
* **Split-Column Control Panel:** Column 1 isolates geographic land and irrigation profiles, while Column 2 handles chemical and genetic inputs.
* **Live Weather Integration:** The backend connects to the **Open-Meteo API**. It maps regional selections to exact GPS coordinates, fetches live weather conditions, and dynamically applies climate modifiers to the prediction model on the fly.
* **Clutter Reduction:** Telemetry is processed silently in the background instead of cluttering the screen with real-time metrics that do not impact long-term harvest windows.

---

## 📊 System Outputs & Features
* **Dual Metric Cards:** Displays clean statistical blocks tracking both Yield Density (Maunds per Acre) and Total Volume Forecast (calculated dynamically against total land size).
* **Genetic Strain Tracking:** Successfully maps the financial and biological impact of biotechnology, proving how switching to high-quality certified seeds scales up the calculated performance ceiling.
* **Automated Advisory System:** Features an intelligent feedback engine that reads the user's specific input matrix and generates live recommendations to optimize farming strategies.

---

## 📁 Project Structure
* `generate_data.py`: The data simulator utilizing real agricultural biology formulas to build the dataset.
* `train_model.py`: The training pipeline that isolates features, evaluates regression coefficients, and exports the model brain.
* `plot.py`: A visualization script using Matplotlib to map model accuracy (Actual vs. Predicted) and chart feature weights.
* `app.py`: The production web application featuring live API integration and the wide-layout dashboard.
