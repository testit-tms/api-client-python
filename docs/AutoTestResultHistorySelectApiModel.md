# AutoTestResultHistorySelectApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcomes** | [**List[AutotestResultOutcome]**](AutotestResultOutcome.md) |  | [optional] 
**status_codes** | **List[str]** |  | [optional] 
**test_plan_ids** | **List[str]** |  | [optional] 
**test_run_ids** | **List[str]** |  | [optional] 
**configuration_ids** | **List[str]** |  | [optional] 
**launch_source** | **str** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 
**duration** | [**Int64RangeSelectorModel**](Int64RangeSelectorModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.auto_test_result_history_select_api_model import AutoTestResultHistorySelectApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestResultHistorySelectApiModel from a JSON string
auto_test_result_history_select_api_model_instance = AutoTestResultHistorySelectApiModel.from_json(json)
# print the JSON string representation of the object
print AutoTestResultHistorySelectApiModel.to_json()

# convert the object into a dict
auto_test_result_history_select_api_model_dict = auto_test_result_history_select_api_model_instance.to_dict()
# create an instance of AutoTestResultHistorySelectApiModel from a dict
auto_test_result_history_select_api_model_from_dict = AutoTestResultHistorySelectApiModel.from_dict(auto_test_result_history_select_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


