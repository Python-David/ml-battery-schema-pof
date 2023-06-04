from data_preparation import generate_data
from feature_extraction import extract_features
from model_training import train_model
from model_evaluation import evaluate_model

# Generate data
train_data, test_data = generate_data()

# Extract features
X_train, X_test, vectorizer = extract_features(train_data, test_data)

# Train model
model = train_model(X_train, train_data['output'])

# Evaluate model
accuracy, y_pred = evaluate_model(model, X_test, test_data['output'])

