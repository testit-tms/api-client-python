# StringChangedFieldWithDiffsViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diff_value** | **str** |  | [optional] 
**old_value** | **str** |  | [optional] 
**new_value** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.string_changed_field_with_diffs_view_model import StringChangedFieldWithDiffsViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of StringChangedFieldWithDiffsViewModel from a JSON string
string_changed_field_with_diffs_view_model_instance = StringChangedFieldWithDiffsViewModel.from_json(json)
# print the JSON string representation of the object
print StringChangedFieldWithDiffsViewModel.to_json()

# convert the object into a dict
string_changed_field_with_diffs_view_model_dict = string_changed_field_with_diffs_view_model_instance.to_dict()
# create an instance of StringChangedFieldWithDiffsViewModel from a dict
string_changed_field_with_diffs_view_model_from_dict = StringChangedFieldWithDiffsViewModel.from_dict(string_changed_field_with_diffs_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


