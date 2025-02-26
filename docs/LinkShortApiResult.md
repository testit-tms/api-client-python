# LinkShortApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**url** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from testit_api_client.models.link_short_api_result import LinkShortApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of LinkShortApiResult from a JSON string
link_short_api_result_instance = LinkShortApiResult.from_json(json)
# print the JSON string representation of the object
print(LinkShortApiResult.to_json())

# convert the object into a dict
link_short_api_result_dict = link_short_api_result_instance.to_dict()
# create an instance of LinkShortApiResult from a dict
link_short_api_result_from_dict = LinkShortApiResult.from_dict(link_short_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


