def categorical_report(df):
    """
    Return all categorical column names.
    """
    return df.select_dtypes(include = ["object", "category", "str"]).columns.tolist()