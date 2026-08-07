import matplotlib.pyplot as plt
import seaborn as sns

# Function 1 
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


# Function 2
def plot_sub_category_sales(data):
    """
    Plot total sales by sub-category
    """

    plt.figure(figsize = (10, 8))

    sns.barplot(
        data = data,
        y = "Sub.Category",
        x = "Sales",
        palette = "Set2",
        hue = "Sub.Category",
        errorbar = None,
        legend = False,
        width = 0.9
    )

    plt.title(
        "Highest Sales by Product Sub-Category", 
        fontsize = 15, 
        fontweight = "bold", 
        pad = 15)

    plt.ylabel(
        "Product Sub-Category", 
        fontsize = 10, 
        fontweight = "bold", 
        labelpad = 15
    )

    plt.xlabel(
        "Total Sales Revenue", 
        fontsize = 10, 
        fontweight = "bold", 
        labelpad = 15
    )

    plt.tight_layout()
    
    return plt.gcf()   