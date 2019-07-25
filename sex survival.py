def sex_survival(df):
	return df[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)
	
def get_output_schema():
    return pd.DataFrame({
		'Sex':prep_string(),
		'Survived':prep_decimal(),
    })