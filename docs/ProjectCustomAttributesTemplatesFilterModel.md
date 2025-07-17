# ProjectCustomAttributesTemplatesFilterModel

Collection of filters to apply to search

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of custom attribute template | [optional] 
**custom_attribute_types** | [**List[CustomAttributeTypesEnum]**](CustomAttributeTypesEnum.md) | Collection of custom attributes types | [optional] 

## Example

```python
from testit_api_client.models.project_custom_attributes_templates_filter_model import ProjectCustomAttributesTemplatesFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCustomAttributesTemplatesFilterModel from a JSON string
project_custom_attributes_templates_filter_model_instance = ProjectCustomAttributesTemplatesFilterModel.from_json(json)
# print the JSON string representation of the object
print ProjectCustomAttributesTemplatesFilterModel.to_json()

# convert the object into a dict
project_custom_attributes_templates_filter_model_dict = project_custom_attributes_templates_filter_model_instance.to_dict()
# create an instance of ProjectCustomAttributesTemplatesFilterModel from a dict
project_custom_attributes_templates_filter_model_from_dict = ProjectCustomAttributesTemplatesFilterModel.from_dict(project_custom_attributes_templates_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


