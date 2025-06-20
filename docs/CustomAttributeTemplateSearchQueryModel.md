# CustomAttributeTemplateSearchQueryModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**project_ids** | **List[str]** |  | [optional] 
**custom_attribute_types** | [**List[CustomAttributeTypesEnum]**](CustomAttributeTypesEnum.md) |  | [optional] 
**is_deleted** | **bool** |  | [optional] 

## Example

```python
from testit_api_client.models.custom_attribute_template_search_query_model import CustomAttributeTemplateSearchQueryModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeTemplateSearchQueryModel from a JSON string
custom_attribute_template_search_query_model_instance = CustomAttributeTemplateSearchQueryModel.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeTemplateSearchQueryModel.to_json())

# convert the object into a dict
custom_attribute_template_search_query_model_dict = custom_attribute_template_search_query_model_instance.to_dict()
# create an instance of CustomAttributeTemplateSearchQueryModel from a dict
custom_attribute_template_search_query_model_from_dict = CustomAttributeTemplateSearchQueryModel.from_dict(custom_attribute_template_search_query_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


