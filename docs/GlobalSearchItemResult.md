# GlobalSearchItemResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | 
**resource_id** | **str** |  | 
**global_id** | **int** |  | [optional] 
**name** | **str** |  | 
**project_global_id** | **int** |  | 

## Example

```python
from testit_api_client.models.global_search_item_result import GlobalSearchItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalSearchItemResult from a JSON string
global_search_item_result_instance = GlobalSearchItemResult.from_json(json)
# print the JSON string representation of the object
print(GlobalSearchItemResult.to_json())

# convert the object into a dict
global_search_item_result_dict = global_search_item_result_instance.to_dict()
# create an instance of GlobalSearchItemResult from a dict
global_search_item_result_from_dict = GlobalSearchItemResult.from_dict(global_search_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


