# CustomAttributeTemplatePostModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_attribute_ids** | **List[str]** | Collection of attribute IDs | [optional] 
**name** | **str** | Custom attributes template name | 

## Example

```python
from testit_api_client.models.custom_attribute_template_post_model import CustomAttributeTemplatePostModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeTemplatePostModel from a JSON string
custom_attribute_template_post_model_instance = CustomAttributeTemplatePostModel.from_json(json)
# print the JSON string representation of the object
print CustomAttributeTemplatePostModel.to_json()

# convert the object into a dict
custom_attribute_template_post_model_dict = custom_attribute_template_post_model_instance.to_dict()
# create an instance of CustomAttributeTemplatePostModel from a dict
custom_attribute_template_post_model_from_dict = CustomAttributeTemplatePostModel.from_dict(custom_attribute_template_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


