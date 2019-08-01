def age_survival(df):
    train_df = df.query('TestData==0')
    return_df = train_df[['Age', 'Survived']].groupby(['Age'], as_index=False).mean().sort_values(by='Survived', ascending=False)
    print(return_df)
    return return_df

def get_output_schema():
    return pd.DataFrame({
		'Age':prep_decimal(),
		'Survived':prep_decimal(),
    })