# ExternalLinkModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**issue_type_name** | **str** |  | [optional] 
**issue_type_icon_url** | **str** |  | [optional] 
**priority_name** | **str** |  | [optional] 
**priority_icon_url** | **str** |  | [optional] 
**status_name** | **str** |  | [optional] 
**assignee_display_name** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.external_link_model import ExternalLinkModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalLinkModel from a JSON string
external_link_model_instance = ExternalLinkModel.from_json(json)
# print the JSON string representation of the object
print(ExternalLinkModel.to_json())

# convert the object into a dict
external_link_model_dict = external_link_model_instance.to_dict()
# create an instance of ExternalLinkModel from a dict
external_link_model_from_dict = ExternalLinkModel.from_dict(external_link_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


