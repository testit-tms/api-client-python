# AutoTestResultHistoryApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**test_plan_id** | **str** |  | [optional] 
**test_plan_global_id** | **int** |  | [optional] 
**test_plan_name** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**test_run_id** | **str** |  | 
**test_run_name** | **str** |  | [optional] 
**configuration_id** | **str** |  | 
**configuration_name** | **str** |  | 
**outcome** | [**AutotestResultOutcome**](AutotestResultOutcome.md) |  | 
**status** | [**TestStatusApiResult**](TestStatusApiResult.md) |  | 
**launch_source** | **str** |  | [optional] 
**rerun_count** | **int** |  | 
**rerun_test_results** | [**List[RerunTestResultApiResult]**](RerunTestResultApiResult.md) |  | 
**created_date** | **datetime** |  | 
**created_by_id** | **str** |  | 
**created_by_name** | **str** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.auto_test_result_history_api_result import AutoTestResultHistoryApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestResultHistoryApiResult from a JSON string
auto_test_result_history_api_result_instance = AutoTestResultHistoryApiResult.from_json(json)
# print the JSON string representation of the object
print AutoTestResultHistoryApiResult.to_json()

# convert the object into a dict
auto_test_result_history_api_result_dict = auto_test_result_history_api_result_instance.to_dict()
# create an instance of AutoTestResultHistoryApiResult from a dict
auto_test_result_history_api_result_from_dict = AutoTestResultHistoryApiResult.from_dict(auto_test_result_history_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


