import matplotlib.pyplot as plt

def plot_metrics(data):
    """Plot key campaign metrics."""
    plt.figure(figsize=(10, 6))
    plt.bar(data['Campaign ID'], data['CTR'], color='blue', label='CTR (%)')
    plt.bar(data['Campaign ID'], data['ROAS'], color='green', alpha=0.5, label='ROAS')
    plt.xlabel("Campaign ID")
    plt.ylabel("Metrics")
    plt.title("Campaign Performance")
    plt.legend()
    plt.show()
