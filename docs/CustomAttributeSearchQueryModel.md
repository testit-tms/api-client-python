# CustomAttributeSearchQueryModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of attribute | [optional] 
**project_ids** | **List[str]** | Unique IDs of projects where attribute is in use | [optional] 
**custom_attribute_ids** | **List[str]** | Unique IDs of attributes for search restriction | [optional] 
**custom_attribute_types** | [**List[CustomAttributeTypesEnum]**](CustomAttributeTypesEnum.md) | Collection of attribute types | [optional] 
**is_global** | **bool** | Indicates whether the attribute is available across all projects | [optional] 
**is_deleted** | **bool** | Indicates whether the attribute is deleted | [optional] 

## Example

```python
from testit_api_client.models.custom_attribute_search_query_model import CustomAttributeSearchQueryModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeSearchQueryModel from a JSON string
custom_attribute_search_query_model_instance = CustomAttributeSearchQueryModel.from_json(json)
# print the JSON string representation of the object
print CustomAttributeSearchQueryModel.to_json()

# convert the object into a dict
custom_attribute_search_query_model_dict = custom_attribute_search_query_model_instance.to_dict()
# create an instance of CustomAttributeSearchQueryModel from a dict
custom_attribute_search_query_model_from_dict = CustomAttributeSearchQueryModel.from_dict(custom_attribute_search_query_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


