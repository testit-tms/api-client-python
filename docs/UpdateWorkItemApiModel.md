# UpdateWorkItemApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the work item | 
**section_id** | **str** | Unique identifier of the section within a project | 
**name** | **str** | Name of the work item | 
**duration** | **int** | Duration of the work item in milliseconds | 
**state** | [**WorkItemStateApiModel**](WorkItemStateApiModel.md) |  | 
**priority** | [**WorkItemPriorityApiModel**](WorkItemPriorityApiModel.md) |  | 
**description** | **str, none_type** | Description of the work item | [optional] 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Set of custom attributes associated with the work item | [optional] 
**tags** | [**[TagModel], none_type**](TagModel.md) | Set of tags applied to the work item | [optional] 
**precondition_steps** | [**[UpdateStepApiModel], none_type**](UpdateStepApiModel.md) | Set of precondition steps that must be executed before the main steps | [optional] 
**steps** | [**[UpdateStepApiModel], none_type**](UpdateStepApiModel.md) | Set of main steps or actions defined for the work item | [optional] 
**postcondition_steps** | [**[UpdateStepApiModel], none_type**](UpdateStepApiModel.md) | Set of postcondition steps that are executed after completing the main steps | [optional] 
**iterations** | [**[AssignIterationApiModel], none_type**](AssignIterationApiModel.md) | Set of iterations associated with the work item | [optional] 
**auto_tests** | [**[AutoTestIdModel], none_type**](AutoTestIdModel.md) | Set of automated tests linked to the work item | [optional] 
**attachments** | [**[AssignAttachmentApiModel], none_type**](AssignAttachmentApiModel.md) | Set of files attached to the work item | [optional] 
**links** | [**[UpdateLinkApiModel], none_type**](UpdateLinkApiModel.md) | Set of links related to the work item | [optional] 
**parameters** | [**[WorkItemParameterKeyApiModel], none_type**](WorkItemParameterKeyApiModel.md) | Set of parameter keys associated with the work item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


