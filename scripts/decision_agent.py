def apply_rules(data):
    """Apply decision-making rules to optimize campaigns."""
    decisions = []
    for _, row in data.iterrows():
        decision = {"Campaign ID": row["Campaign ID"], "Action": "No Action"}
        if row['CTR'] < 1:
            decision["Action"] = "Pause Campaign (Low CTR)"
        elif row['ROAS'] > 4:
            decision["Action"] = "Increase Budget (High ROAS)"
        elif row['ROAS'] < 1.5:
            decision["Action"] = "Decrease Budget (Low ROAS)"
        decisions.append(decision)
    return decisions
