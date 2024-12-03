# GlobalCustomAttributePostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of attribute | 
**is_enabled** | **bool** | Indicates whether the attribute is available | [optional] 
**is_required** | **bool** | Indicates whether the attribute value is mandatory to specify | [optional] 
**options** | [**List[CustomAttributeOptionPostModel]**](CustomAttributeOptionPostModel.md) | Collection of attribute options     Available for attributes of type &#x60;options&#x60; and &#x60;multiple options&#x60; only | [optional] 
**type** | [**CustomAttributeTypesEnum**](CustomAttributeTypesEnum.md) | Type of attribute | 

## Example

```python
from testit_api_client.models.global_custom_attribute_post_model import GlobalCustomAttributePostModel

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalCustomAttributePostModel from a JSON string
global_custom_attribute_post_model_instance = GlobalCustomAttributePostModel.from_json(json)
# print the JSON string representation of the object
print(GlobalCustomAttributePostModel.to_json())

# convert the object into a dict
global_custom_attribute_post_model_dict = global_custom_attribute_post_model_instance.to_dict()
# create an instance of GlobalCustomAttributePostModel from a dict
global_custom_attribute_post_model_from_dict = GlobalCustomAttributePostModel.from_dict(global_custom_attribute_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


