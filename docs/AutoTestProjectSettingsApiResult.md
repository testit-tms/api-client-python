# AutoTestProjectSettingsApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Unique ID of the project. | 
**is_flaky_auto** | **bool** | Indicates if the status \&quot;Flaky/Stable\&quot; sets automatically | 
**flaky_stability_percentage** | **int** | Stability percentage for autotest flaky computing | 
**flaky_test_run_count** | **int** | Last test run count for autotest flaky computing | 
**rerun_enabled** | **bool** | Auto rerun enabled | 
**rerun_attempts_count** | **int** | Auto rerun attempt count | 
**work_item_updating_enabled** | **bool** | Autotest to work item updating enabled | 
**work_item_updating_fields** | [**AutoTestProjectSettingsApiResultWorkItemUpdatingFields**](AutoTestProjectSettingsApiResultWorkItemUpdatingFields.md) |  | 
**archive_outdated_test_runs_enabled** | **bool** | Indicates whether archiving of outdated test runs is enabled for the project. | 
**test_runs_archive_limit_enabled** | **bool** | Indicates whether a limit is enforced on the number of archived test runs. | 
**test_runs_retention_period_days** | **int** |  The retention period in days for test runs. After this period, outdated test runs may be archived based on project settings | 
**max_active_test_runs_count** | **int** | Maximum number of active test runs to keep. When this limit is exceeded, older test runs are automatically archived | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


