# CustomAttributeSearchResponseModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_item_usage** | [**List[ProjectShortestModel]**](ProjectShortestModel.md) |  | 
**test_plan_usage** | [**List[ProjectShortestModel]**](ProjectShortestModel.md) |  | 
**id** | **str** | Unique ID of the attribute | 
**options** | [**List[CustomAttributeOptionModel]**](CustomAttributeOptionModel.md) | Collection of the attribute options   Available for attributes of type &#x60;options&#x60; and &#x60;multiple options&#x60; only | 
**type** | [**CustomAttributeTypesEnum**](CustomAttributeTypesEnum.md) | Type of the attribute | 
**is_deleted** | **bool** | Indicates if the attribute is deleted | 
**name** | **str** | Name of the attribute | 
**is_enabled** | **bool** | Indicates if the attribute is enabled | 
**is_required** | **bool** | Indicates if the attribute value is mandatory to specify | 
**is_global** | **bool** | Indicates if the attribute is available across all projects | 

## Example

```python
from testit_api_client.models.custom_attribute_search_response_model import CustomAttributeSearchResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeSearchResponseModel from a JSON string
custom_attribute_search_response_model_instance = CustomAttributeSearchResponseModel.from_json(json)
# print the JSON string representation of the object
print CustomAttributeSearchResponseModel.to_json()

# convert the object into a dict
custom_attribute_search_response_model_dict = custom_attribute_search_response_model_instance.to_dict()
# create an instance of CustomAttributeSearchResponseModel from a dict
custom_attribute_search_response_model_from_dict = CustomAttributeSearchResponseModel.from_dict(custom_attribute_search_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


