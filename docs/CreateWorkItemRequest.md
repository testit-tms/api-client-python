# CreateWorkItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type_name** | [**WorkItemEntityTypes**](WorkItemEntityTypes.md) |  | 
**state** | [**WorkItemStates**](WorkItemStates.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**steps** | [**[StepPostModel]**](StepPostModel.md) |  | 
**precondition_steps** | [**[StepPostModel]**](StepPostModel.md) |  | 
**postcondition_steps** | [**[StepPostModel]**](StepPostModel.md) |  | 
**duration** | **int** | Must be 0 for shared steps and greater than 0 for the other types of work items | 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**tags** | [**[TagPostModel]**](TagPostModel.md) |  | 
**links** | [**[LinkPostModel]**](LinkPostModel.md) |  | 
**name** | **str** |  | 
**project_id** | **str** | This property is used to link workitem with project | 
**section_id** | **str** |  | 
**description** | **str, none_type** |  | [optional] 
**attachments** | [**[AttachmentPutModel], none_type**](AttachmentPutModel.md) |  | [optional] 
**iterations** | [**[IterationPutModel], none_type**](IterationPutModel.md) |  | [optional] 
**auto_tests** | [**[AutoTestIdModel], none_type**](AutoTestIdModel.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


