# WorkItemStepChangeViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**expected** | **str** |  | 
**comments** | **str** |  | 
**test_data** | **str** |  | 
**index** | **int** |  | 
**work_item_id** | **str** |  | [optional] 
**work_item** | [**SharedStepChangeViewModel**](SharedStepChangeViewModel.md) |  | 

## Example

```python
from testit_api_client.models.work_item_step_change_view_model import WorkItemStepChangeViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemStepChangeViewModel from a JSON string
work_item_step_change_view_model_instance = WorkItemStepChangeViewModel.from_json(json)
# print the JSON string representation of the object
print WorkItemStepChangeViewModel.to_json()

# convert the object into a dict
work_item_step_change_view_model_dict = work_item_step_change_view_model_instance.to_dict()
# create an instance of WorkItemStepChangeViewModel from a dict
work_item_step_change_view_model_from_dict = WorkItemStepChangeViewModel.from_dict(work_item_step_change_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


