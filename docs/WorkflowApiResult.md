# WorkflowApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**is_system** | **bool** |  | 
**is_default** | **bool** |  | 
**statuses** | [**List[WorkflowStatusApiResult]**](WorkflowStatusApiResult.md) |  | 

## Example

```python
from testit_api_client.models.workflow_api_result import WorkflowApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowApiResult from a JSON string
workflow_api_result_instance = WorkflowApiResult.from_json(json)
# print the JSON string representation of the object
print(WorkflowApiResult.to_json())

# convert the object into a dict
workflow_api_result_dict = workflow_api_result_instance.to_dict()
# create an instance of WorkflowApiResult from a dict
workflow_api_result_from_dict = WorkflowApiResult.from_dict(workflow_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


