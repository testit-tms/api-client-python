# AutoTestFilterModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **List[str]** |  | [optional] 
**external_ids** | **List[str]** |  | [optional] 
**global_ids** | **List[int]** |  | [optional] 
**name** | **str** |  | [optional] 
**is_flaky** | **bool** |  | [optional] 
**must_be_approved** | **bool** |  | [optional] 
**stability_percentage** | [**Int64RangeSelectorModel**](Int64RangeSelectorModel.md) |  | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**created_by_ids** | **List[str]** |  | [optional] 
**modified_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**modified_by_ids** | **List[str]** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**namespace** | **str** |  | [optional] 
**is_empty_namespace** | **bool** |  | [optional] 
**class_name** | **str** |  | [optional] 
**is_empty_class_name** | **bool** |  | [optional] 
**last_test_result_outcome** | [**AutotestResultOutcome**](AutotestResultOutcome.md) |  | [optional] 
**last_test_result_status_code** | **str** |  | [optional] 
**external_key** | **str** |  | [optional] 
**last_test_result_configuration_ids** | **List[str]** |  | [optional] 

## Example

```python
from testit_api_client.models.auto_test_filter_model import AutoTestFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestFilterModel from a JSON string
auto_test_filter_model_instance = AutoTestFilterModel.from_json(json)
# print the JSON string representation of the object
print AutoTestFilterModel.to_json()

# convert the object into a dict
auto_test_filter_model_dict = auto_test_filter_model_instance.to_dict()
# create an instance of AutoTestFilterModel from a dict
auto_test_filter_model_from_dict = AutoTestFilterModel.from_dict(auto_test_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


