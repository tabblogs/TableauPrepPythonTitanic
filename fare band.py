def fare_band(df):
    return str(pd.qcut(df['Fare'], 4))
