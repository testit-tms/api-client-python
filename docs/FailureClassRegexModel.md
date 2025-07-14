# FailureClassRegexModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regex_text** | **str** |  | 
**failure_class_id** | **str** |  | [optional] 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 

## Example

```python
from testit_api_client.models.failure_class_regex_model import FailureClassRegexModel

# TODO update the JSON string below
json = "{}"
# create an instance of FailureClassRegexModel from a JSON string
failure_class_regex_model_instance = FailureClassRegexModel.from_json(json)
# print the JSON string representation of the object
print FailureClassRegexModel.to_json()

# convert the object into a dict
failure_class_regex_model_dict = failure_class_regex_model_instance.to_dict()
# create an instance of FailureClassRegexModel from a dict
failure_class_regex_model_from_dict = FailureClassRegexModel.from_dict(failure_class_regex_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


