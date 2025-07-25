# TestResultHistoryReportApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal test result identifier | 
**created_date** | **datetime** | Test result creation date | 
**user_id** | **str** | Internal identifier of user who stopped test run related to the test result or user who created the test result                If test run was stopped, this property equals identifier of user who stopped it.  Otherwise, the property equals identifier of user who created the test result | 
**is_automated** | **bool** | Boolean flag defines if test point related to the test result is automated or not | 
**status** | [**TestResultHistoryReportApiResultStatus**](TestResultHistoryReportApiResultStatus.md) |  | 
**created_by_id** | **str** | Unique identifier of user who created first test result in the test run | 
**failure_class_ids** | **[str]** | Unique identifier of failure classes related to the first test result in the test run | 
**modified_date** | **datetime, none_type** | Test result last modification date | [optional] 
**test_run_id** | **str, none_type** | Identifier of test run related to the test result | [optional] 
**test_run_name** | **str, none_type** | Name of test run related to the test result | [optional] 
**created_by_user_name** | **str, none_type** | Username of user who created test run | [optional] 
**test_plan_id** | **str, none_type** | Internal identifier of test plan related to the test result&#39;s test run | [optional] 
**test_plan_global_id** | **int, none_type** | Global identifier of test plan related to the test result&#39;s test run | [optional] 
**test_plan_name** | **str, none_type** | Name of test plan related to the test result&#39;s test run | [optional] 
**configuration_name** | **str, none_type** | Configuration name of test point related to the test result or from test result itself                If test point related to the test result has configuration, this property will be equal to the test point configuration name.  Otherwise, this property will be equal to the test result configuration name | [optional] 
**outcome** | **str, none_type** | Outcome from test result with max modified date or from first created test result                Property can contain one of these values: Passed, Failed, InProgress, Blocked, Skipped.                If any test result related to the test run is linked with autotest and the run has an outcome, the outcome value equals to the  worst outcome of the last modified test result. Otherwise, the outcome equals to the outcome of first created test result in the  test run. | [optional] 
**comment** | **str, none_type** | Test result comment                If any test result related to the test run is linked with autotest, comment will have default value.  Otherwise, the comment equals to the comment of first created test result in the test run | [optional] 
**links** | [**[LinkApiResult], none_type**](LinkApiResult.md) | Test result links                If any test result related to the test run is linked with autotest, link will be equal to the links of last modified test result.  Otherwise, the links equals to the links of first created test result in the test run. | [optional] 
**started_on** | **datetime, none_type** | Start date time from test result or from test run (if test run new state is Running or Completed state) | [optional] 
**completed_on** | **datetime, none_type** | End date time from test result or from test run (if test run new state is In progress, Stopped or Completed) | [optional] 
**duration** | **int, none_type** | Duration of first created test result in the test run | [optional] 
**modified_by_id** | **str, none_type** | Unique identifier of user who applied last modification of first test result in the test run | [optional] 
**attachments** | [**[AttachmentApiResult], none_type**](AttachmentApiResult.md) | Attachments related to the test result                If any test result related to the test run is linked with autotest, attachments will be equal to the attachments of last modified  test result. Otherwise, the attachments equals to the attachments of first created test result in the test run. | [optional] 
**work_item_version_id** | **str, none_type** | Unique identifier of workitem version related to the first test result in the test run | [optional] 
**work_item_version_number** | **int, none_type** | Number of workitem version related to the first test result in the test run | [optional] 
**launch_source** | **str, none_type** |  | [optional] 
**parameters** | **{str: (str,)}, none_type** | Parameters of test result | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


