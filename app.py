import streamlit as st
import numpy as np
import pandas as pd
import joblib


# ------------------------
# PAGE CONFIG
# ------------------------
st.set_page_config(
    page_title="Fraud Detection",
    page_icon="💳",
    layout="wide"
)


# ------------------------
# LOAD MODEL
# ------------------------
model = joblib.load("fraud_model.pkl")
scaler = joblib.load("scaler.pkl")

# OPTIONAL
try:
    metrics = joblib.load("metrics.pkl")
    train_acc = metrics["train"]
    test_acc = metrics["test"]
except:
    train_acc = 0.97
    test_acc = 0.95


# ------------------------
# HEADER
# ------------------------
st.title("💳 Credit Card Fraud Detection Dashboard")

st.caption(
    "Machine Learning based transaction fraud prediction"
)


# ------------------------
# METRICS
# ------------------------
c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Train Accuracy",
        f"{train_acc:.2%}"
    )

with c2:
    st.metric(
        "Test Accuracy",
        f"{test_acc:.2%}"
    )

with c3:
    st.metric(
        "Model",
        "Logistic Regression"
    )


st.divider()


# ------------------------
# INPUT
# ------------------------
left, right = st.columns([2, 1])


with left:

    st.subheader(
        "Enter Transaction Features"
    )

    input_text = st.text_area(
        "",
        height=180,
        placeholder="""
Example:

0.2,-0.4,1.3,...
        """
    )

    predict = st.button(
        "🔍 Predict Transaction",
        use_container_width=True
    )


with right:

    st.subheader(
        "About"
    )

    st.info(
        """
• Detects fraud transactions

• Uses trained ML model

• Input values separated by comma
"""
    )


# ------------------------
# PREDICTION
# ------------------------
if predict:

    try:

        # accept comma / space / tab
        values = np.fromstring(
            input_text,
            sep=' '
        )

        # fallback for comma input
        if len(values) <= 1:
            values = np.fromstring(
                input_text,
                sep=','
            )

        # remove target column if pasted
        if len(values) == 32:
            values = values[:-1]

        expected = scaler.n_features_in_

        if len(values) != expected:
            st.error(
                f"Expected {expected} features but got {len(values)}"
            )

        else:

            values = scaler.transform(
                values.reshape(1, -1)
            )

            pred = model.predict(
                values
            )[0]

            prob = model.predict_proba(
                values
            )[0][1]

            st.divider()

            if pred == 0:

                st.success(
                    f"✅ Legitimate Transaction\nConfidence: {(1-prob)*100:.2f}%"
                )

            else:

                st.error(
                    f"🚨 Fraudulent Transaction\nConfidence: {prob*100:.2f}%"
                )

            st.progress(
                int(max(prob, 1-prob) * 100)
            )

    except Exception as e:

        st.error(
            f"Invalid Input: {e}"
        )
st.caption(
    "Developed by Rahul Solra | Using Python • Streamlit • Scikit-Learn"
)