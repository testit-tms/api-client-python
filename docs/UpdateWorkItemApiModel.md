# UpdateWorkItemApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Workitem internal identifier | 
**section_id** | **str** | Internal identifier of section where workitem is located | 
**description** | **str** | Workitem description | [optional] 
**state** | [**WorkItemStates**](WorkItemStates.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**source_type** | [**WorkItemSourceTypeModel**](WorkItemSourceTypeModel.md) |  | [optional] 
**steps** | [**List[UpdateStepApiModel]**](UpdateStepApiModel.md) | Collection of workitem steps | 
**precondition_steps** | [**List[UpdateStepApiModel]**](UpdateStepApiModel.md) | Collection of workitem precondtion steps | 
**postcondition_steps** | [**List[UpdateStepApiModel]**](UpdateStepApiModel.md) | Collection of workitem postcondition steps | 
**duration** | **int** | Workitem duration in milliseconds | 
**attributes** | **Dict[str, object]** | Key value pair of custom workitem attributes | 
**tags** | [**List[TagModel]**](TagModel.md) | Collection of workitem tags | 
**links** | [**List[UpdateLinkApiModel]**](UpdateLinkApiModel.md) | Collection of workitem links | 
**name** | **str** | Workitem name | 
**attachments** | [**List[AssignAttachmentApiModel]**](AssignAttachmentApiModel.md) |  | 
**iterations** | [**List[AssignIterationApiModel]**](AssignIterationApiModel.md) | Collection of parameter id sets | [optional] 
**auto_tests** | [**List[AutoTestIdModel]**](AutoTestIdModel.md) | Collection of autotest internal ids | [optional] 

## Example

```python
from testit_api_client.models.update_work_item_api_model import UpdateWorkItemApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkItemApiModel from a JSON string
update_work_item_api_model_instance = UpdateWorkItemApiModel.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkItemApiModel.to_json())

# convert the object into a dict
update_work_item_api_model_dict = update_work_item_api_model_instance.to_dict()
# create an instance of UpdateWorkItemApiModel from a dict
update_work_item_api_model_from_dict = UpdateWorkItemApiModel.from_dict(update_work_item_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


