# AutotestResultHistoricalGetModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modified_date** | **datetime** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**test_plan_id** | **str** |  | [optional] 
**test_plan_global_id** | **int** |  | [optional] 
**test_plan_name** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**id** | **str** |  | 
**created_date** | **datetime** |  | 
**created_by_id** | **str** |  | 
**created_by_name** | **str** |  | 
**test_run_id** | **str** |  | 
**test_run_name** | **str** |  | [optional] 
**configuration_id** | **str** |  | 
**configuration_name** | **str** |  | 
**outcome** | [**AutotestResultOutcome**](AutotestResultOutcome.md) |  | 
**launch_source** | **str** |  | [optional] 
**rerun_count** | **int** |  | 
**rerun_test_results** | [**List[RerunTestResultModel]**](RerunTestResultModel.md) |  | 

## Example

```python
from testit_api_client.models.autotest_result_historical_get_model import AutotestResultHistoricalGetModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutotestResultHistoricalGetModel from a JSON string
autotest_result_historical_get_model_instance = AutotestResultHistoricalGetModel.from_json(json)
# print the JSON string representation of the object
print(AutotestResultHistoricalGetModel.to_json())

# convert the object into a dict
autotest_result_historical_get_model_dict = autotest_result_historical_get_model_instance.to_dict()
# create an instance of AutotestResultHistoricalGetModel from a dict
autotest_result_historical_get_model_from_dict = AutotestResultHistoricalGetModel.from_dict(autotest_result_historical_get_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


