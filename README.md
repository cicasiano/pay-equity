# 💼 Pay Equity Analysis — IBM HR Dataset

This project explores whether gender or other common employee attributes can statistically explain variation in salary using the IBM HR Analytics Employee Attrition & Performance dataset. The project walks through data cleaning, exploratory data analysis, and regression modeling.

---

## Objective

To determine whether there are statistically significant pay disparities based on gender, job level, education, or tenure after controlling for key job-related factors.

---

## Tools & Methods

- Python (pandas, seaborn, statsmodels)
- One-hot encoding for categorical variables
- Exploratory Data Analysis (histograms, boxplots, correlation matrix)
- Multiple Linear Regression (OLS)
- Hypothesis testing for p-values and confidence intervals

---

## Key Variables

- **Dependent Variable:** `AnnualSalary` (derived from MonthlyIncome)
- **Independent Variables:**
  - `Gender`
  - `JobLevel`
  - `YearsAtCompany`
  - `Education`
  - One-hot encoded `JobRole`

---

## Summary of Results

- No independent variables were statistically significant (p < 0.05).
- R² remained very low even after including job roles: **0.004**
- This suggests that the dataset does **not capture pay patterns**, likely due to being a synthetic data set.
- Demonstration of a framework to conduct pay equity analysis 

---

## Interpretation

In a real-world setting, we would expect job level, role, tenure, and other common human resources/people variables to strongly influence pay. Still, this project illustrates best practices in:

- Preparing data for equity analysis
- Evaluating model fit and assumptions
- Interpreting regression results for non-technical audiences

---

## Project Structure

```
pay_equity_analysis/
├── data/
├── notebooks/
│ ├── 01_data_cleaning.ipynb
│ ├── 02_eda.ipynb
│ ├── 03_regression_analysis.ipynb
├── outputs/
│ ├── charts/
│ ├── model_summary.csv
├── README.md
```

---

## 🧾 Author

Carolann Decasiano  
Master’s in Applied Data Science  
[LinkedIn](https://www.linkedin.com/in/carolann-decasiano/) | [GitHub](https://github.com/cicasiano)