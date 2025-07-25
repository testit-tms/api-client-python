# UpdateWorkItemApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Workitem internal identifier | 
**section_id** | **str** | Internal identifier of section where workitem is located | 
**state** | [**WorkItemStates**](WorkItemStates.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**steps** | [**[UpdateStepApiModel]**](UpdateStepApiModel.md) | Collection of workitem steps | 
**precondition_steps** | [**[UpdateStepApiModel]**](UpdateStepApiModel.md) | Collection of workitem precondtion steps | 
**postcondition_steps** | [**[UpdateStepApiModel]**](UpdateStepApiModel.md) | Collection of workitem postcondition steps | 
**duration** | **int** | Workitem duration in milliseconds | 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Key value pair of custom workitem attributes | 
**tags** | [**[TagModel]**](TagModel.md) | Collection of workitem tags | 
**links** | [**[UpdateLinkApiModel]**](UpdateLinkApiModel.md) | Collection of workitem links | 
**name** | **str** | Workitem name | 
**attachments** | [**[AssignAttachmentApiModel]**](AssignAttachmentApiModel.md) |  | 
**description** | **str, none_type** | Workitem description | [optional] 
**source_type** | [**WorkItemSourceTypeModel**](WorkItemSourceTypeModel.md) |  | [optional] 
**iterations** | [**[AssignIterationApiModel], none_type**](AssignIterationApiModel.md) | Collection of parameter id sets | [optional] 
**auto_tests** | [**[AutoTestIdModel], none_type**](AutoTestIdModel.md) | Collection of autotest internal ids | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


