# CreateStepApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action applied by user | [optional] 
**expected** | **str** | Expected system reaction | [optional] 
**test_data** | **str** | Test data for step | [optional] 
**comments** | **str** | Comments for step | [optional] 
**work_item_id** | **str** | Unique identifier of workitem which relates to the step | [optional] 

## Example

```python
from testit_api_client.models.create_step_api_model import CreateStepApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStepApiModel from a JSON string
create_step_api_model_instance = CreateStepApiModel.from_json(json)
# print the JSON string representation of the object
print(CreateStepApiModel.to_json())

# convert the object into a dict
create_step_api_model_dict = create_step_api_model_instance.to_dict()
# create an instance of CreateStepApiModel from a dict
create_step_api_model_from_dict = CreateStepApiModel.from_dict(create_step_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


