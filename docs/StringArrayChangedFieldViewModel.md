# StringArrayChangedFieldViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_value** | **List[str]** |  | [optional] 
**new_value** | **List[str]** |  | [optional] 

## Example

```python
from testit_api_client.models.string_array_changed_field_view_model import StringArrayChangedFieldViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of StringArrayChangedFieldViewModel from a JSON string
string_array_changed_field_view_model_instance = StringArrayChangedFieldViewModel.from_json(json)
# print the JSON string representation of the object
print(StringArrayChangedFieldViewModel.to_json())

# convert the object into a dict
string_array_changed_field_view_model_dict = string_array_changed_field_view_model_instance.to_dict()
# create an instance of StringArrayChangedFieldViewModel from a dict
string_array_changed_field_view_model_from_dict = StringArrayChangedFieldViewModel.from_dict(string_array_changed_field_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


