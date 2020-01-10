import json


class QueryBuilder(object):
    def __init__(self, json_input):
        self.json_input = json_input

    def insert_values(self, mapping):
        def json_traverser(data):
            if isinstance(data, dict):
                for k, v in data.items():
                    if isinstance(v, dict):
                        json_traverser(v)
                    elif isinstance(v, list):
                        json_traverser(v)
                    else:
                        pass  # ignore recursive call for base types
                    if k in mapping:
                        data[k] = mapping[k]
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        json_traverser(item)
                    elif isinstance(item, list):
                        json_traverser(item)
                    else:
                        pass  # ignore recursive call for base types
            else:
                pass  # ignore recursive call for base types
        json_traverser(self.json_input)

    def get_query(self):
        return json.dumps(self.json_input)
