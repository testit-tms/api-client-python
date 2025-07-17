# ExternalFormCreateModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**possible_values** | **Dict[str, List[ExternalFormAllowedValueModel]]** |  | 
**fields** | [**List[ExternalFormFieldModel]**](ExternalFormFieldModel.md) |  | 
**links** | [**List[ExternalFormLinkModel]**](ExternalFormLinkModel.md) |  | 
**values** | **Dict[str, object]** |  | 

## Example

```python
from testit_api_client.models.external_form_create_model import ExternalFormCreateModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalFormCreateModel from a JSON string
external_form_create_model_instance = ExternalFormCreateModel.from_json(json)
# print the JSON string representation of the object
print ExternalFormCreateModel.to_json()

# convert the object into a dict
external_form_create_model_dict = external_form_create_model_instance.to_dict()
# create an instance of ExternalFormCreateModel from a dict
external_form_create_model_from_dict = ExternalFormCreateModel.from_dict(external_form_create_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


