# WorkItemCommentPutModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text of the comment | 
**id** | **str** | Unique ID of the comment | 

## Example

```python
from testit_api_client.models.work_item_comment_put_model import WorkItemCommentPutModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemCommentPutModel from a JSON string
work_item_comment_put_model_instance = WorkItemCommentPutModel.from_json(json)
# print the JSON string representation of the object
print(WorkItemCommentPutModel.to_json())

# convert the object into a dict
work_item_comment_put_model_dict = work_item_comment_put_model_instance.to_dict()
# create an instance of WorkItemCommentPutModel from a dict
work_item_comment_put_model_from_dict = WorkItemCommentPutModel.from_dict(work_item_comment_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


