# SharedStepChangeViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**global_id** | **int** |  | 
**name** | **str** |  | 
**steps** | [**List[WorkItemStepChangeViewModel]**](WorkItemStepChangeViewModel.md) |  | 

## Example

```python
from testit_api_client.models.shared_step_change_view_model import SharedStepChangeViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of SharedStepChangeViewModel from a JSON string
shared_step_change_view_model_instance = SharedStepChangeViewModel.from_json(json)
# print the JSON string representation of the object
print SharedStepChangeViewModel.to_json()

# convert the object into a dict
shared_step_change_view_model_dict = shared_step_change_view_model_instance.to_dict()
# create an instance of SharedStepChangeViewModel from a dict
shared_step_change_view_model_from_dict = SharedStepChangeViewModel.from_dict(shared_step_change_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


