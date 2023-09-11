# WorkItemShortModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Work Item internal unique identifier | 
**version_id** | **str** | Work Item version identifier | 
**name** | **str** | Work Item name | 
**entity_type_name** | **str** | Work Item type. Possible values: CheckLists, SharedSteps, TestCases | 
**project_id** | **str** | Project unique identifier | 
**section_id** | **str** | Identifier of Section where Work Item is located | 
**section_name** | **str** | Section name of Work Item | 
**is_automated** | **bool** | Boolean flag determining whether Work Item is automated | 
**global_id** | **int** | Work Item global identifier | 
**duration** | **int** | Work Item duration | 
**created_by_id** | **str** | Unique identifier of user who created Work Item | 
**state** | [**WorkItemStates**](WorkItemStates.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**is_deleted** | **bool** | Flag determining whether Work Item is deleted | 
**median_duration** | **int, none_type** | Work Item median duration | [optional] 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Work Item attributes | [optional] 
**modified_by_id** | **str, none_type** | Unique identifier of user who applied the latest modification of Work Item | [optional] 
**created_date** | **datetime, none_type** | Date and time of Work Item creation | [optional] 
**modified_date** | **datetime, none_type** | Date and time of the latest modification of Work Item | [optional] 
**tag_names** | **[str], none_type** | Array of tag names of Work Item | [optional] 
**iterations** | [**[IterationModel], none_type**](IterationModel.md) | Set of iterations related to Work Item | [optional] 
**links** | [**[LinkShortModel], none_type**](LinkShortModel.md) | Set of links related to Work Item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


