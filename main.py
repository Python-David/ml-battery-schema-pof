import json

# Define the transformation rules
transformation_rules = {
    "battery_level": ["battery_level", "power.level", "Battery.Level", "batLevel", "energy.currentLevel"],
    "battery_status": ["battery_status", "power.status", "Battery.Status", "batStatus", "energy.status"],
    "voltage": ["battery_info.voltage", "battery.voltage", "Battery.Information.Voltage", "batDetails.batVoltage",
                "energy.details.voltage"],
    "capacity": ["battery_info.capacity", "battery.capacity", "Battery.Information.Capacity", "batDetails.batCapacity",
                 "energy.details.capacity"]
}


# Function to extract data based on transformation rules
def extract_data(input_schema, rules):
    extracted_data = {}
    for key in input_schema.keys():
        for rule_key, rule_values in rules.items():
            for rule_value in rule_values:
                rule_parts = rule_value.split('.')
                if key.lower() == rule_parts[0].lower():
                    if len(rule_parts) > 1:
                        if isinstance(input_schema[key], dict):
                            extracted_data[rule_key] = extract_data(input_schema[key],
                                                                    {rule_key: ['.'.join(rule_parts[1:])]})
                    else:
                        extracted_data[rule_key] = input_schema[key]
    return extracted_data


# Function to transform the input schema to the output schema
def transform_schema(input_schema, rules, schema_name="ML_battery_schema", schema_version="1.0"):
    extracted_data = extract_data(input_schema, rules)

    output_schema = {
        "schema_name": schema_name,
        "schema_version": schema_version,
        "data": {
            "battery_level": extracted_data.get("battery_level"),
            "battery_status": extracted_data.get("battery_status"),
            "schema_specific_properties": {
                "voltage": extracted_data.get("voltage"),
                "capacity": extracted_data.get("capacity"),
            }
        }
    }

    return output_schema


# Sample input schema
example = {
    "battery_level": 80,
    "battery_status": "charged",
    "battery_info": {
        "voltage": 3.7,
        "capacity": "3000mAh"
    }
}

transformed_schema = transform_schema(example, transformation_rules)

# Print pretty JSON
print(json.dumps(transformed_schema, indent=2))
