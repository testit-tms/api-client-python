# ProjectAttributesFilterModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies an attribute name to search for | 
**is_required** | **bool** | Specifies an attribute mandatory status to search for | [optional] 
**is_global** | **bool** | Specifies an attribute global status to search for | [optional] 
**types** | [**List[CustomAttributeTypesEnum]**](CustomAttributeTypesEnum.md) | Specifies an attribute types to search for | 
**is_enabled** | **bool** | Specifies an attribute enabled status to search for | [optional] 

## Example

```python
from testit_api_client.models.project_attributes_filter_model import ProjectAttributesFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectAttributesFilterModel from a JSON string
project_attributes_filter_model_instance = ProjectAttributesFilterModel.from_json(json)
# print the JSON string representation of the object
print ProjectAttributesFilterModel.to_json()

# convert the object into a dict
project_attributes_filter_model_dict = project_attributes_filter_model_instance.to_dict()
# create an instance of ProjectAttributesFilterModel from a dict
project_attributes_filter_model_from_dict = ProjectAttributesFilterModel.from_dict(project_attributes_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


