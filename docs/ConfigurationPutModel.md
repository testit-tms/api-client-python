# ConfigurationPutModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**description** | **str** |  | [optional] 
**parameters** | **Dict[str, str]** |  | 
**project_id** | **str** | This property is used to link configuration with project | 
**is_default** | **bool** |  | 
**name** | **str** |  | 

## Example

```python
from testit_api_client.models.configuration_put_model import ConfigurationPutModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationPutModel from a JSON string
configuration_put_model_instance = ConfigurationPutModel.from_json(json)
# print the JSON string representation of the object
print(ConfigurationPutModel.to_json())

# convert the object into a dict
configuration_put_model_dict = configuration_put_model_instance.to_dict()
# create an instance of ConfigurationPutModel from a dict
configuration_put_model_from_dict = ConfigurationPutModel.from_dict(configuration_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


