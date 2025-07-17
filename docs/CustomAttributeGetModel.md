# CustomAttributeGetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the attribute | 
**options** | [**List[CustomAttributeOptionModel]**](CustomAttributeOptionModel.md) | Collection of the attribute options | 
**type** | [**CustomAttributeTypesEnum**](CustomAttributeTypesEnum.md) | Type of the attribute | 
**is_deleted** | **bool** | Indicates if the attribute is deleted | 
**name** | **str** | Name of the attribute | 
**is_enabled** | **bool** | Indicates if the attribute is enabled | 
**is_required** | **bool** | Indicates if the attribute is mandatory to specify | 
**is_global** | **bool** | Indicates if the attribute is available across all projects | 

## Example

```python
from testit_api_client.models.custom_attribute_get_model import CustomAttributeGetModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeGetModel from a JSON string
custom_attribute_get_model_instance = CustomAttributeGetModel.from_json(json)
# print the JSON string representation of the object
print CustomAttributeGetModel.to_json()

# convert the object into a dict
custom_attribute_get_model_dict = custom_attribute_get_model_instance.to_dict()
# create an instance of CustomAttributeGetModel from a dict
custom_attribute_get_model_from_dict = CustomAttributeGetModel.from_dict(custom_attribute_get_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


