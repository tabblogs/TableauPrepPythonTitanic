def family_size(df):
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    return df

def get_output_schema():
    return pd.DataFrame({
        'TestData': prep_int(),
        'AgeBands': prep_int(),
        'Embarked': prep_string(),
        'Pclass': prep_int(),
        'Survived': prep_int(),
        'Parch': prep_int(),
        'SexNum':prep_int(),
        'TitleNum': prep_int(),
        'Title': prep_string(),
        'Name': prep_string(),
        'SibSp': prep_int(),
        'Fare': prep_decimal(),
        'FamilySize': prep_int(),
        'Sex': prep_string(),
        'Age': prep_decimal(),
    })