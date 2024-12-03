# ExternalFormFieldModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **str** |  | [optional] 
**field_name** | **str** |  | [optional] 
**help_text** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**array_values_type** | **str** |  | [optional] 
**default_value** | **object** |  | [optional] 
**is_custom_value_allowed** | **bool** |  | 
**auto_complete_url** | **str** |  | [optional] 
**control_type** | **str** |  | [optional] 
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**min** | **object** |  | [optional] 
**max** | **object** |  | [optional] 

## Example

```python
from testit_api_client.models.external_form_field_model import ExternalFormFieldModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalFormFieldModel from a JSON string
external_form_field_model_instance = ExternalFormFieldModel.from_json(json)
# print the JSON string representation of the object
print(ExternalFormFieldModel.to_json())

# convert the object into a dict
external_form_field_model_dict = external_form_field_model_instance.to_dict()
# create an instance of ExternalFormFieldModel from a dict
external_form_field_model_from_dict = ExternalFormFieldModel.from_dict(external_form_field_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


