def get_missing_summary(df):
    
    """
    Returns missing values report.
    """

    missing_series = df.isnull().sum()

    return{
        "missing_per_column" : missing_series,
        "total_missing"      : missing_series.sum()
    }