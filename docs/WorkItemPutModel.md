# WorkItemPutModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**[AttachmentPutModel]**](AttachmentPutModel.md) |  | 
**state** | [**WorkItemStates**](WorkItemStates.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**steps** | [**[StepPutModel]**](StepPutModel.md) |  | 
**precondition_steps** | [**[StepPutModel]**](StepPutModel.md) |  | 
**postcondition_steps** | [**[StepPutModel]**](StepPutModel.md) |  | 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**tags** | [**[TagShortModel]**](TagShortModel.md) |  | 
**links** | [**[LinkPutModel]**](LinkPutModel.md) |  | 
**name** | **str** |  | 
**iterations** | [**[IterationPutModel], none_type**](IterationPutModel.md) |  | [optional] 
**auto_tests** | [**[AutoTestIdModel], none_type**](AutoTestIdModel.md) |  | [optional] 
**id** | **str** |  | [optional] 
**section_id** | **str** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**duration** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


