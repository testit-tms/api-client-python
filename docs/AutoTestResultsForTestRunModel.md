# AutoTestResultsForTestRunModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_id** | **str** | Specifies the GUID of the autotest configuration, which was specified when the test run was created. | 
**auto_test_external_id** | **str** | Specifies the external ID of the autotest, which was specified when the test run was created. | 
**links** | [**[LinkPostModel], none_type**](LinkPostModel.md) | Specifies the links in the autotest. | [optional] 
**failure_reason_names** | [**[FailureCategoryModel], none_type**](FailureCategoryModel.md) | Specifies the cause of autotest failure. | [optional] 
**outcome** | [**AvailableTestResultOutcome**](AvailableTestResultOutcome.md) |  | [optional] 
**status_code** | **str, none_type** | Specifies the result of the autotest execution. | [optional] 
**message** | **str, none_type** | A comment for the result. | [optional] 
**traces** | **str, none_type** | An extended comment or a stack trace. | [optional] 
**started_on** | **datetime, none_type** | Test run start date. | [optional] 
**completed_on** | **datetime, none_type** | Test run end date. | [optional] 
**duration** | **int, none_type** | Expected or actual duration of the test run execution in milliseconds. | [optional] 
**attachments** | [**[AttachmentPutModel], none_type**](AttachmentPutModel.md) | Specifies an attachment GUID. Multiple values can be sent. | [optional] 
**parameters** | **{str: (str,)}, none_type** | \&quot;&lt;b&gt;parameter&lt;/b&gt;\&quot;: \&quot;&lt;b&gt;value&lt;/b&gt;\&quot; pair with arbitrary custom parameters. Multiple parameters can be sent. | [optional] 
**properties** | **{str: (str,)}, none_type** | \&quot;&lt;b&gt;property&lt;/b&gt;\&quot;: \&quot;&lt;b&gt;value&lt;/b&gt;\&quot; pair with arbitrary custom properties. Multiple properties can be sent. | [optional] 
**step_results** | [**[AttachmentPutModelAutoTestStepResultsModel], none_type**](AttachmentPutModelAutoTestStepResultsModel.md) | Specifies the results of individual steps. | [optional] 
**setup_results** | [**[AttachmentPutModelAutoTestStepResultsModel], none_type**](AttachmentPutModelAutoTestStepResultsModel.md) | Specifies the results of setup steps. For information on supported values, see the &#x60;stepResults&#x60; parameter above. | [optional] 
**teardown_results** | [**[AttachmentPutModelAutoTestStepResultsModel], none_type**](AttachmentPutModelAutoTestStepResultsModel.md) | Specifies the results of the teardown steps. For information on supported values, see the &#x60;stepResults&#x60; parameter above. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


