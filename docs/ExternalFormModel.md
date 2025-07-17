# ExternalFormModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[ExternalFormFieldModel]**](ExternalFormFieldModel.md) |  | 
**possible_values** | **Dict[str, List[ExternalFormAllowedValueModel]]** |  | 

## Example

```python
from testit_api_client.models.external_form_model import ExternalFormModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalFormModel from a JSON string
external_form_model_instance = ExternalFormModel.from_json(json)
# print the JSON string representation of the object
print ExternalFormModel.to_json()

# convert the object into a dict
external_form_model_dict = external_form_model_instance.to_dict()
# create an instance of ExternalFormModel from a dict
external_form_model_from_dict = ExternalFormModel.from_dict(external_form_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


