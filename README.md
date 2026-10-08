# Customer Churn Prediction

Predicting which telecom customers will cancel their contract, using the
IBM Telco Customer Churn dataset (7,043 customers, 21 columns).

## Key findings (EDA)
- Month-to-month customers churn at ~43%, vs ~3% on two-year contracts.
- Churners have a median tenure of ~10 months vs ~38 for loyal customers.
- Churners pay higher monthly bills (median ~80 vs ~64).

## Model results (test set, 1,407 customers)
| Model | ROC-AUC | Recall (churn) | Precision (churn) |
|---|---|---|---|
| Logistic Regression | 0.835 | 0.80 | 0.49 |
| Random Forest | 0.833 | 0.78 | 0.52 |

Logistic regression was chosen: equal performance, easier to explain.
It catches 298 of 374 churners in the test set.

Main churn drivers: month-to-month contracts, short tenure, fibre-optic
internet, electronic-check payment, no online security or tech support.

Note: tenure, MonthlyCharges and TotalCharges are strongly correlated,
so their individual coefficients should not be read causally.

## How to run
pip install -r requirements.txt
python src/download_data.py
Then run notebooks/01_eda.ipynb and notebooks/02_model.ipynb.