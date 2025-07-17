# GuidChangedFieldViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_value** | **str** |  | 
**new_value** | **str** |  | 

## Example

```python
from testit_api_client.models.guid_changed_field_view_model import GuidChangedFieldViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of GuidChangedFieldViewModel from a JSON string
guid_changed_field_view_model_instance = GuidChangedFieldViewModel.from_json(json)
# print the JSON string representation of the object
print GuidChangedFieldViewModel.to_json()

# convert the object into a dict
guid_changed_field_view_model_dict = guid_changed_field_view_model_instance.to_dict()
# create an instance of GuidChangedFieldViewModel from a dict
guid_changed_field_view_model_from_dict = GuidChangedFieldViewModel.from_dict(guid_changed_field_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


