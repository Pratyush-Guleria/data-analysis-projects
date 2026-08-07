# Function 1
def category_sales(df):
    """
    Returns total sales grouped by category.
    """

    return (
        df.groupby("Category")["Sales"]
          .sum()
          .sort_values(ascending = False)
          .reset_index()
    )


# Function 2
def sub_category_sales(df):
    """
    Returns total sales grouped by sub-category.
    """
    return (df.groupby("Sub.Category")["Sales"]
            .sum()
            .sort_values(ascending = False)
            .reset_index()
    )


# Function 3
def get_top_sales_countries(df, threshold = 0.8):
    """
    Return countries contributing up to the given cumulative sales threshold.
    """

    countries_sales_df = (
        df.groupby("Country")["Sales"]
        .sum()
        .sort_values(ascending = False)
        .reset_index()
    )

    cumulative_ratio = (
        countries_sales_df["Sales"].cumsum()
        / countries_sales_df["Sales"].sum()
    )

    return countries_sales_df[cumulative_ratio <= threshold]