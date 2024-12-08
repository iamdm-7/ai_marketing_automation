def calculate_metrics(data):
    """Calculate key metrics."""
    metrics = {
        "average_ctr": data['CTR'].mean(),
        "average_roas": data['ROAS'].mean(),
        "total_spend": data['Spend'].sum(),
        "total_revenue": data['Revenue'].sum(),
    }
    return metrics
