# CustomAttributeOptionModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the attribute option | 
**is_deleted** | **bool** | Indicates if the attributes option is deleted | 
**value** | **str** | Value of the attribute option | [optional] 
**is_default** | **bool** | Indicates if the attribute option is used by default | 

## Example

```python
from testit_api_client.models.custom_attribute_option_model import CustomAttributeOptionModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeOptionModel from a JSON string
custom_attribute_option_model_instance = CustomAttributeOptionModel.from_json(json)
# print the JSON string representation of the object
print CustomAttributeOptionModel.to_json()

# convert the object into a dict
custom_attribute_option_model_dict = custom_attribute_option_model_instance.to_dict()
# create an instance of CustomAttributeOptionModel from a dict
custom_attribute_option_model_from_dict = CustomAttributeOptionModel.from_dict(custom_attribute_option_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


