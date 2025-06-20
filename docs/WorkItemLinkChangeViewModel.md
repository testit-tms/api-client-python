# WorkItemLinkChangeViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**url** | **str** |  | 
**title** | **str** |  | 
**has_info** | **bool** |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from testit_api_client.models.work_item_link_change_view_model import WorkItemLinkChangeViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemLinkChangeViewModel from a JSON string
work_item_link_change_view_model_instance = WorkItemLinkChangeViewModel.from_json(json)
# print the JSON string representation of the object
print(WorkItemLinkChangeViewModel.to_json())

# convert the object into a dict
work_item_link_change_view_model_dict = work_item_link_change_view_model_instance.to_dict()
# create an instance of WorkItemLinkChangeViewModel from a dict
work_item_link_change_view_model_from_dict = WorkItemLinkChangeViewModel.from_dict(work_item_link_change_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


