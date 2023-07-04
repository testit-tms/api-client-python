# UpdateWorkItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**[AttachmentPutModel]**](AttachmentPutModel.md) |  | 
**id** | **str** |  | 
**state** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**priority** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**steps** | [**[StepPutModel]**](StepPutModel.md) |  | 
**precondition_steps** | [**[StepPutModel]**](StepPutModel.md) |  | 
**postcondition_steps** | [**[StepPutModel]**](StepPutModel.md) |  | 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**tags** | [**[TagShortModel]**](TagShortModel.md) |  | 
**links** | [**[LinkPutModel]**](LinkPutModel.md) |  | 
**name** | **str** |  | 
**iterations** | [**[IterationPutModel], none_type**](IterationPutModel.md) |  | [optional] 
**auto_tests** | [**[AutoTestIdModel], none_type**](AutoTestIdModel.md) |  | [optional] 
**section_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


