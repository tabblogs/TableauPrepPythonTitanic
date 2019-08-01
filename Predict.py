def predict_survival(df):
    from sklearn.ensemble import RandomForestClassifier

    train_df = df.query('TestData==0')
    test_df = df.query('TestData==1')

    X_train = train_df.drop("Survived", axis=1)
    Y_train = train_df["Survived"]

    X_test  = test_df.drop("Survived", axis=1).copy()

    random_forest = RandomForestClassifier(n_estimators=100)
    random_forest.fit(X_train, Y_train)
    Y_pred = random_forest.predict(X_test)
    
    X_test['survive_pred']=Y_pred
    return X_test

def get_output_schema():
    return pd.DataFrame({
        'EmbarkedNum': prep_int(),
        'Pclass': prep_int(),
        'FamilySize': prep_int(),
        'AgeBands': prep_int(),
        'SexNum':prep_int(),
        'TitleNum': prep_int(),
        'IsAlone': prep_int(),
        'Fare': prep_decimal(),
        'FareBin': prep_int(),
        'survive_pred': prep_decimal(),
    })