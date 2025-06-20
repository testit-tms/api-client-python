# WorkflowStatusApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**code** | **str** |  | 
**type** | [**TestStatusApiType**](TestStatusApiType.md) | Collection of possible status types | 
**description** | **str** |  | [optional] 
**is_system** | **bool** |  | 
**priority** | **int** |  | 

## Example

```python
from testit_api_client.models.workflow_status_api_result import WorkflowStatusApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStatusApiResult from a JSON string
workflow_status_api_result_instance = WorkflowStatusApiResult.from_json(json)
# print the JSON string representation of the object
print(WorkflowStatusApiResult.to_json())

# convert the object into a dict
workflow_status_api_result_dict = workflow_status_api_result_instance.to_dict()
# create an instance of WorkflowStatusApiResult from a dict
workflow_status_api_result_from_dict = WorkflowStatusApiResult.from_dict(workflow_status_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


