# AutotestHistoricalResultSelectModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcomes** | [**List[AutotestResultOutcome]**](AutotestResultOutcome.md) |  | [optional] 
**test_plan_ids** | **List[str]** |  | [optional] 
**test_run_ids** | **List[str]** |  | [optional] 
**configuration_ids** | **List[str]** |  | [optional] 
**launch_source** | **str** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 
**duration** | [**Int64RangeSelectorModel**](Int64RangeSelectorModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.autotest_historical_result_select_model import AutotestHistoricalResultSelectModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutotestHistoricalResultSelectModel from a JSON string
autotest_historical_result_select_model_instance = AutotestHistoricalResultSelectModel.from_json(json)
# print the JSON string representation of the object
print(AutotestHistoricalResultSelectModel.to_json())

# convert the object into a dict
autotest_historical_result_select_model_dict = autotest_historical_result_select_model_instance.to_dict()
# create an instance of AutotestHistoricalResultSelectModel from a dict
autotest_historical_result_select_model_from_dict = AutotestHistoricalResultSelectModel.from_dict(autotest_historical_result_select_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


