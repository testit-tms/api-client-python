# WorkItemCommentPostModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**work_item_id** | **str** |  | 

## Example

```python
from testit_api_client.models.work_item_comment_post_model import WorkItemCommentPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemCommentPostModel from a JSON string
work_item_comment_post_model_instance = WorkItemCommentPostModel.from_json(json)
# print the JSON string representation of the object
print WorkItemCommentPostModel.to_json()

# convert the object into a dict
work_item_comment_post_model_dict = work_item_comment_post_model_instance.to_dict()
# create an instance of WorkItemCommentPostModel from a dict
work_item_comment_post_model_from_dict = WorkItemCommentPostModel.from_dict(work_item_comment_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


