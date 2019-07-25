def pclass_survival(df):
	return df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)
	
def get_output_schema():
    return pd.DataFrame({
		'Pclass':prep_int(),
		'Survived':prep_decimal(),
    })