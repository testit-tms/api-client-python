# AutoTestChangeViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**project_id** | **str** |  | 
**external_id** | **str** |  | 
**global_id** | **int** |  | 

## Example

```python
from testit_api_client.models.auto_test_change_view_model import AutoTestChangeViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestChangeViewModel from a JSON string
auto_test_change_view_model_instance = AutoTestChangeViewModel.from_json(json)
# print the JSON string representation of the object
print(AutoTestChangeViewModel.to_json())

# convert the object into a dict
auto_test_change_view_model_dict = auto_test_change_view_model_instance.to_dict()
# create an instance of AutoTestChangeViewModel from a dict
auto_test_change_view_model_from_dict = AutoTestChangeViewModel.from_dict(auto_test_change_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


