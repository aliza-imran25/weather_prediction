# 🌦️ Islamabad Weather Prediction ML App

A machine learning application that predicts **tomorrow's temperature** and **whether rain is likely tomorrow** using historical weather data from Islamabad, Pakistan.

## 📌 Project Overview

This project was built to practice an end-to-end machine learning workflow:

* Data collection
* Data cleaning
* Feature engineering
* Regression
* Classification
* Model evaluation
* Model saving with Joblib
* Streamlit deployment

The project uses historical daily weather data from **2015–2025**.

## 🤖 Machine Learning Models

### Temperature Prediction

A Linear Regression model with cyclical seasonal features was used to predict tomorrow's mean temperature.

**Evaluation:**

| Metric |   Result |
| ------ | -------: |
| MAE    | 0.873 °C |
| RMSE   | 1.138 °C |
| R²     |    0.975 |

### Rain Prediction

A Random Forest Classifier was used to predict whether significant rain would occur the following day.

**Evaluation:**

| Metric    | Result |
| --------- | -----: |
| Accuracy  |  0.779 |
| Precision |  0.688 |
| Recall    |  0.692 |
| F1 Score  |  0.690 |

## 🧠 Features

The models use:

* Mean temperature
* Maximum temperature
* Minimum temperature
* Precipitation
* Rain amount
* Maximum wind speed
* Day-of-year sine
* Day-of-year cosine

The cyclical date features allow the model to represent seasonal patterns more naturally.

## 🛠️ Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit
* Jupyter Notebook

## 📁 Project Structure

```text
weather-prediction/
│
├── data/
├── models/
├── notebooks/
├── src/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd weather-prediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate it on Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## ⚠️ Disclaimer

This project is an educational machine learning application based on historical weather data. Its predictions should not be treated as official weather forecasts.
