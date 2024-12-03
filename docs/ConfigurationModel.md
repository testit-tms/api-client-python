# ConfigurationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**parameters** | **Dict[str, str]** |  | [optional] 
**project_id** | **str** | This property is used to link configuration with project | 
**is_default** | **bool** |  | 
**name** | **str** |  | [optional] 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**global_id** | **int** |  | 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 

## Example

```python
from testit_api_client.models.configuration_model import ConfigurationModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationModel from a JSON string
configuration_model_instance = ConfigurationModel.from_json(json)
# print the JSON string representation of the object
print(ConfigurationModel.to_json())

# convert the object into a dict
configuration_model_dict = configuration_model_instance.to_dict()
# create an instance of ConfigurationModel from a dict
configuration_model_from_dict = ConfigurationModel.from_dict(configuration_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


