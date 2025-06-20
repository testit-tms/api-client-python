# CustomAttributeTemplatePutModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the attribute template | 
**custom_attribute_ids** | **List[str]** | Collection of attribute IDs | [optional] 
**name** | **str** | Custom attributes template name | 

## Example

```python
from testit_api_client.models.custom_attribute_template_put_model import CustomAttributeTemplatePutModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeTemplatePutModel from a JSON string
custom_attribute_template_put_model_instance = CustomAttributeTemplatePutModel.from_json(json)
# print the JSON string representation of the object
print CustomAttributeTemplatePutModel.to_json()

# convert the object into a dict
custom_attribute_template_put_model_dict = custom_attribute_template_put_model_instance.to_dict()
# create an instance of CustomAttributeTemplatePutModel from a dict
custom_attribute_template_put_model_from_dict = CustomAttributeTemplatePutModel.from_dict(custom_attribute_template_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


