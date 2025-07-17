# UpdateLinkApiModel


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
from testit_api_client.models.update_link_api_model import UpdateLinkApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLinkApiModel from a JSON string
update_link_api_model_instance = UpdateLinkApiModel.from_json(json)
# print the JSON string representation of the object
print UpdateLinkApiModel.to_json()

# convert the object into a dict
update_link_api_model_dict = update_link_api_model_instance.to_dict()
# create an instance of UpdateLinkApiModel from a dict
update_link_api_model_from_dict = UpdateLinkApiModel.from_dict(update_link_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


