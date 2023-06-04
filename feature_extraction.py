from sklearn.feature_extraction.text import CountVectorizer


def extract_features(train_data, test_data):
    vectorizer = CountVectorizer()

    # Fit the vectorizer and transform the data
    X_train = vectorizer.fit_transform(train_data['input'])
    X_test = vectorizer.transform(test_data['input'])

    return X_train, X_test, vectorizer
