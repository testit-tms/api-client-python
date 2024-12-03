# SharedStepResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_id** | **str** |  | 
**outcome** | **str** |  | 

## Example

```python
from testit_api_client.models.shared_step_result import SharedStepResult

# TODO update the JSON string below
json = "{}"
# create an instance of SharedStepResult from a JSON string
shared_step_result_instance = SharedStepResult.from_json(json)
# print the JSON string representation of the object
print(SharedStepResult.to_json())

# convert the object into a dict
shared_step_result_dict = shared_step_result_instance.to_dict()
# create an instance of SharedStepResult from a dict
shared_step_result_from_dict = SharedStepResult.from_dict(shared_step_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


