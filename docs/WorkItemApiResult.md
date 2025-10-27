# WorkItemApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the work item | 
**global_id** | **int** | Global identifier of the work item | 
**version_id** | **str** | Version identifier of the work item | 
**version_number** | **int** | Version number of the work item | 
**project_id** | **str** | Unique identifier of the project | 
**section_id** | **str** | Unique identifier of the section within a project | 
**name** | **str** | Name of the work item | 
**source_type** | [**WorkItemSourceTypeApiModel**](WorkItemSourceTypeApiModel.md) |  | 
**entity_type_name** | [**WorkItemEntityTypeApiModel**](WorkItemEntityTypeApiModel.md) |  | 
**duration** | **int** | Duration of the work item in milliseconds | 
**median_duration** | **int** | Median duration of the work item in milliseconds | 
**state** | [**WorkItemStateApiModel**](WorkItemStateApiModel.md) |  | 
**priority** | [**WorkItemPriorityApiModel**](WorkItemPriorityApiModel.md) |  | 
**is_automated** | **bool** |  | 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Set of custom attributes associated with the work item | 
**tags** | [**[TagModel]**](TagModel.md) | Set of tags applied to the work item | 
**section_precondition_steps** | [**[StepModel]**](StepModel.md) | Set of section precondition steps that need to be executed before starting the work item steps | 
**section_postcondition_steps** | [**[StepModel]**](StepModel.md) | Set of section postcondition steps that need to be executed after completing the work item steps | 
**precondition_steps** | [**[StepModel]**](StepModel.md) | Set of precondition steps that need to be executed before starting the main steps | 
**steps** | [**[StepModel]**](StepModel.md) | Main steps or actions defined for the work item | 
**postcondition_steps** | [**[StepModel]**](StepModel.md) | Set of postcondition steps that are executed after completing the main steps | 
**iterations** | [**[IterationModel]**](IterationModel.md) | Associated iterations linked to the work item | 
**auto_tests** | [**[AutoTestModel]**](AutoTestModel.md) | Automated tests associated with the work item | 
**attachments** | [**[AttachmentModel]**](AttachmentModel.md) | Files attached to the work item | 
**links** | [**[LinkModel]**](LinkModel.md) | Set of links related to the work item | 
**external_issues** | [**[ExternalIssueApiResult]**](ExternalIssueApiResult.md) | Set of external issues related to the work item | 
**created_date** | **datetime** | Creation date of the work item | 
**created_by_id** | **str** | Unique identifier of the work item creator | 
**is_deleted** | **bool** | Indicates whether the work item is marked as deleted | 
**description** | **str, none_type** | Description of the work item | [optional] 
**modified_date** | **datetime, none_type** | Modification date of the work item | [optional] 
**modified_by_id** | **str, none_type** | Unique identifier of the work item modifier | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


