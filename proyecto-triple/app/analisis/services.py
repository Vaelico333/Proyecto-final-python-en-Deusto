from flask import current_app
import pandas as pd

def load_data():
    """Load data from the CSV file."""
    data_path = current_app.config['DATA_PATH']
    return pd.read_csv(data_path)

def analyze_data(data):
    """Perform analysis on the loaded data."""
    analysis_result = data.groupby('column_name').size()
    return analysis_result

def save_analysis_results(results):
    """Save analysis results to a text file."""
    with open(current_app.config['ANALYSIS_STORE'], 'w') as f:
        f.write(results.to_json())  

def get_analysis_results():
    """Load and return analysis results from the text file."""
    with open(current_app.config['ANALYSIS_STORE'], 'r') as f:
        return pd.read_json(f.read())