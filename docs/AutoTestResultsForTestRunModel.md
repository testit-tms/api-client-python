# AutoTestResultsForTestRunModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_id** | **str** | Specifies the GUID of the autotest configuration, which was specified when the test run was created. | 
**links** | [**List[LinkPostModel]**](LinkPostModel.md) | Specifies the links in the autotest. | [optional] 
**failure_reason_names** | [**List[FailureCategoryModel]**](FailureCategoryModel.md) | Specifies the cause of autotest failure. | [optional] 
**auto_test_external_id** | **str** | Specifies the external ID of the autotest, which was specified when the test run was created. | 
**outcome** | [**AvailableTestResultOutcome**](AvailableTestResultOutcome.md) | Specifies the result of the autotest execution. | 
**message** | **str** | A comment for the result. | [optional] 
**traces** | **str** | An extended comment or a stack trace. | [optional] 
**started_on** | **datetime** | Test run start date. | [optional] 
**completed_on** | **datetime** | Test run end date. | [optional] 
**duration** | **int** | Expected or actual duration of the test run execution in milliseconds. | [optional] 
**attachments** | [**List[AttachmentPutModel]**](AttachmentPutModel.md) | Specifies an attachment GUID. Multiple values can be sent. | [optional] 
**parameters** | **Dict[str, str]** | \&quot;&lt;b&gt;parameter&lt;/b&gt;\&quot;: \&quot;&lt;b&gt;value&lt;/b&gt;\&quot; pair with arbitrary custom parameters. Multiple parameters can be sent. | [optional] 
**properties** | **Dict[str, str]** | \&quot;&lt;b&gt;property&lt;/b&gt;\&quot;: \&quot;&lt;b&gt;value&lt;/b&gt;\&quot; pair with arbitrary custom properties. Multiple properties can be sent. | [optional] 
**step_results** | [**List[AttachmentPutModelAutoTestStepResultsModel]**](AttachmentPutModelAutoTestStepResultsModel.md) | Specifies the results of individual steps. | [optional] 
**setup_results** | [**List[AttachmentPutModelAutoTestStepResultsModel]**](AttachmentPutModelAutoTestStepResultsModel.md) | Specifies the results of setup steps. For information on supported values, see the &#x60;stepResults&#x60; parameter above. | [optional] 
**teardown_results** | [**List[AttachmentPutModelAutoTestStepResultsModel]**](AttachmentPutModelAutoTestStepResultsModel.md) | Specifies the results of the teardown steps. For information on supported values, see the &#x60;stepResults&#x60; parameter above. | [optional] 

## Example

```python
from testit_api_client.models.auto_test_results_for_test_run_model import AutoTestResultsForTestRunModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestResultsForTestRunModel from a JSON string
auto_test_results_for_test_run_model_instance = AutoTestResultsForTestRunModel.from_json(json)
# print the JSON string representation of the object
print(AutoTestResultsForTestRunModel.to_json())

# convert the object into a dict
auto_test_results_for_test_run_model_dict = auto_test_results_for_test_run_model_instance.to_dict()
# create an instance of AutoTestResultsForTestRunModel from a dict
auto_test_results_for_test_run_model_from_dict = AutoTestResultsForTestRunModel.from_dict(auto_test_results_for_test_run_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


