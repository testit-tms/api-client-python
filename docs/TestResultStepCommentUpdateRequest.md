# TestResultStepCommentUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity unique identifier | 
**text** | **str** |  | 
**step_id** | **str** |  | 
**parent_step_id** | **str** |  | [optional] 
**attachments** | [**List[AttachmentUpdateRequest]**](AttachmentUpdateRequest.md) |  | 

## Example

```python
from testit_api_client.models.test_result_step_comment_update_request import TestResultStepCommentUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultStepCommentUpdateRequest from a JSON string
test_result_step_comment_update_request_instance = TestResultStepCommentUpdateRequest.from_json(json)
# print the JSON string representation of the object
print TestResultStepCommentUpdateRequest.to_json()

# convert the object into a dict
test_result_step_comment_update_request_dict = test_result_step_comment_update_request_instance.to_dict()
# create an instance of TestResultStepCommentUpdateRequest from a dict
test_result_step_comment_update_request_from_dict = TestResultStepCommentUpdateRequest.from_dict(test_result_step_comment_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


