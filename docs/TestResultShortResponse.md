# TestResultShortResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the test result | 
**name** | **str** | Name of autotest represented by the test result | 
**autotest_global_id** | **int** | Global ID of autotest represented by the test result | 
**auto_test_tags** | **[str]** | Tags of the autotest represented by the test result | 
**test_run_id** | **str** | Unique ID of test run where the test result is located | 
**configuration_id** | **str** | Unique ID of configuration which the test result uses | 
**configuration_name** | **str** | Name of configuration which the test result uses | 
**status** | [**AutoTestResultHistoryApiResultStatus**](AutoTestResultHistoryApiResultStatus.md) |  | 
**result_reasons** | [**[AutoTestResultReasonShort]**](AutoTestResultReasonShort.md) | Collection of result reasons which the test result have | 
**date** | **datetime** | Date when the test result was completed or started or created | 
**created_date** | **datetime** | Date when the test result has been created | 
**links** | [**[LinkShort]**](LinkShort.md) | Collection of links attached to the test result | 
**attachments** | [**[AttachmentApiResult]**](AttachmentApiResult.md) | Collection of files attached to the test result | 
**rerun_completed_count** | **int** | Run count | 
**autotest_external_id** | **str, none_type** | External ID of autotest represented by the test result | [optional] 
**outcome** | **str, none_type** | Outcome of the test result | [optional] 
**comment** | **str, none_type** | Comment to the test result | [optional] 
**modified_date** | **datetime, none_type** | Date when the test result has been modified | [optional] 
**started_on** | **datetime, none_type** | Date when the test result has been started | [optional] 
**completed_on** | **datetime, none_type** | Date when the test result has been completed | [optional] 
**duration** | **int, none_type** | Time which it took to run the test | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


