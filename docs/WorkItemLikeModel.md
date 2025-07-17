# WorkItemLikeModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_item_id** | **str** |  | 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 

## Example

```python
from testit_api_client.models.work_item_like_model import WorkItemLikeModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemLikeModel from a JSON string
work_item_like_model_instance = WorkItemLikeModel.from_json(json)
# print the JSON string representation of the object
print WorkItemLikeModel.to_json()

# convert the object into a dict
work_item_like_model_dict = work_item_like_model_instance.to_dict()
# create an instance of WorkItemLikeModel from a dict
work_item_like_model_from_dict = WorkItemLikeModel.from_dict(work_item_like_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


