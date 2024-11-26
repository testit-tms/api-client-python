# ApiV2TestRunsSearchPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **[str], none_type** | Specifies a test run project IDs to search for | [optional] 
**name** | **str, none_type** | Specifies test run name | [optional] 
**states** | [**[TestRunState], none_type**](TestRunState.md) | Specifies a test run states to search for | [optional] 
**created_date** | [**TestRunFilterModelCreatedDate**](TestRunFilterModelCreatedDate.md) |  | [optional] 
**started_date** | [**TestRunFilterModelStartedDate**](TestRunFilterModelStartedDate.md) |  | [optional] 
**created_by_ids** | **[str], none_type** | Specifies a test run creator IDs to search for | [optional] 
**modified_by_ids** | **[str], none_type** | Specifies a test run last editor IDs to search for | [optional] 
**is_deleted** | **bool, none_type** | Specifies a test run deleted status to search for | [optional] 
**auto_tests_count** | [**TestRunFilterModelAutoTestsCount**](TestRunFilterModelAutoTestsCount.md) |  | [optional] 
**test_results_outcome** | [**[TestResultOutcome], none_type**](TestResultOutcome.md) | Specifies test results outcomes | [optional] 
**failure_category** | [**[FailureCategoryModel], none_type**](FailureCategoryModel.md) | Specifies failure categories | [optional] 
**completed_date** | [**TestRunFilterModelCompletedDate**](TestRunFilterModelCompletedDate.md) |  | [optional] 
**test_results_configuration_ids** | **[str], none_type** | Specifies a test result configuration IDs to search for | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


