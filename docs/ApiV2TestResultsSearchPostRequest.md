# ApiV2TestResultsSearchPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_ids** | **[str], none_type** | Specifies a test result configuration IDs to search for | [optional] 
**outcomes** | [**[TestResultOutcome], none_type**](TestResultOutcome.md) | Specifies a test result outcomes to search for | [optional] 
**status_codes** | **[str], none_type** | Specifies a test result status codes to search for | [optional] 
**failure_categories** | [**[FailureCategoryModel], none_type**](FailureCategoryModel.md) | Specifies a test result failure categories to search for | [optional] 
**namespace** | **str, none_type** | Specifies a test result namespace to search for | [optional] 
**class_name** | **str, none_type** | Specifies a test result class name to search for | [optional] 
**auto_test_global_ids** | **[int], none_type** | Specifies an autotest global IDs to search results for | [optional] 
**name** | **str, none_type** | Specifies an autotest name to search results for | [optional] 
**created_date** | [**TestResultsFilterApiModelCreatedDate**](TestResultsFilterApiModelCreatedDate.md) |  | [optional] 
**modified_date** | [**TestResultsFilterApiModelModifiedDate**](TestResultsFilterApiModelModifiedDate.md) |  | [optional] 
**started_on** | [**TestResultsFilterApiModelStartedOn**](TestResultsFilterApiModelStartedOn.md) |  | [optional] 
**completed_on** | [**TestResultsFilterApiModelCompletedOn**](TestResultsFilterApiModelCompletedOn.md) |  | [optional] 
**duration** | [**TestResultsFilterApiModelDuration**](TestResultsFilterApiModelDuration.md) |  | [optional] 
**result_reasons** | **[str], none_type** | Specifies result reasons for searching test results | [optional] 
**test_run_ids** | **[str], none_type** | Specifies a test result test run IDs to search for | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


