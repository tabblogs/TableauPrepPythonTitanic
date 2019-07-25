def log_reg(df):

    print(df)

    from sklearn.linear_model import LogisticRegression
    train_df = df.query('TestData==0')
    # print(train_df)
    test_df = df.query('TestData==1')
    # print(test_df)

    X_train = train_df.drop("Survived", axis=1)
    Y_train = train_df["Survived"]

    X_test  = test_df.drop("Survived", axis=1).copy()
    X_train.shape, Y_train.shape, X_test.shape

    logreg = LogisticRegression()

    logreg.fit(X_train, Y_train)
    Y_pred = logreg.predict(X_test)
    acc_log = round(logreg.score(X_train, Y_train) * 100, 2)
    print(acc_log)
    lr_score = pd.DataFrame(data={'algorithm':['Logistic Regression'],'score':[acc_log]})

    # find coefficient for each feature
    coeff_df = pd.DataFrame(train_df.columns.delete(0))
    coeff_df.columns = ['Feature']
    coeff_df["Correlation"] = pd.Series(logreg.coef_[0])
    coeff_df.sort_values(by='Correlation', ascending=False)
    print(coeff_df)

    return lr_score
    

def get_output_schema():
    return pd.DataFrame({
        'algorithm': prep_string(),
        'score': prep_decimal(),
    })