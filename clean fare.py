def clean_fare(df):
    df['Fare'].fillna(df['Fare'].dropna().median(), inplace=True)
    return df

def get_output_schema():
    return pd.DataFrame({
        'TestData': prep_int(),
        'AgeBands': prep_int(),
        'EmbarkedNum': prep_int(),
        'Pclass': prep_int(),
        'Survived': prep_int(),
        'SexNum':prep_int(),
        'TitleNum': prep_int(),
        'Fare': prep_decimal(),
        'FamilySize': prep_int(),
        'IsAlone': prep_int(),
    })