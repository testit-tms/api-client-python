# CreateWorkItemApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type_name** | [**WorkItemEntityTypes**](WorkItemEntityTypes.md) |  | 
**description** | **str** | Workitem description | [optional] 
**state** | [**WorkItemStates**](WorkItemStates.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**steps** | [**List[CreateStepApiModel]**](CreateStepApiModel.md) | Collection of workitem steps | 
**precondition_steps** | [**List[CreateStepApiModel]**](CreateStepApiModel.md) | Collection of workitem precondition steps | 
**postcondition_steps** | [**List[CreateStepApiModel]**](CreateStepApiModel.md) | Collection of workitem postcondition steps | 
**duration** | **int** | WorkItem duration in milliseconds, must be 0 for shared steps and greater than 0 for the other types of work items | 
**attributes** | **Dict[str, object]** | Key value pair of custom workitem attributes | 
**tags** | [**List[TagModel]**](TagModel.md) | Collection of workitem tags | 
**attachments** | [**List[AssignAttachmentApiModel]**](AssignAttachmentApiModel.md) | Collection of workitem attachments | [optional] 
**iterations** | [**List[AssignIterationApiModel]**](AssignIterationApiModel.md) | Collection of parameter sets | [optional] 
**links** | [**List[CreateLinkApiModel]**](CreateLinkApiModel.md) | Collection of workitem links | 
**name** | **str** | Workitem name | 
**project_id** | **str** | Project unique identifier - used to link workitem with project | 
**section_id** | **str** | Internal identifier of section where workitem is located | 
**auto_tests** | [**List[AutoTestIdModel]**](AutoTestIdModel.md) | Collection of autotest internal ids | [optional] 

## Example

```python
from testit_api_client.models.create_work_item_api_model import CreateWorkItemApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkItemApiModel from a JSON string
create_work_item_api_model_instance = CreateWorkItemApiModel.from_json(json)
# print the JSON string representation of the object
print(CreateWorkItemApiModel.to_json())

# convert the object into a dict
create_work_item_api_model_dict = create_work_item_api_model_instance.to_dict()
# create an instance of CreateWorkItemApiModel from a dict
create_work_item_api_model_from_dict = CreateWorkItemApiModel.from_dict(create_work_item_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


