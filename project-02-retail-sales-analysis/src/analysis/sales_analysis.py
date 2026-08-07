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
def get_top_sales_countries(df, threshold=0.8):
    """
    Return countries contributing up to the given cumulative sales threshold.
    """

    country_sales_df = (
        df.groupby("Country")["Sales"]
          .sum()
          .sort_values(ascending=False)
          .reset_index()
    )

    country_sales_df["Cum_Percentage"] = (
        country_sales_df["Sales"].cumsum()
        / country_sales_df["Sales"].sum()
    ) * 100

    return country_sales_df[
        country_sales_df["Cum_Percentage"] <= threshold * 100
    ]