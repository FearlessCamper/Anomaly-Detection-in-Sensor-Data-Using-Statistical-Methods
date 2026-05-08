# Air Quality Analysis and Anomaly Detection Using Statistical Methods

This project was developed to perform Exploratory Data Analysis (EDA) on an Air Quality dataset using classical statistical methods and to compare the effects of different data imputation techniques on anomaly detection.

## 📋 Project Summary and Methodology

Within the scope of the project, after cleaning the sensor errors (`-200` values), the analysis process was carried out through two different scenarios:

1.  **Scenario 1 (Row Deletion - Dropna):** Rows containing missing data were completely removed from the dataset. While this method results in data loss, it preserves the natural distribution of the existing data.
2.  **Scenario 2 (Mean Imputation):** Missing values were filled with the mean of their respective columns. This method maintains data integrity (sample size) but may artificially reduce statistical variance (standard deviation).

The following analyses were performed for both scenarios:
- **Normal Distribution Estimation:** Calculation of Mean ($\mu$) and Standard Deviation ($\sigma$).
- **Z-Score and 68-95-99.7 Rule:** Evaluation of conformity to the theoretical normal distribution.
- **Normality Tests:** Shapiro-Wilk test and Q-Q Plot visualization.
- **Anomaly Detection:** Identification of outliers satisfying the condition $|Z| > 3$.
- **Confidence Intervals:** 95% confidence interval estimation for population parameters.

## ⚙️ Requirements

**Python 3.8+** is required to run the project. Necessary libraries:
- `pandas`, `numpy`, `scipy`, `matplotlib`, `seaborn`

## 🚀 Installation and Usage

```bash
# 1. Install the libraries
pip install -r requirements.txt

# 2. Run the script
python project_code.py
```

---

## 📊 Exploratory Data Analysis (EDA) Visuals

To understand the raw structure of the data, the analysis process was supported by the following visualizations based on Scenario 1 (Clean Data):

| Distribution Analysis | Relationship Analysis |
| :--- | :--- |
| ![Temperature Distribution](Ekran%20Alıntısı.PNG) | ![Temp vs Humidity Relationship](Ekran%20Alıntısı2.PNG) |

| Outliers (Boxplot) | Correlation Heatmap |
| :--- | :--- |
| ![CO Outliers](Ekran%20Alıntısı3.PNG) | ![Heatmap](Ekran%20Alıntısı4.PNG) |

---

## 📈 Comparison of Results

### Normality and Q-Q Plot
The conformity of the data to the normal distribution line was tested for both scenarios. The following plot illustrates the deviation in the tails of the distribution:
![Q-Q Plot](Figure_2.png)

### Statistical Inference
The analysis revealed that **filling missing data with the mean (Scenario 2)** artificially narrows the standard deviation and causes the data to "spike" at the center. This situation changes the anomaly detection thresholds, leading to different results. In classical statistical analysis, it is concluded that the **Scenario 1 (Deletion)** method is more reliable as it does not distort the underlying data distribution.
