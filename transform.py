import json

def transform_api_response(data: list, field_map: dict) -> list:
    """
    Transforms a list of API responses based on the field map configuration.
    :param data: The list of original API responses.
    :param field_map: The field mapping configuration.
    :return: The list of transformed API responses.
    """
    transformed_data = []

    for item in data:
        transformed_item = {}

        for field, rules in field_map.items():
            # Check if the field exists in the original data
            if field in item:
                # If 'new_key' is provided, rename the field
                new_key = rules.get("new_key", field)
                transformed_item[new_key] = item[field]

            elif rules.get("required", False):
                # If the field is required but missing, raise an error
                raise ValueError(f"Missing required field: {field}")

        transformed_data.append(transformed_item)

    return transformed_data
