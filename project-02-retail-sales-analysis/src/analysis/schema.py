def classify_column(df):

    numerical_cols = df.select_dtypes(include=['number']).columns.tolist()

    categorical_cols = df.select_dtypes(include=['object', 'category', 'str']).columns.tolist()

    datetime_cols = df.select_dtypes(include=['datetime64', 'datetime']).columns.tolist()

    return{
        "numerical"         : numerical_cols,
        "categorical"       : categorical_cols,
        "datetime"          : datetime_cols
    }