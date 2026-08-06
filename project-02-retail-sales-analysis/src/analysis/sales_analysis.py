def category_sales(df):
    """
    Returns total sales grouped by category.
    """

    return (
        df.groupby("Category")["Sales"]
          .sum()
          .sort_values(ascending=False)
          .reset_index()
    )