from sklearn.metrics import accuracy_score, classification_report


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print('Model accuracy: ', accuracy)
    print(classification_report(y_test, y_pred))

    return accuracy, y_pred
