# ApiV2WorkItemsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Unique identifier of the project | 
**name** | **str** | Name of the work item | 
**entity_type_name** | [**WorkItemEntityTypeApiModel**](WorkItemEntityTypeApiModel.md) |  | 
**duration** | **int** | Duration of the work item in milliseconds | 
**state** | [**WorkItemStateApiModel**](WorkItemStateApiModel.md) |  | 
**priority** | [**WorkItemPriorityApiModel**](WorkItemPriorityApiModel.md) |  | 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Set of custom attributes associated with the work item | 
**tags** | [**[TagModel]**](TagModel.md) | Set of tags applied to the work item | 
**precondition_steps** | [**[CreateStepApiModel]**](CreateStepApiModel.md) | Set of precondition steps that need to be executed before starting the main steps | 
**steps** | [**[CreateStepApiModel]**](CreateStepApiModel.md) | Main steps or actions defined for the work item | 
**postcondition_steps** | [**[CreateStepApiModel]**](CreateStepApiModel.md) | Set of postcondition steps that are executed after completing the main steps | 
**links** | [**[CreateLinkApiModel]**](CreateLinkApiModel.md) | Set of links related to the work item | 
**section_id** | **str, none_type** | Unique identifier of the section within a project | [optional] 
**description** | **str, none_type** | Description of the work item | [optional] 
**iterations** | [**[AssignIterationApiModel], none_type**](AssignIterationApiModel.md) | Associated iterations linked to the work item | [optional] 
**auto_tests** | [**[AutoTestIdModel], none_type**](AutoTestIdModel.md) | Automated tests associated with the work item | [optional] 
**attachments** | [**[AssignAttachmentApiModel], none_type**](AssignAttachmentApiModel.md) | Files attached to the work item | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


