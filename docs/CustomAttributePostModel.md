# CustomAttributePostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**List[CustomAttributeOptionPostModel]**](CustomAttributeOptionPostModel.md) | Collection of attribute options     Available for attributes of type &#x60;options&#x60; and &#x60;multiple options&#x60; only | [optional] 
**type** | [**CustomAttributeTypesEnum**](CustomAttributeTypesEnum.md) | Type of attribute | 
**name** | **str** | Name of the attribute | 
**is_enabled** | **bool** | Indicates if the attribute is enabled | 
**is_required** | **bool** | Indicates if the attribute value is mandatory to specify | 
**is_global** | **bool** | Indicates if the attribute is available across all projects | 

## Example

```python
from testit_api_client.models.custom_attribute_post_model import CustomAttributePostModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributePostModel from a JSON string
custom_attribute_post_model_instance = CustomAttributePostModel.from_json(json)
# print the JSON string representation of the object
print(CustomAttributePostModel.to_json())

# convert the object into a dict
custom_attribute_post_model_dict = custom_attribute_post_model_instance.to_dict()
# create an instance of CustomAttributePostModel from a dict
custom_attribute_post_model_from_dict = CustomAttributePostModel.from_dict(custom_attribute_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


