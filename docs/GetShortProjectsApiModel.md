# GetShortProjectsApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inquiry** | [**Inquiry**](Inquiry.md) |  | [optional] 
**permission_name** | **str** |  | [optional] 
**permission_type** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.get_short_projects_api_model import GetShortProjectsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetShortProjectsApiModel from a JSON string
get_short_projects_api_model_instance = GetShortProjectsApiModel.from_json(json)
# print the JSON string representation of the object
print GetShortProjectsApiModel.to_json()

# convert the object into a dict
get_short_projects_api_model_dict = get_short_projects_api_model_instance.to_dict()
# create an instance of GetShortProjectsApiModel from a dict
get_short_projects_api_model_from_dict = GetShortProjectsApiModel.from_dict(get_short_projects_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


