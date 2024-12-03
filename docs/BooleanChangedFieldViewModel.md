# BooleanChangedFieldViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_value** | **bool** |  | 
**new_value** | **bool** |  | 

## Example

```python
from testit_api_client.models.boolean_changed_field_view_model import BooleanChangedFieldViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanChangedFieldViewModel from a JSON string
boolean_changed_field_view_model_instance = BooleanChangedFieldViewModel.from_json(json)
# print the JSON string representation of the object
print(BooleanChangedFieldViewModel.to_json())

# convert the object into a dict
boolean_changed_field_view_model_dict = boolean_changed_field_view_model_instance.to_dict()
# create an instance of BooleanChangedFieldViewModel from a dict
boolean_changed_field_view_model_from_dict = BooleanChangedFieldViewModel.from_dict(boolean_changed_field_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


