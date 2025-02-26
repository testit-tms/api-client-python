# SharedStepResultApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_id** | **str** |  | 
**outcome** | **str** |  | 

## Example

```python
from testit_api_client.models.shared_step_result_api_model import SharedStepResultApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of SharedStepResultApiModel from a JSON string
shared_step_result_api_model_instance = SharedStepResultApiModel.from_json(json)
# print the JSON string representation of the object
print(SharedStepResultApiModel.to_json())

# convert the object into a dict
shared_step_result_api_model_dict = shared_step_result_api_model_instance.to_dict()
# create an instance of SharedStepResultApiModel from a dict
shared_step_result_api_model_from_dict = SharedStepResultApiModel.from_dict(shared_step_result_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


