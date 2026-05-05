# Anomaly-Detection-in-Sensor-Data-Using-Statistical-Methods
This project was developed to perform Exploratory Data Analysis (EDA) and Univariate Anomaly Detection on the Air Quality dataset using classical statistical methods.

## 📋 Project Description

Hourly sensor data (such as Temperature, Carbon Monoxide, etc.) collected from an air quality monitoring device were analyzed in this project. Device errors (represented by `-200` values) were cleaned from the dataset, columns with excessive missing data (`NMHC(GT)`) were removed, and the following statistical analyses were applied to the remaining clean data:

- **Normal Distribution Parameter Estimation:** Calculation of the Mean ($\mu$) and Standard Deviation ($\sigma$).
- **Z-Score Transformation:** Standardizing the data to a standard normal distribution.
- **68-95-99.7 Rule (Empirical Rule):** Checking the data distribution's conformity to a theoretical normal distribution.
- **Normality Tests:** Conducting the Shapiro-Wilk statistical test and generating Q-Q Plot visualizations.
- **Anomaly Detection:** Identifying outliers (anomalies) where the absolute value of the Z-score is greater than 3 ($|Z| > 3$).
- **Confidence Intervals:** Calculating the 95% confidence interval for the population mean.

## ⚙️ Requirements

For the project to run smoothly, you must have **Python 3.8 or higher** installed on your system. The core libraries used in this project are:
- `pandas` (Data manipulation and analysis)
- `numpy` (Numerical operations)
- `scipy` (Statistical tests and calculations)
- `matplotlib` & `seaborn` (Data visualization)

## 🚀 Installation and Usage

**Step 1:** Install the required libraries. Open your terminal or command prompt, navigate to the project directory, and run the following command:
```bash
pip install -r requirements.txt
