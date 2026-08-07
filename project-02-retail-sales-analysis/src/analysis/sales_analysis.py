# Function 1
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