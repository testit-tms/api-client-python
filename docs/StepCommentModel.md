# StepCommentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**text** | **str** |  | [optional] 
**step_id** | **str** |  | 
**parent_step_id** | **str** |  | [optional] 
**attachments** | [**List[AttachmentModel]**](AttachmentModel.md) |  | [optional] 
**test_result_id** | **str** |  | 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 

## Example

```python
from testit_api_client.models.step_comment_model import StepCommentModel

# TODO update the JSON string below
json = "{}"
# create an instance of StepCommentModel from a JSON string
step_comment_model_instance = StepCommentModel.from_json(json)
# print the JSON string representation of the object
print(StepCommentModel.to_json())

# convert the object into a dict
step_comment_model_dict = step_comment_model_instance.to_dict()
# create an instance of StepCommentModel from a dict
step_comment_model_from_dict = StepCommentModel.from_dict(step_comment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


