import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_data():
    # Sample Data (Replace with actual cleaned data)
    data = {
        'category': ['A', 'B', 'C', 'A', 'B', 'C'],
        'value': [10, 15, 8, 12, 14, 9]
    }
    df = pd.DataFrame(data)

    # Create plot
    plt.figure(figsize=(8, 5))
    sns.barplot(x=df["category"], y=df["value"])
    plt.title("Category vs Value")

    # Save in static folder
    plot_path = "static/plot.png"
    plt.savefig(plot_path)
    plt.close()

    return plot_path
