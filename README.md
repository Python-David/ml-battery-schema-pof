# Proof-of-Concept (POC): Schema Transformation for ML Model

This repository contains a Proof-of-Concept (POC) for a larger project aimed at transforming diverse data schemas into a common schema using machine learning. The ultimate goal of the larger project is to handle schema transformations in a real-world scenario where different data sources may have varied and complex data formats. This POC provides a simplistic view of the larger project.

The specific problem tackled in this POC is transforming different battery data schemas into a common schema.

The project is organized in a modular fashion, with different scripts performing distinct tasks. Below are the main steps followed in the POC and their corresponding scripts.

## Project Steps & Scripts

1. **Data Preparation (`data_preparation.py`):** This step involves defining the common schema and the various input schemas. The schemas are then paired as input-output pairs and divided into a training set and a testing set. The training set is used for model training, while the testing set is used for model evaluation.

2. **Feature Extraction (`feature_extraction.py`):** The input schemas (in JSON string format) are converted into a numerical representation that can be used by a machine learning model. This is done using the `CountVectorizer` from Scikit-learn which converts text into a matrix of token counts.

3. **Model Training:** We use a Decision Tree Classifier model from scikit-learn for training. After training, we use `joblib` to save the trained model to disk for future use. `joblib` is a Python library often used in machine learning for its efficient handling of large data and for its ability to persist trained models to disk and load them back into memory when required. The line `joblib.dump(model, 'model.joblib')` is using the `dump` function of `joblib` to serialize the trained model object and save it to a file named 'model.joblib'. To load the saved model back into memory, use `joblib.load('model.joblib')`.

4. **Model Evaluation (`model_evaluation.py`):** The trained model's performance is evaluated on the testing set. This provides an indication of how well the model is likely to perform on unseen data.

The main script (`main.py`) executes the entire workflow by calling the functions from each of the scripts in the order of the steps described above.

## Relation to Larger Project

This POC illustrates several key steps that will be necessary in the larger project:

1. **Data Preparation:** In the larger project, we'll need to handle many more schemas, and the data will not be hardcoded but will come from an external source. However, the basic principle of generating input-output pairs for the model to learn from will remain the same.

2. **Feature Extraction:** While we used a simple CountVectorizer here, in the larger project, we may need a more complex feature extraction process to handle the variety and complexity of the input schemas.

3. **Model Training:** The POC uses a simple Decision Tree Classifier, but the final project might require a more complex model to accurately learn the mapping from the variety of input schemas to the unified output schema. The use of `joblib` to save and load the model will be critical in the larger project to avoid re-training the model every time.

4. **Model Evaluation:** Evaluating model performance is a crucial step in any machine learning project. In the larger project, we'll likely need more sophisticated evaluation metrics and techniques given the complexity of the task.

By developing and testing these steps in a simplified context, this POC provides a foundation for the development of the larger project. 
## Running the Scripts

To execute the scripts, follow the steps below:

1. Clone the repository: `git clone <repo-url>`

2. Change to the repository directory: `cd <repo-dir>`

3. Install dependencies: `pip install requirements.txt`

4. Run the main script: `python main.py`

The main script will call the functions in the necessary scripts in the correct order.

## Dependencies

This project requires Python and the following Python libraries installed:

- [Pandas](https://pandas.pydata.org/)
- [Scikit-Learn](https://scikit-learn.org/stable/)
- [Joblib](https://joblib.readthedocs.io/en/latest/)

