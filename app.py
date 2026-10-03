import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import date
from pathlib import Path


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Weather Prediction",
    page_icon="🌦️",
    layout="centered"
)


# --------------------------------------------------
# LOAD MODELS
# --------------------------------------------------

@st.cache_resource
def load_models():
    model_dir = Path(__file__).resolve().parent / "models"
    temperature = joblib.load(model_dir / "temperature_model.pkl")
    rain = joblib.load(model_dir / "rain_model.pkl")
    return temperature, rain


temperature_model, rain_model = load_models()


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🌦️ Islamabad Weather Prediction")

st.write(
    "Enter today's weather conditions to estimate "
    "tomorrow's temperature and rain probability."
)

st.divider()


# --------------------------------------------------
# DATE
# --------------------------------------------------

selected_date = st.date_input(
    "Select today's date",
    value=date.today()
)


# --------------------------------------------------
# WEATHER INPUTS
# --------------------------------------------------

st.subheader("Today's Weather")

col1, col2 = st.columns(2)

with col1:

    temperature_mean = st.number_input(
        "Mean Temperature (°C)",
        min_value=-10.0,
        max_value=50.0,
        value=25.0,
        step=0.1
    )

    temperature_max = st.number_input(
        "Maximum Temperature (°C)",
        min_value=-10.0,
        max_value=55.0,
        value=30.0,
        step=0.1
    )

    temperature_min = st.number_input(
        "Minimum Temperature (°C)",
        min_value=-20.0,
        max_value=40.0,
        value=18.0,
        step=0.1
    )

with col2:

    precipitation = st.number_input(
        "Precipitation (mm)",
        min_value=0.0,
        max_value=200.0,
        value=0.0,
        step=0.1
    )

    rain = st.number_input(
        "Rain (mm)",
        min_value=0.0,
        max_value=200.0,
        value=0.0,
        step=0.1
    )

    wind_speed = st.number_input(
        "Maximum Wind Speed (km/h)",
        min_value=0.0,
        max_value=150.0,
        value=10.0,
        step=0.1
    )


# --------------------------------------------------
# CREATE CYCLICAL DATE FEATURES
# --------------------------------------------------

day_of_year = selected_date.timetuple().tm_yday

day_of_year_sin = np.sin(
    2 * np.pi * day_of_year / 365
)

day_of_year_cos = np.cos(
    2 * np.pi * day_of_year / 365
)


# --------------------------------------------------
# CREATE INPUT DATAFRAME
# --------------------------------------------------

input_data = pd.DataFrame({
    "temperature_2m_mean": [temperature_mean],
    "temperature_2m_max": [temperature_max],
    "temperature_2m_min": [temperature_min],
    "precipitation_sum": [precipitation],
    "rain_sum": [rain],
    "wind_speed_10m_max": [wind_speed],
    "day_of_year_sin": [day_of_year_sin],
    "day_of_year_cos": [day_of_year_cos]
})


# --------------------------------------------------
# PREDICTION BUTTON
# --------------------------------------------------

st.divider()

if st.button(
    "🔮 Predict Tomorrow's Weather",
    use_container_width=True
):

    # Temperature prediction
    temperature_prediction = temperature_model.predict(
        input_data
    )[0]

    # Rain prediction
    rain_prediction = rain_model.predict(
        input_data
    )[0]

    # Rain probability
    rain_probability = rain_model.predict_proba(
        input_data
    )[0][1]


    # --------------------------------------------------
    # RESULTS
    # --------------------------------------------------

    st.subheader("Tomorrow's Prediction")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🌡️ Predicted Temperature",
            f"{temperature_prediction:.1f} °C"
        )

    with col2:

        if rain_prediction == 1:

            st.metric(
                "🌧️ Rain Prediction",
                "YES"
            )

        else:

            st.metric(
                "☀️ Rain Prediction",
                "NO"
            )


    st.progress(
        float(rain_probability)
    )

    st.write(
        f"Estimated rain probability: "
        f"**{rain_probability * 100:.1f}%**"
    )


    st.info(
        "These predictions are machine-learning estimates "
        "based on historical Islamabad weather data from "
        "2015–2025. They are not official weather forecasts."
    )