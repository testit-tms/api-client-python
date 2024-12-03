# SharedStepResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_id** | **str** |  | 
**outcome** | **str** |  | 

## Example

```python
from testit_api_client.models.shared_step_result_model import SharedStepResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of SharedStepResultModel from a JSON string
shared_step_result_model_instance = SharedStepResultModel.from_json(json)
# print the JSON string representation of the object
print(SharedStepResultModel.to_json())

# convert the object into a dict
shared_step_result_model_dict = shared_step_result_model_instance.to_dict()
# create an instance of SharedStepResultModel from a dict
shared_step_result_model_from_dict = SharedStepResultModel.from_dict(shared_step_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


