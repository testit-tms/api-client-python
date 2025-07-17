# UpdateWorkflowApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**is_default** | **bool** |  | 
**statuses** | [**List[WorkflowStatusApiModel]**](WorkflowStatusApiModel.md) |  | 

## Example

```python
from testit_api_client.models.update_workflow_api_model import UpdateWorkflowApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkflowApiModel from a JSON string
update_workflow_api_model_instance = UpdateWorkflowApiModel.from_json(json)
# print the JSON string representation of the object
print UpdateWorkflowApiModel.to_json()

# convert the object into a dict
update_workflow_api_model_dict = update_workflow_api_model_instance.to_dict()
# create an instance of UpdateWorkflowApiModel from a dict
update_workflow_api_model_from_dict = UpdateWorkflowApiModel.from_dict(update_workflow_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


