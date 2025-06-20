# StepCommentApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**text** | **str** |  | [optional] 
**step_id** | **str** |  | 
**parent_step_id** | **str** |  | [optional] 
**attachments** | [**List[AttachmentApiResult]**](AttachmentApiResult.md) |  | 
**test_result_id** | **str** |  | 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 

## Example

```python
from testit_api_client.models.step_comment_api_model import StepCommentApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of StepCommentApiModel from a JSON string
step_comment_api_model_instance = StepCommentApiModel.from_json(json)
# print the JSON string representation of the object
print(StepCommentApiModel.to_json())

# convert the object into a dict
step_comment_api_model_dict = step_comment_api_model_instance.to_dict()
# create an instance of StepCommentApiModel from a dict
step_comment_api_model_from_dict = StepCommentApiModel.from_dict(step_comment_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


