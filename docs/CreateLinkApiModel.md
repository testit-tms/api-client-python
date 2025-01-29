# CreateLinkApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Link name. | [optional] 
**url** | **str** | Address can be specified without protocol, but necessarily with the domain. | 
**description** | **str** | Link description. | [optional] 
**type** | [**LinkType**](LinkType.md) | Specifies the type of the link. | [optional] 
**has_info** | **bool** | Flag defines if link relates to integrated jira service | 

## Example

```python
from testit_api_client.models.create_link_api_model import CreateLinkApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLinkApiModel from a JSON string
create_link_api_model_instance = CreateLinkApiModel.from_json(json)
# print the JSON string representation of the object
print(CreateLinkApiModel.to_json())

# convert the object into a dict
create_link_api_model_dict = create_link_api_model_instance.to_dict()
# create an instance of CreateLinkApiModel from a dict
create_link_api_model_from_dict = CreateLinkApiModel.from_dict(create_link_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


