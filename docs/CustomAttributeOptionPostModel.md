# CustomAttributeOptionPostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the attribute option | [optional] 
**is_default** | **bool** | Indicates if the attribute option is used by default | 

## Example

```python
from testit_api_client.models.custom_attribute_option_post_model import CustomAttributeOptionPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeOptionPostModel from a JSON string
custom_attribute_option_post_model_instance = CustomAttributeOptionPostModel.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeOptionPostModel.to_json())

# convert the object into a dict
custom_attribute_option_post_model_dict = custom_attribute_option_post_model_instance.to_dict()
# create an instance of CustomAttributeOptionPostModel from a dict
custom_attribute_option_post_model_from_dict = CustomAttributeOptionPostModel.from_dict(custom_attribute_option_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


