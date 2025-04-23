import json

def transform_record(record: dict, field_map: dict, required_fields: list) -> dict:
    if not all(field in record for field in required_fields):
        missing = [field for field in required_fields if field not in record]
        print(f"⚠️ Record skipped. Missing required fields: {missing}")
        return None

    return {
        new_key: record[old_key]
        for old_key, new_key in field_map.items()
        if old_key in record
    }

def transform_data_list(data_list: list, config_path: str) -> list:
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)

        field_map = config.get("field_map", {})
        required_fields = config.get("required_fields", [])

        transformed = [
            transformed_record
            for record in data_list
            if (transformed_record := transform_record(record, field_map, required_fields)) is not None
        ]

        return transformed

    except Exception as e:
        print(f"❌ Error during transformation: {e}")
        return []
