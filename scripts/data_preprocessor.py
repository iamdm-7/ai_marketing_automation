import pandas as pd

def load_and_preprocess_data(file_path):
    """Load and preprocess the campaign data."""
    data = pd.read_csv(file_path)
    # Add calculated metrics for analysis
    data['CTR'] = (data['Clicks'] / data['Impressions']) * 100
    data['CPA'] = data['Spend'] / data['Conversions']
    data['ROAS'] = data['Revenue'] / data['Spend']
    return data
