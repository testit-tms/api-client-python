# AutoTest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | External ID of the autotest | 
**project_id** | **str** | Unique ID of the autotest project | 
**name** | **str** | Name of the autotest | 
**global_id** | **int** | Global ID of the autotest | 
**is_deleted** | **bool** | Indicates if the autotest is deleted | 
**must_be_approved** | **bool** | Indicates if the autotest has unapproved changes from linked work items | 
**id** | **str** | Unique ID of the autotest | 
**created_date** | **datetime** | Creation date of the autotest | 
**created_by_id** | **str** | Unique ID of the project creator | 
**links** | [**[Link], none_type**](Link.md) | Collection of the autotest links | [optional] 
**namespace** | **str, none_type** | Name of the autotest namespace | [optional] 
**classname** | **str, none_type** | Name of the autotest class | [optional] 
**steps** | [**[AutoTestStep], none_type**](AutoTestStep.md) | Collection of the autotest steps | [optional] 
**setup** | [**[AutoTestStep], none_type**](AutoTestStep.md) | Collection of the autotest setup steps | [optional] 
**teardown** | [**[AutoTestStep], none_type**](AutoTestStep.md) | Collection of the autotest teardown steps | [optional] 
**title** | **str, none_type** | Name of the autotest in autotest&#39;s card | [optional] 
**description** | **str, none_type** | Description of the autotest in autotest&#39;s card | [optional] 
**labels** | [**[Label], none_type**](Label.md) | Collection of the autotest labels | [optional] 
**is_flaky** | **bool, none_type** | Indicates if the autotest is marked as flaky | [optional] 
**external_key** | **str, none_type** | External key of the autotest | [optional] 
**modified_date** | **datetime, none_type** | Last modification date of the project | [optional] 
**modified_by_id** | **str, none_type** | Unique ID of the project last editor | [optional] 
**last_test_run_id** | **str, none_type** | Unique ID of the autotest last test run | [optional] 
**last_test_run_name** | **str, none_type** | Name of the autotest last test run | [optional] 
**last_test_result_id** | **str, none_type** | Unique ID of the autotest last test result | [optional] 
**last_test_result_configuration** | [**AutoTestLastTestResultConfiguration**](AutoTestLastTestResultConfiguration.md) |  | [optional] 
**last_test_result_outcome** | **str, none_type** | Outcome of the autotest last test result | [optional] 
**stability_percentage** | **int, none_type** | Stability percentage of the autotest | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


