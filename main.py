from scripts.data_preprocessor import load_and_preprocess_data
from scripts.analytics import calculate_metrics
from scripts.decision_agent import apply_rules
from scripts.report_generator import generate_report
from scripts.visualization import plot_metrics

# Load data
data = load_and_preprocess_data("data/campaign_data.csv")

# Analyze data
metrics = calculate_metrics(data)
print("Metrics:", metrics)

# Apply decision rules
decisions = apply_rules(data)
print("Decisions:", decisions)

# Generate report
report = generate_report(data, decisions, "data/campaign_report.csv")
print("Report saved to data/campaign_report.csv")

# Plot metrics
plot_metrics(data)
