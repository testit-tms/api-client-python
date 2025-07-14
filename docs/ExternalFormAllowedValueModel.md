# ExternalFormAllowedValueModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**has_children** | **bool** |  | 

## Example

```python
from testit_api_client.models.external_form_allowed_value_model import ExternalFormAllowedValueModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalFormAllowedValueModel from a JSON string
external_form_allowed_value_model_instance = ExternalFormAllowedValueModel.from_json(json)
# print the JSON string representation of the object
print ExternalFormAllowedValueModel.to_json()

# convert the object into a dict
external_form_allowed_value_model_dict = external_form_allowed_value_model_instance.to_dict()
# create an instance of ExternalFormAllowedValueModel from a dict
external_form_allowed_value_model_from_dict = ExternalFormAllowedValueModel.from_dict(external_form_allowed_value_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


