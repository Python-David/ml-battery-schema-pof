import joblib
from sklearn.tree import DecisionTreeClassifier


def train_model(X_train, y_train):
    model = DecisionTreeClassifier()

    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, 'model.joblib')

    return model
