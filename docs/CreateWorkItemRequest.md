# CreateWorkItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type_name** | [**WorkItemEntityTypes**](WorkItemEntityTypes.md) |  | 
**state** | [**WorkItemStates**](WorkItemStates.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**steps** | [**[CreateStepApiModel]**](CreateStepApiModel.md) | Collection of workitem steps | 
**precondition_steps** | [**[CreateStepApiModel]**](CreateStepApiModel.md) | Collection of workitem precondition steps | 
**postcondition_steps** | [**[CreateStepApiModel]**](CreateStepApiModel.md) | Collection of workitem postcondition steps | 
**duration** | **int** | WorkItem duration in milliseconds, must be 0 for shared steps and greater than 0 for the other types of work items | 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Key value pair of custom workitem attributes | 
**tags** | [**[TagModel]**](TagModel.md) | Collection of workitem tags | 
**links** | [**[CreateLinkApiModel]**](CreateLinkApiModel.md) | Collection of workitem links | 
**name** | **str** | Workitem name | 
**project_id** | **str** | Project unique identifier - used to link workitem with project | 
**section_id** | **str** | Internal identifier of section where workitem is located | 
**description** | **str, none_type** | Workitem description | [optional] 
**attachments** | [**[AssignAttachmentApiModel], none_type**](AssignAttachmentApiModel.md) | Collection of workitem attachments | [optional] 
**iterations** | [**[AssignIterationApiModel], none_type**](AssignIterationApiModel.md) | Collection of parameter sets | [optional] 
**auto_tests** | [**[AutoTestIdModel], none_type**](AutoTestIdModel.md) | Collection of autotest internal ids | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


