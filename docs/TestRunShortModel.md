# TestRunShortModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_name** | [**TestRunState**](TestRunState.md) |  | 
**project_id** | **str** |  | 
**test_plan_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 

## Example

```python
from testit_api_client.models.test_run_short_model import TestRunShortModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunShortModel from a JSON string
test_run_short_model_instance = TestRunShortModel.from_json(json)
# print the JSON string representation of the object
print(TestRunShortModel.to_json())

# convert the object into a dict
test_run_short_model_dict = test_run_short_model_instance.to_dict()
# create an instance of TestRunShortModel from a dict
test_run_short_model_from_dict = TestRunShortModel.from_dict(test_run_short_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


