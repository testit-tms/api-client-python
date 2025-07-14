# GlobalSearchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**resource_type** | **str** |  | [optional] 
**take** | **int** |  | 
**skip** | **int** |  | 

## Example

```python
from testit_api_client.models.global_search_request import GlobalSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalSearchRequest from a JSON string
global_search_request_instance = GlobalSearchRequest.from_json(json)
# print the JSON string representation of the object
print GlobalSearchRequest.to_json()

# convert the object into a dict
global_search_request_dict = global_search_request_instance.to_dict()
# create an instance of GlobalSearchRequest from a dict
global_search_request_from_dict = GlobalSearchRequest.from_dict(global_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


