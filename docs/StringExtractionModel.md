# StringExtractionModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**exclude** | **List[str]** |  | [optional] 

## Example

```python
from testit_api_client.models.string_extraction_model import StringExtractionModel

# TODO update the JSON string below
json = "{}"
# create an instance of StringExtractionModel from a JSON string
string_extraction_model_instance = StringExtractionModel.from_json(json)
# print the JSON string representation of the object
print StringExtractionModel.to_json()

# convert the object into a dict
string_extraction_model_dict = string_extraction_model_instance.to_dict()
# create an instance of StringExtractionModel from a dict
string_extraction_model_from_dict = StringExtractionModel.from_dict(string_extraction_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


