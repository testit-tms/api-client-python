# AttachmentPutModelAutoTestStepResultsModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The name of the step. | [optional] 
**description** | **str** | Description of the step result. | [optional] 
**info** | **str** | Extended description of the step result. | [optional] 
**started_on** | **datetime** | Step start date. | [optional] 
**completed_on** | **datetime** | Step end date. | [optional] 
**duration** | **int** | Expected or actual duration of the test run execution in milliseconds. | [optional] 
**outcome** | [**AvailableTestResultOutcome**](AvailableTestResultOutcome.md) | Specifies the result of the autotest execution. | [optional] 
**step_results** | [**List[AttachmentPutModelAutoTestStepResultsModel]**](AttachmentPutModelAutoTestStepResultsModel.md) | Nested step results. The maximum nesting level is 15. | [optional] 
**attachments** | [**List[AttachmentPutModel]**](AttachmentPutModel.md) | /// &lt;summary&gt; Specifies an attachment GUID. Multiple values can be sent. &lt;/summary&gt; | [optional] 
**parameters** | **Dict[str, str]** | \&quot;&lt;b&gt;parameter&lt;/b&gt;\&quot;: \&quot;&lt;b&gt;value&lt;/b&gt;\&quot; pair with arbitrary custom parameters. Multiple parameters can be sent. | [optional] 

## Example

```python
from testit_api_client.models.attachment_put_model_auto_test_step_results_model import AttachmentPutModelAutoTestStepResultsModel

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentPutModelAutoTestStepResultsModel from a JSON string
attachment_put_model_auto_test_step_results_model_instance = AttachmentPutModelAutoTestStepResultsModel.from_json(json)
# print the JSON string representation of the object
print AttachmentPutModelAutoTestStepResultsModel.to_json()

# convert the object into a dict
attachment_put_model_auto_test_step_results_model_dict = attachment_put_model_auto_test_step_results_model_instance.to_dict()
# create an instance of AttachmentPutModelAutoTestStepResultsModel from a dict
attachment_put_model_auto_test_step_results_model_from_dict = AttachmentPutModelAutoTestStepResultsModel.from_dict(attachment_put_model_auto_test_step_results_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


