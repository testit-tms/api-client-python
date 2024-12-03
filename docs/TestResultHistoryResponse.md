# TestResultHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal test result identifier | 
**created_date** | **datetime** | Test result creation date | 
**modified_date** | **datetime** | Test result last modification date | 
**user_id** | **str** | Internal identifier of user who stopped test run related to the test result or user who created the test result                If test run was stopped, this property equals identifier of user who stopped it.  Otherwise, the property equals identifier of user who created the test result | 
**test_run_id** | **str** | Identifier of test run related to the test result | [optional] 
**test_run_name** | **str** | Name of test run related to the test result | [optional] 
**created_by_user_name** | **str** | Username of user who created test run | [optional] 
**test_plan_id** | **str** | Internal identifier of test plan related to the test result&#39;s test run | [optional] 
**test_plan_global_id** | **int** | Global identifier of test plan related to the test result&#39;s test run | [optional] 
**test_plan_name** | **str** | Name of test plan related to the test result&#39;s test run | [optional] 
**configuration_name** | **str** | Configuration name of test point related to the test result or from test result itself                If test point related to the test result has configuration, this property will be equal to the test point configuration name.  Otherwise, this property will be equal to the test result configuration name | [optional] 
**is_automated** | **bool** | Boolean flag defines if test point related to the test result is automated or not | 
**outcome** | **str** | Outcome from test result with max modified date or from first created test result                Property can contain one of these values: Passed, Failed, InProgress, Blocked, Skipped.                If any test result related to the test run is linked with autotest and the run has an outcome, the outcome value equals to the  worst outcome of the last modified test result. Otherwise, the outcome equals to the outcome of first created test result in the  test run. | [optional] 
**comment** | **str** | Test result comment                If any test result related to the test run is linked with autotest, comment will have default value.  Otherwise, the comment equals to the comment of first created test result in the test run | [optional] 
**links** | [**List[LinkModel]**](LinkModel.md) | Test result links                If any test result related to the test run is linked with autotest, link will be equal to the links of last modified test result.  Otherwise, the links equals to the links of first created test result in the test run. | [optional] 
**started_on** | **datetime** | Start date time from test result or from test run (if test run new state is Running or Completed state) | [optional] 
**completed_on** | **datetime** | End date time from test result or from test run (if test run new state is In progress, Stopped or Completed) | [optional] 
**duration** | **int** | Duration of first created test result in the test run | [optional] 
**created_by_id** | **str** | Unique identifier of user who created first test result in the test run | 
**modified_by_id** | **str** | Unique identifier of user who applied last modification of first test result in the test run | [optional] 
**attachments** | [**List[AttachmentModel]**](AttachmentModel.md) | Attachments related to the test result                If any test result related to the test run is linked with autotest, attachments will be equal to the attachments of last modified  test result. Otherwise, the attachments equals to the attachments of first created test result in the test run. | [optional] 
**work_item_version_id** | **str** | Unique identifier of workitem version related to the first test result in the test run | [optional] 
**work_item_version_number** | **int** | Number of workitem version related to the first test result in the test run | [optional] 
**launch_source** | **str** |  | [optional] 
**failure_class_ids** | **List[str]** | Unique identifier of failure classes related to the first test result in the test run | 
**parameters** | **Dict[str, str]** | Parameters of test result | [optional] 

## Example

```python
from testit_api_client.models.test_result_history_response import TestResultHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultHistoryResponse from a JSON string
test_result_history_response_instance = TestResultHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(TestResultHistoryResponse.to_json())

# convert the object into a dict
test_result_history_response_dict = test_result_history_response_instance.to_dict()
# create an instance of TestResultHistoryResponse from a dict
test_result_history_response_from_dict = TestResultHistoryResponse.from_dict(test_result_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


