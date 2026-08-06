def get_duplicate_report(df):

    """
    Returns total duplicate rows report.
    """
    
    return df.duplicated().sum()