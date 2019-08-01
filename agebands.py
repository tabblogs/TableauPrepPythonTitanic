def age_bands(df):
    df['AgeBand'] = pd.cut(df['AgeAugmented'], 5)
    # this will fail because the format of the returned age band field is not a string
    return df
	
def get_output_schema():
    return pd.DataFrame({
        'AgeBand': prep_string(),
        'Embarked': prep_string(),
        'Pclass': prep_int(),
        'Survived': prep_bool(),
        'AgeAugmented':prep_int(),
        'Parch': prep_int(),
        'SexNum':prep_int(),
        'TitleNum': prep_int(),
        'SibSp': prep_int(),
        'Fare': prep_int(),
    })
