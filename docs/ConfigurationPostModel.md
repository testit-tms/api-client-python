# ConfigurationPostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**parameters** | **Dict[str, str]** |  | 
**project_id** | **str** | This property is used to link configuration with project | 
**is_default** | **bool** |  | 
**name** | **str** |  | 

## Example

```python
from testit_api_client.models.configuration_post_model import ConfigurationPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationPostModel from a JSON string
configuration_post_model_instance = ConfigurationPostModel.from_json(json)
# print the JSON string representation of the object
print(ConfigurationPostModel.to_json())

# convert the object into a dict
configuration_post_model_dict = configuration_post_model_instance.to_dict()
# create an instance of ConfigurationPostModel from a dict
configuration_post_model_from_dict = ConfigurationPostModel.from_dict(configuration_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


