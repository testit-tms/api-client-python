# CustomAttributeTemplateModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**is_deleted** | **bool** |  | 
**name** | **str** | Custom attributes template name | 

## Example

```python
from testit_api_client.models.custom_attribute_template_model import CustomAttributeTemplateModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeTemplateModel from a JSON string
custom_attribute_template_model_instance = CustomAttributeTemplateModel.from_json(json)
# print the JSON string representation of the object
print CustomAttributeTemplateModel.to_json()

# convert the object into a dict
custom_attribute_template_model_dict = custom_attribute_template_model_instance.to_dict()
# create an instance of CustomAttributeTemplateModel from a dict
custom_attribute_template_model_from_dict = CustomAttributeTemplateModel.from_dict(custom_attribute_template_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


