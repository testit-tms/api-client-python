# WorkItemChangeModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**work_item_id** | **str** |  | 
**old_version_id** | **str** |  | 
**new_version_id** | **str** |  | 
**work_item_changed_fields** | [**WorkItemChangedFieldsViewModel**](WorkItemChangedFieldsViewModel.md) |  | 
**created_by_id** | **str** |  | 
**created_date** | **datetime** |  | [optional] 

## Example

```python
from testit_api_client.models.work_item_change_model import WorkItemChangeModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemChangeModel from a JSON string
work_item_change_model_instance = WorkItemChangeModel.from_json(json)
# print the JSON string representation of the object
print WorkItemChangeModel.to_json()

# convert the object into a dict
work_item_change_model_dict = work_item_change_model_instance.to_dict()
# create an instance of WorkItemChangeModel from a dict
work_item_change_model_from_dict = WorkItemChangeModel.from_dict(work_item_change_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


