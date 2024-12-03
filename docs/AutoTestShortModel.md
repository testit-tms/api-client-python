# AutoTestShortModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**global_id** | **int** |  | 
**external_id** | **str** |  | 
**project_id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from testit_api_client.models.auto_test_short_model import AutoTestShortModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestShortModel from a JSON string
auto_test_short_model_instance = AutoTestShortModel.from_json(json)
# print the JSON string representation of the object
print(AutoTestShortModel.to_json())

# convert the object into a dict
auto_test_short_model_dict = auto_test_short_model_instance.to_dict()
# create an instance of AutoTestShortModel from a dict
auto_test_short_model_from_dict = AutoTestShortModel.from_dict(auto_test_short_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


