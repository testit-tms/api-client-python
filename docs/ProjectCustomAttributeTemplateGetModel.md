# ProjectCustomAttributeTemplateGetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the custom attributes template | 
**is_deleted** | **bool** | Indicates if the custom attribute template is deleted | 
**name** | **str** | Name of the custom attribute template | 
**custom_attribute_models** | [**List[CustomAttributeModel]**](CustomAttributeModel.md) | Attributes of the template | 

## Example

```python
from testit_api_client.models.project_custom_attribute_template_get_model import ProjectCustomAttributeTemplateGetModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCustomAttributeTemplateGetModel from a JSON string
project_custom_attribute_template_get_model_instance = ProjectCustomAttributeTemplateGetModel.from_json(json)
# print the JSON string representation of the object
print ProjectCustomAttributeTemplateGetModel.to_json()

# convert the object into a dict
project_custom_attribute_template_get_model_dict = project_custom_attribute_template_get_model_instance.to_dict()
# create an instance of ProjectCustomAttributeTemplateGetModel from a dict
project_custom_attribute_template_get_model_from_dict = ProjectCustomAttributeTemplateGetModel.from_dict(project_custom_attribute_template_get_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


