# WorkItemShortModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**entity_type_name** | **str** | Property can have one of these values: CheckLists, SharedSteps, TestCases | 
**project_id** | **str** | This property is used to link autotest with project | 
**section_id** | **str** | This property links workitem with section | 
**section_name** | **str** | Name of the section where work item is located | 
**state** | **bool, date, datetime, dict, float, int, list, str, none_type** | Property can have one of these values: NeedsWork, NotReady, Ready | 
**priority** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**id** | **str** |  | [optional] 
**version_id** | **str** | used for versioning changes in workitem | [optional] 
**is_automated** | **bool** |  | [optional] 
**global_id** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**created_date** | **datetime, none_type** |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**tag_names** | **[str]** |  | [optional] 
**iterations** | [**[IterationModel]**](IterationModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


