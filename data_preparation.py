import json
import pandas as pd


def load_schema(filename):
    with open(filename) as f:
        return json.load(f)


def generate_data():
    # Load schemas from files
    common_schema = load_schema('schemas/common_schema.json')
    schemas = load_schema('schemas/input_schemas.json')

    # Generate input-output pairs
    input_output_pairs = [(json.dumps(schema), json.dumps(common_schema)) for schema in schemas]

    # Split into training and testing sets
    train_data = pd.DataFrame(input_output_pairs[:4], columns=["input", "output"])
    test_data = pd.DataFrame(input_output_pairs[4:], columns=["input", "output"])

    return train_data, test_data
