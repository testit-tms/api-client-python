# LinkApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Link unique identifier | [optional] 
**title** | **str** | Link name. | [optional] 
**url** | **str** | Address can be specified without protocol, but necessarily with the domain. | 
**description** | **str** | Link description. | [optional] 
**type** | [**LinkType**](LinkType.md) | Specifies the type of the link. | [optional] 
**has_info** | **bool** | Flag defines if link relates to integrated jira service | 

## Example

```python
from testit_api_client.models.link_api_result import LinkApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of LinkApiResult from a JSON string
link_api_result_instance = LinkApiResult.from_json(json)
# print the JSON string representation of the object
print(LinkApiResult.to_json())

# convert the object into a dict
link_api_result_dict = link_api_result_instance.to_dict()
# create an instance of LinkApiResult from a dict
link_api_result_from_dict = LinkApiResult.from_dict(link_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


