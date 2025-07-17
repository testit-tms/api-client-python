# WorkItemCommentModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**text** | **str** |  | 
**user** | [**UserWithRankModel**](UserWithRankModel.md) |  | 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 

## Example

```python
from testit_api_client.models.work_item_comment_model import WorkItemCommentModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemCommentModel from a JSON string
work_item_comment_model_instance = WorkItemCommentModel.from_json(json)
# print the JSON string representation of the object
print WorkItemCommentModel.to_json()

# convert the object into a dict
work_item_comment_model_dict = work_item_comment_model_instance.to_dict()
# create an instance of WorkItemCommentModel from a dict
work_item_comment_model_from_dict = WorkItemCommentModel.from_dict(work_item_comment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


