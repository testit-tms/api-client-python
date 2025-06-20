# UpdateStepApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Step unique internal identifier | 
**action** | **str** | Action applied by user | [optional] 
**expected** | **str** | Expected system reaction | [optional] 
**test_data** | **str** | Test data for step | [optional] 
**comments** | **str** | Comments for step | [optional] 
**work_item_id** | **str** | Unique identifier of workitem which relates to the step | [optional] 

## Example

```python
from testit_api_client.models.update_step_api_model import UpdateStepApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStepApiModel from a JSON string
update_step_api_model_instance = UpdateStepApiModel.from_json(json)
# print the JSON string representation of the object
print(UpdateStepApiModel.to_json())

# convert the object into a dict
update_step_api_model_dict = update_step_api_model_instance.to_dict()
# create an instance of UpdateStepApiModel from a dict
update_step_api_model_from_dict = UpdateStepApiModel.from_dict(update_step_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


