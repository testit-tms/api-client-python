# WorkflowShortApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**is_system** | **bool** |  | 
**is_default** | **bool** |  | 

## Example

```python
from testit_api_client.models.workflow_short_api_result import WorkflowShortApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowShortApiResult from a JSON string
workflow_short_api_result_instance = WorkflowShortApiResult.from_json(json)
# print the JSON string representation of the object
print WorkflowShortApiResult.to_json()

# convert the object into a dict
workflow_short_api_result_dict = workflow_short_api_result_instance.to_dict()
# create an instance of WorkflowShortApiResult from a dict
workflow_short_api_result_from_dict = WorkflowShortApiResult.from_dict(workflow_short_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


