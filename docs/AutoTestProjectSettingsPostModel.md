# AutoTestProjectSettingsPostModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rerun_enabled** | **bool** | Auto rerun enabled | 
**rerun_attempts_count** | **int** | Auto rerun attempt count | 
**is_flaky_auto** | **bool** | Indicates if the status \&quot;Flaky/Stable\&quot; sets automatically | [optional]  if omitted the server will use the default value of False
**flaky_stability_percentage** | **int** | Stability percentage for autotest flaky computing | [optional]  if omitted the server will use the default value of 100
**flaky_test_run_count** | **int** | Last test run count for autotest flaky computing | [optional]  if omitted the server will use the default value of 100

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


