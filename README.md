# Transactions Risk Analysis Using ML

![](https://raw.githubusercontent.com/RahulSolra/Transactions-Risk-Analysis/refs/heads/main/Power%20BI%20Dashboard.png)

![](https://raw.githubusercontent.com/RahulSolra/Transactions-Risk-Analysis/refs/heads/main/Streamlit%20Dashboard.png)

## Project Overview

The **Transactions Risk Analysis** project aims to predict and detect fraudulent credit card transactions in real-time. This prediction is made by analyzing a dataset containing various transaction parameters and anonymized features. The project involves assessing 30 distinct variables, including the transaction time, the transaction amount in USD, and 28 principal component analysis (PCA) transformed features. The primary objective is to understand the hidden patterns that differentiate legitimate transactions from fraudulent ones and to develop a highly accurate machine-learning model (achieving 97% training and 95% testing accuracy) to flag high-risk activity. Additionally, the project integrates this model into an interactive Streamlit dashboard to allow for quick, user-friendly fraud evaluation and confidence scoring.

#### Data Dictionary

| Variable                  | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| Time                      | Number of seconds elapsed between the transaction and the first transaction |
| V1 - V28                  | Anonymized variables resulting from a PCA transformation representing transaction aspects |
| Amount                    | Transaction amount in USD                                                   |
| Class                     | Status of the transaction (0 = Legitimate, 1 = Fraudulent)                  |

## Conclusion

The **Transactions Risk Analysis** project provides valuable insights into fraudulent financial behavior and offers a robust predictive tool to aid institutions in securing their transaction pipelines. The project's outcomes contribute to a more secure, efficient, and reliable financial ecosystem. The project's conclusion emphasizes the following key points:

1. **Real-Time Fraud Detection:** The project's predictive model and interactive dashboard enable the immediate classification of transactions, streamlining the security review process and drastically reducing the time it takes to identify fraudulent activity.

2. **Informed Risk Assessment:** By analyzing the PCA-transformed features and transaction amounts, the project empowers financial decision-makers to rely on data-driven confidence metrics (probability scores) rather than manual reviews, enhancing the overall accuracy of fraud detection.

3. **Enhanced Financial Security:** The ability to accurately catch high-risk transactions strengthens the institution's security posture, leading to a safer environment for consumers and building trust in the payment system.

4. **Proactive Risk Mitigation:** Understanding the variables that correlate with fraudulent transactions allows banks to manage and mitigate financial risk proactively, resulting in a significantly reduced risk of chargebacks and monetary losses.

In conclusion, the **Transactions Risk Analysis** project contributes to a more secure transaction processing system, superior risk management, and improved financial safety within the banking and credit sector.
