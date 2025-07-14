# WorkItemChangedAttributeViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**old_attribute_name** | **str** |  | 
**new_attribute_name** | **str** |  | 
**old_value** | **object** |  | 
**new_value** | **object** |  | 

## Example

```python
from testit_api_client.models.work_item_changed_attribute_view_model import WorkItemChangedAttributeViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemChangedAttributeViewModel from a JSON string
work_item_changed_attribute_view_model_instance = WorkItemChangedAttributeViewModel.from_json(json)
# print the JSON string representation of the object
print WorkItemChangedAttributeViewModel.to_json()

# convert the object into a dict
work_item_changed_attribute_view_model_dict = work_item_changed_attribute_view_model_instance.to_dict()
# create an instance of WorkItemChangedAttributeViewModel from a dict
work_item_changed_attribute_view_model_from_dict = WorkItemChangedAttributeViewModel.from_dict(work_item_changed_attribute_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


