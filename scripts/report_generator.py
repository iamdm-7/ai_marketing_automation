import pandas as pd

def generate_report(data, decisions, output_path):
    """Generate a report summarizing actions taken."""
    decision_df = pd.DataFrame(decisions)
    report = data.merge(decision_df, on="Campaign ID")
    report.to_csv(output_path, index=False)
    return report
