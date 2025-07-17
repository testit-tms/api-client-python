# SearchCustomAttributeTemplateGetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**is_deleted** | **bool** |  | 
**name** | **str** |  | 
**project_shortest_models** | [**List[ProjectShortestModel]**](ProjectShortestModel.md) |  | 
**custom_attribute_models** | [**List[CustomAttributeModel]**](CustomAttributeModel.md) |  | 

## Example

```python
from testit_api_client.models.search_custom_attribute_template_get_model import SearchCustomAttributeTemplateGetModel

# TODO update the JSON string below
json = "{}"
# create an instance of SearchCustomAttributeTemplateGetModel from a JSON string
search_custom_attribute_template_get_model_instance = SearchCustomAttributeTemplateGetModel.from_json(json)
# print the JSON string representation of the object
print SearchCustomAttributeTemplateGetModel.to_json()

# convert the object into a dict
search_custom_attribute_template_get_model_dict = search_custom_attribute_template_get_model_instance.to_dict()
# create an instance of SearchCustomAttributeTemplateGetModel from a dict
search_custom_attribute_template_get_model_from_dict = SearchCustomAttributeTemplateGetModel.from_dict(search_custom_attribute_template_get_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


