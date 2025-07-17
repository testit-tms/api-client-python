# WorkItemShortModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Work Item internal unique identifier | 
**version_id** | **str** | Work Item version identifier | 
**version_number** | **int** | Work Item version number | 
**name** | **str** | Work Item name | 
**entity_type_name** | **str** | Work Item type. Possible values: CheckLists, SharedSteps, TestCases | 
**project_id** | **str** | Project unique identifier | 
**section_id** | **str** | Identifier of Section where Work Item is located | 
**section_name** | **str** | Section name of Work Item | 
**is_automated** | **bool** | Boolean flag determining whether Work Item is automated | 
**global_id** | **int** | Work Item global identifier | 
**duration** | **int** | Work Item duration | 
**median_duration** | **int** | Work Item median duration | [optional] 
**attributes** | **Dict[str, object]** | Work Item attributes | [optional] 
**created_by_id** | **str** | Unique identifier of user who created Work Item | 
**modified_by_id** | **str** | Unique identifier of user who applied the latest modification of Work Item | [optional] 
**created_date** | **datetime** | Date and time of Work Item creation | [optional] 
**modified_date** | **datetime** | Date and time of the latest modification of Work Item | [optional] 
**state** | [**WorkItemStates**](WorkItemStates.md) | The current state of Work Item | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) | Work Item priority level | 
**source_type** | [**WorkItemSourceTypeModel**](WorkItemSourceTypeModel.md) | Work Item source type | 
**is_deleted** | **bool** | Flag determining whether Work Item is deleted | 
**tag_names** | **List[str]** | Array of tag names of Work Item | [optional] 
**iterations** | [**List[IterationModel]**](IterationModel.md) | Set of iterations related to Work Item | 
**links** | [**List[LinkShortModel]**](LinkShortModel.md) | Set of links related to Work Item | 

## Example

```python
from testit_api_client.models.work_item_short_model import WorkItemShortModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemShortModel from a JSON string
work_item_short_model_instance = WorkItemShortModel.from_json(json)
# print the JSON string representation of the object
print WorkItemShortModel.to_json()

# convert the object into a dict
work_item_short_model_dict = work_item_short_model_instance.to_dict()
# create an instance of WorkItemShortModel from a dict
work_item_short_model_from_dict = WorkItemShortModel.from_dict(work_item_short_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


