import matplotlib.pyplot as plt
import seaborn as sns


def plot_category_sales(data):
    """
    Plot total sales by category.
    """

    plt.figure(figsize=(10,6))

    sns.barplot(
        data=data,
        x="Category",
        y="Sales",
        palette="Set2",
        width=0.4,
        errorbar=None,
        hue="Category",
        legend=False
    )

    plt.title(
        "Highest Sales by Product Category",
        fontsize=15,
        fontweight="bold",
        pad=15
    )

    plt.xlabel(
        "Product Categories",
        fontsize=10,
        fontweight="bold",
        labelpad=15
    )

    plt.ylabel(
        "Total Sales Revenue",
        fontsize=10,
        fontweight="bold",
        labelpad=15
    )

    plt.tight_layout()

    return plt.gcf()