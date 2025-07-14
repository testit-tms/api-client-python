# WorkItemMovePostModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**new_section_id** | **str** |  | 
**old_section_id** | **str** |  | [optional] 
**next_work_item_id** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.work_item_move_post_model import WorkItemMovePostModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemMovePostModel from a JSON string
work_item_move_post_model_instance = WorkItemMovePostModel.from_json(json)
# print the JSON string representation of the object
print WorkItemMovePostModel.to_json()

# convert the object into a dict
work_item_move_post_model_dict = work_item_move_post_model_instance.to_dict()
# create an instance of WorkItemMovePostModel from a dict
work_item_move_post_model_from_dict = WorkItemMovePostModel.from_dict(work_item_move_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


