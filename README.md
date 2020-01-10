# Automation Utilities
Utilities that will help in developing and maintaining automation frameworks
## JSON Utils

Update values in JSON request

### Usage

```python
from json_utils import QueryBuilder

with open('example.json', 'r') as f:
    json_example = json.load(f)

query = QueryBuilder(json_example)
d = {"mrn": 12345, "first": "jane", "postalCode": 413305}

query.insert_values(d)
modified_json = query.get_query()

print(modified_json)
```
### Input JSON query
```
#example.json
{
    "tag": "post",
    "body": {
      "patient": {
        "site": [
          {
            "code": "string",
            "mrn": "string"
          }
        ],
        "email": [
          "string"
        ],
        "addresses": [
          {
            "line1": "string",
            "line2": "string",
            "city": "string",
            "state": "string",
            "postalCode": "string"
          }
        ],
        "names": [
          {
            "first": "jane",
            "middle": "string",
            "last": "string",
            "suffix": "string"
          }
        ]
      }
    }
  }
```
### Output JSON query
```
{
    "tag": "post",
    "body": {
      "patient": {
        "site": [
          {
            "code": "string",
            "mrn": 12345
          }
        ],
        "email": [
          "string"
        ],
        "addresses": [
          {
            "line1": "string",
            "line2": "string",
            "city": "string",
            "state": "string",
            "postalCode": 413305
          }
        ],
        "names": [
          {
            "first": "string",
            "middle": "string",
            "last": "string",
            "suffix": "string"
          }
        ]
      }
    }
  }
```