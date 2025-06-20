# StringChangedFieldViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_value** | **str** |  | [optional] 
**new_value** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.string_changed_field_view_model import StringChangedFieldViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of StringChangedFieldViewModel from a JSON string
string_changed_field_view_model_instance = StringChangedFieldViewModel.from_json(json)
# print the JSON string representation of the object
print(StringChangedFieldViewModel.to_json())

# convert the object into a dict
string_changed_field_view_model_dict = string_changed_field_view_model_instance.to_dict()
# create an instance of StringChangedFieldViewModel from a dict
string_changed_field_view_model_from_dict = StringChangedFieldViewModel.from_dict(string_changed_field_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


