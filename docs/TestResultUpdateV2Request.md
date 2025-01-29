# TestResultUpdateV2Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_class_ids** | **List[str]** |  | [optional] 
**outcome** | [**TestResultOutcome**](TestResultOutcome.md) |  | [optional] 
**status_code** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**step_results** | [**List[StepResult]**](StepResult.md) |  | [optional] 
**attachments** | [**List[AttachmentUpdateRequest]**](AttachmentUpdateRequest.md) |  | [optional] 
**duration_in_ms** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**step_comments** | [**List[TestResultStepCommentUpdateRequest]**](TestResultStepCommentUpdateRequest.md) |  | [optional] 
**setup_results** | [**List[AttachmentPutModelAutoTestStepResultsModel]**](AttachmentPutModelAutoTestStepResultsModel.md) |  | [optional] 
**teardown_results** | [**List[AttachmentPutModelAutoTestStepResultsModel]**](AttachmentPutModelAutoTestStepResultsModel.md) |  | [optional] 
**message** | **str** |  | [optional] 
**trace** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.test_result_update_v2_request import TestResultUpdateV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultUpdateV2Request from a JSON string
test_result_update_v2_request_instance = TestResultUpdateV2Request.from_json(json)
# print the JSON string representation of the object
print(TestResultUpdateV2Request.to_json())

# convert the object into a dict
test_result_update_v2_request_dict = test_result_update_v2_request_instance.to_dict()
# create an instance of TestResultUpdateV2Request from a dict
test_result_update_v2_request_from_dict = TestResultUpdateV2Request.from_dict(test_result_update_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


