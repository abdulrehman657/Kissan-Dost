import streamlit as st
import streamlit.components.v1 as components
import joblib
import os
import json
import pandas as pd
from sklearn.model_selection import train_test_split

# Force absolute full-screen configuration
st.set_page_config(page_title="Kisaan Dost AI", layout="wide", initial_sidebar_state="collapsed")

# Aggressive CSS: Removes all Streamlit default UI, borders, and margins
st.markdown("""
    <style>
        /* 1. Hide the top header bar (the white bar in your screenshot) */
        [data-testid="stHeader"] {
            display: none !important;
        }

        /* 2. Hide the sidebar toggle/menu */
        [data-testid="stSidebar"] {
            display: none !important;
        }

        /* 3. Force the main container to consume the entire viewport */
        .main, .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            max-width: 100% !important;
            height: 100vh !important;
            overflow: hidden !important;
        }

        /* 4. Ensure no scrollbar appears on the Streamlit container itself */
        [data-testid="stAppViewContainer"] {
            overflow: hidden !important;
        }

        /* 5. The Iframe itself */
        iframe {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
            z-index: 999999 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Define paths relative to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'crop_model.pkl')
HTML_PATH = os.path.join(BASE_DIR, 'kisaan-dost.html')
DATA_PATH = os.path.join(BASE_DIR, 'pak_crop_data.csv')

if os.path.exists(MODEL_PATH) and os.path.exists(HTML_PATH) and os.path.exists(DATA_PATH):
    model = joblib.load(MODEL_PATH)

    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=['Yield_Maunds'])
    y = df['Yield_Maunds']
    feature_order = list(X.columns)

    # Reproduce the exact split used in train_model.py so R2/RMSE reflect
    # genuine held-out performance, not training-set fit.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    r2 = float(model.score(X_test, y_test))
    residuals = y_test.values - model.predict(X_test)
    rmse = float((residuals ** 2).mean() ** 0.5)

    intercept = float(model.intercept_)
    coefficients = {name: float(c) for name, c in zip(feature_order, model.coef_)}

    stats = X.describe().T[['min', 'max', 'mean', 'std']]
    feature_stats = {
        name: {k: float(v) for k, v in row.items()}
        for name, row in stats.iterrows()
    }
    yield_stats = {k: float(v) for k, v in y.describe()[['min', 'max', 'mean']].items()}

    model_payload = {
        "featureOrder": feature_order,
        "coefficients": coefficients,
        "intercept": intercept,
        "r2": r2,
        "rmse": rmse,
        "featureStats": feature_stats,
        "yieldStats": yield_stats,
    }

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html_content = f.read()

    js_vars = f"""
    <script>
        window.MODEL_DATA = {json.dumps(model_payload)};
    </script>
    """

    final_html = html_content.replace("// __INJECT_MODEL_DATA__", js_vars)

    components.html(final_html, height=1080, scrolling=True)
else:
    st.error(
        "Missing files. Check if 'crop_model.pkl', 'pak_crop_data.csv' and "
        "'kisaan-dost.html' are in the same folder as app.py."
    )
