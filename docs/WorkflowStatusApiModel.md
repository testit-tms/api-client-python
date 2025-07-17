# WorkflowStatusApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_id** | **str** |  | 
**priority** | **int** |  | 

## Example

```python
from testit_api_client.models.workflow_status_api_model import WorkflowStatusApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStatusApiModel from a JSON string
workflow_status_api_model_instance = WorkflowStatusApiModel.from_json(json)
# print the JSON string representation of the object
print WorkflowStatusApiModel.to_json()

# convert the object into a dict
workflow_status_api_model_dict = workflow_status_api_model_instance.to_dict()
# create an instance of WorkflowStatusApiModel from a dict
workflow_status_api_model_from_dict = WorkflowStatusApiModel.from_dict(workflow_status_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


