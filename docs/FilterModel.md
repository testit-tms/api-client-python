# FilterModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**data** | [**WorkItemSearchQueryModel**](WorkItemSearchQueryModel.md) |  | [optional] 
**project_id** | **str** |  | 
**fields_to_show** | **object** |  | [optional] 
**name** | **str** |  | 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 

## Example

```python
from testit_api_client.models.filter_model import FilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of FilterModel from a JSON string
filter_model_instance = FilterModel.from_json(json)
# print the JSON string representation of the object
print(FilterModel.to_json())

# convert the object into a dict
filter_model_dict = filter_model_instance.to_dict()
# create an instance of FilterModel from a dict
filter_model_from_dict = FilterModel.from_dict(filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


