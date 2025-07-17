# GlobalSearchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GlobalSearchItemResult]**](GlobalSearchItemResult.md) |  | 
**more_results_available** | **bool** |  | 
**available_resource_types** | **List[str]** |  | 

## Example

```python
from testit_api_client.models.global_search_response import GlobalSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalSearchResponse from a JSON string
global_search_response_instance = GlobalSearchResponse.from_json(json)
# print the JSON string representation of the object
print GlobalSearchResponse.to_json()

# convert the object into a dict
global_search_response_dict = global_search_response_instance.to_dict()
# create an instance of GlobalSearchResponse from a dict
global_search_response_from_dict = GlobalSearchResponse.from_dict(global_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


