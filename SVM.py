def svm(df):

    print(df)

    #from sklearn.linear_model import LogisticRegression
    from sklearn.svm import SVC, LinearSVC

    train_df = df.query('TestData==0')
    # print(train_df)
    test_df = df.query('TestData==1')
    # print(test_df)

    X_train = train_df.drop("Survived", axis=1)
    Y_train = train_df["Survived"]

    X_test  = test_df.drop("Survived", axis=1).copy()
    # X_train.shape, Y_train.shape, X_test.shape

    # logreg = LogisticRegression()

    # logreg.fit(X_train, Y_train)
    # Y_pred = logreg.predict(X_test)
    # acc_log = round(logreg.score(X_train, Y_train) * 100, 2)

    # Support Vector Machines

    svc = SVC()
    svc.fit(X_train, Y_train)
    Y_pred = svc.predict(X_test)
    acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
    print("acc_svc: ",acc_svc)
    svc_score = pd.DataFrame(data={'algorithm':['SVM'],'score':[acc_svc]})
    return svc_score
    

def get_output_schema():
    return pd.DataFrame({
        'algorithm': prep_string(),
        'score': prep_decimal(),
    })