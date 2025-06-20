# WorkItemChangedFieldsViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**StringChangedFieldWithDiffsViewModel**](StringChangedFieldWithDiffsViewModel.md) |  | [optional] 
**is_deleted** | [**BooleanChangedFieldViewModel**](BooleanChangedFieldViewModel.md) |  | 
**project_id** | [**GuidChangedFieldViewModel**](GuidChangedFieldViewModel.md) |  | 
**is_automated** | [**BooleanChangedFieldViewModel**](BooleanChangedFieldViewModel.md) |  | 
**section_id** | [**GuidChangedFieldViewModel**](GuidChangedFieldViewModel.md) |  | 
**description** | [**StringChangedFieldWithDiffsViewModel**](StringChangedFieldWithDiffsViewModel.md) |  | [optional] 
**state** | [**StringChangedFieldViewModel**](StringChangedFieldViewModel.md) |  | 
**priority** | [**StringChangedFieldViewModel**](StringChangedFieldViewModel.md) |  | 
**duration** | [**Int32ChangedFieldViewModel**](Int32ChangedFieldViewModel.md) |  | 
**attributes** | [**Dict[str, WorkItemChangedAttributeViewModel]**](WorkItemChangedAttributeViewModel.md) |  | 
**steps** | [**WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel**](WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel.md) |  | 
**precondition_steps** | [**WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel**](WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel.md) |  | 
**postcondition_steps** | [**WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel**](WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel.md) |  | 
**auto_tests** | [**AutoTestChangeViewModelArrayChangedFieldViewModel**](AutoTestChangeViewModelArrayChangedFieldViewModel.md) |  | 
**attachments** | [**AttachmentChangeViewModelArrayChangedFieldViewModel**](AttachmentChangeViewModelArrayChangedFieldViewModel.md) |  | 
**tags** | [**StringArrayChangedFieldViewModel**](StringArrayChangedFieldViewModel.md) |  | 
**links** | [**WorkItemLinkChangeViewModelArrayChangedFieldViewModel**](WorkItemLinkChangeViewModelArrayChangedFieldViewModel.md) |  | 
**global_id** | [**Int64ChangedFieldViewModel**](Int64ChangedFieldViewModel.md) |  | 
**version_number** | [**Int32ChangedFieldViewModel**](Int32ChangedFieldViewModel.md) |  | 
**entity_type_name** | [**StringChangedFieldViewModel**](StringChangedFieldViewModel.md) |  | 

## Example

```python
from testit_api_client.models.work_item_changed_fields_view_model import WorkItemChangedFieldsViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemChangedFieldsViewModel from a JSON string
work_item_changed_fields_view_model_instance = WorkItemChangedFieldsViewModel.from_json(json)
# print the JSON string representation of the object
print(WorkItemChangedFieldsViewModel.to_json())

# convert the object into a dict
work_item_changed_fields_view_model_dict = work_item_changed_fields_view_model_instance.to_dict()
# create an instance of WorkItemChangedFieldsViewModel from a dict
work_item_changed_fields_view_model_from_dict = WorkItemChangedFieldsViewModel.from_dict(work_item_changed_fields_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


