import matplotlib.pyplot as plt
import seaborn as sns

# Function 1 

# ==========================

# Sales Distribution Plots

# ==========================

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


# Function 3
def plot_country_sales_bar(data):
    """
    Plot countries contributing up to the given cumulative sales threshold.
    """
    plt.figure(figsize = (12,10))

    sns.barplot(
        data = data,
        y = "Country",
        x = "Sales",
        hue = "Country",
        legend = False,
        palette = "Set2",
        errorbar = None,
        width = 0.9
    )

    plt.title(
        "Top Countries Contributing to Total Sales",
         fontsize = 20,
         fontweight = "bold", 
         pad = 15
    )

    plt.xlabel(
        "Total Sales Revenue", 
        fontsize = 15, 
        fontweight = "bold", 
        labelpad = 15
    )

    plt.ylabel(
        "Country", 
        fontsize = 15, 
        fontweight = "bold", 
        labelpad = 15
    )

    plt.tight_layout()

    return plt.gcf()


# Function 4
def plot_country_sales_pareto_line(data):
    """
    Plot countries contributing up to the given cumulative sales threshold.
    """

    plt.figure(figsize=(15, 6))

    sns.lineplot(
        data = data,
        x = "Country",
        y = "Cum_Percentage",
        color = "red",
        marker = "o",
        linewidth = 2,
        sort = False
    )

    plt.title(
        "Cumulative Sales Contribution of Top Countries", 
        fontsize=14, 
        fontweight="bold", 
        pad=15
    )

    plt.xlabel(
        "Countries", 
        fontsize=10, 
        fontweight="bold", 
        labelpad=10
    )

    plt.ylabel(
        "Cumulative Percentage (%)", 
        fontsize=10, 
        fontweight="bold", 
        labelpad=10
    )

    plt.xticks(
        rotation=45, 
        ha='right'
    )

    return plt.gcf()


# Function 5 
def plot_profit_vs_sales(data):
    """
    Plot profit vs sales graph 
    """

    plt.figure(figsize = (15, 8))

    sns.regplot(
        data = data,
        x = "Profit",
        y = "Sales",
        scatter_kws={"color": "royalblue", "alpha": 0.6, "s": 50}, 
        line_kws={"color": "crimson", "linewidth": 2.5}
    )

    plt.title(
        "Profit VS Sales", 
        fontsize = 20, 
        fontweight = "bold", 
        pad = 15
    )

    plt.xlabel(
        "Profit", 
        fontsize = 20, 
        fontweight = "bold", 
        labelpad = 15
    )

    plt.ylabel(
        "Sales", 
        fontsize = 20, 
        fontweight = "bold", 
        labelpad = 15
    )

    plt.grid(True, linestyle = "--", alpha = 0.5)

    plt.tight_layout()

    return plt.gcf()