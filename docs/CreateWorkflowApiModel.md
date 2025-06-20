# CreateWorkflowApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**is_default** | **bool** |  | [optional] 
**statuses** | [**List[WorkflowStatusApiModel]**](WorkflowStatusApiModel.md) |  | 

## Example

```python
from testit_api_client.models.create_workflow_api_model import CreateWorkflowApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkflowApiModel from a JSON string
create_workflow_api_model_instance = CreateWorkflowApiModel.from_json(json)
# print the JSON string representation of the object
print(CreateWorkflowApiModel.to_json())

# convert the object into a dict
create_workflow_api_model_dict = create_workflow_api_model_instance.to_dict()
# create an instance of CreateWorkflowApiModel from a dict
create_workflow_api_model_from_dict = CreateWorkflowApiModel.from_dict(create_workflow_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


