from jsonschema import validate
import json
import yaml
import os
from datetime import datetime


def convert_datetime_to_string(data):
    if isinstance(data, dict):
        return {k: convert_datetime_to_string(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_datetime_to_string(v) for v in data]
    elif isinstance(data, datetime):
        return data.isoformat()
    else:
        return data


schema = json.load(open('schemas/ht.json'))

for path, directories, files in os.walk('fixtures'):
    for file in files:
        current_map = yaml.safe_load(open(f'fixtures/{file}'))
        current_map = convert_datetime_to_string(current_map)
        validate(current_map, schema=schema)
