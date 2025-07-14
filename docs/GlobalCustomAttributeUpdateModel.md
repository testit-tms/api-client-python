# GlobalCustomAttributeUpdateModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of attribute | 
**options** | [**List[CustomAttributeOptionModel]**](CustomAttributeOptionModel.md) | Collection of attribute options     Available for attributes of type &#x60;options&#x60; and &#x60;multiple options&#x60; only | [optional] 
**is_enabled** | **bool** | Indicates whether the attribute is available | [optional] 
**is_required** | **bool** | Indicates whether the attribute value is mandatory to specify | [optional] 

## Example

```python
from testit_api_client.models.global_custom_attribute_update_model import GlobalCustomAttributeUpdateModel

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalCustomAttributeUpdateModel from a JSON string
global_custom_attribute_update_model_instance = GlobalCustomAttributeUpdateModel.from_json(json)
# print the JSON string representation of the object
print GlobalCustomAttributeUpdateModel.to_json()

# convert the object into a dict
global_custom_attribute_update_model_dict = global_custom_attribute_update_model_instance.to_dict()
# create an instance of GlobalCustomAttributeUpdateModel from a dict
global_custom_attribute_update_model_from_dict = GlobalCustomAttributeUpdateModel.from_dict(global_custom_attribute_update_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


