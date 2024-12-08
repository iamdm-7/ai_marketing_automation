import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st

from scripts.data_preprocessor import load_and_preprocess_data
from scripts.analytics import calculate_metrics
import pandas as pd


# Load data
data = load_and_preprocess_data("data/campaign_data.csv")

# Streamlit dashboard
st.title("AI Marketing Automation Dashboard")
st.write("### Campaign Data")
st.dataframe(data)

# Key metrics
st.write("### Key Metrics")
metrics = calculate_metrics(data)
st.json(metrics)

# Visualization
st.write("### Campaign Performance")
st.bar_chart(data[['CTR', 'ROAS']])
