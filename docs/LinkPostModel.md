# LinkPostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Link name. | [optional] 
**url** | **str** | Address can be specified without protocol, but necessarily with the domain. | 
**description** | **str** | Link description. | [optional] 
**type** | [**LinkType**](LinkType.md) | Specifies the type of the link. | [optional] 
**has_info** | **bool** |  | 

## Example

```python
from testit_api_client.models.link_post_model import LinkPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of LinkPostModel from a JSON string
link_post_model_instance = LinkPostModel.from_json(json)
# print the JSON string representation of the object
print(LinkPostModel.to_json())

# convert the object into a dict
link_post_model_dict = link_post_model_instance.to_dict()
# create an instance of LinkPostModel from a dict
link_post_model_from_dict = LinkPostModel.from_dict(link_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


