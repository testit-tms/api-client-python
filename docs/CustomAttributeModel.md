# CustomAttributeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the attribute | 
**options** | [**List[CustomAttributeOptionModel]**](CustomAttributeOptionModel.md) | Collection of the attribute options     Available for attributes of type &#x60;options&#x60; and &#x60;multiple options&#x60; only | 
**type** | [**CustomAttributeTypesEnum**](CustomAttributeTypesEnum.md) | Type of the attribute | 
**is_deleted** | **bool** | Indicates if the attribute is deleted | 
**name** | **str** | Name of the attribute | 
**is_enabled** | **bool** | Indicates if the attribute is enabled | 
**is_required** | **bool** | Indicates if the attribute value is mandatory to specify | 
**is_global** | **bool** | Indicates if the attribute is available across all projects | 

## Example

```python
from testit_api_client.models.custom_attribute_model import CustomAttributeModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeModel from a JSON string
custom_attribute_model_instance = CustomAttributeModel.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeModel.to_json())

# convert the object into a dict
custom_attribute_model_dict = custom_attribute_model_instance.to_dict()
# create an instance of CustomAttributeModel from a dict
custom_attribute_model_from_dict = CustomAttributeModel.from_dict(custom_attribute_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


