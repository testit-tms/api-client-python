# AutotestFilterModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **List[str]** | Specifies an autotest projects IDs to search for | [optional] 
**external_ids** | **List[str]** | Specifies an autotest external IDs to search for | [optional] 
**global_ids** | **List[int]** | Specifies an autotest global IDs to search for | [optional] 
**name** | **str** | Specifies an autotest name to search for | [optional] 
**is_flaky** | **bool** | Specifies an autotest flaky status to search for | [optional] 
**must_be_approved** | **bool** | Specifies an autotest unapproved changes status to search for | [optional] 
**stability_percentage** | [**Int64RangeSelectorModel**](Int64RangeSelectorModel.md) | Specifies an autotest range of stability percentage to search for | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies an autotest range of creation date to search for | [optional] 
**created_by_ids** | **List[str]** | Specifies an autotest creator IDs to search for | [optional] 
**modified_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies an autotest range of last modification date to search for | [optional] 
**modified_by_ids** | **List[str]** | Specifies an autotest last editor IDs to search for | [optional] 
**is_deleted** | **bool** | Specifies an autotest deleted status to search for | [optional] 
**namespace** | **str** | Specifies an autotest namespace to search for | [optional] 
**is_empty_namespace** | **bool** | Specifies an autotest namespace name presence status to search for | [optional] 
**class_name** | **str** | Specifies an autotest class name to search for | [optional] 
**is_empty_class_name** | **bool** | Specifies an autotest class name presence status to search for | [optional] 
**last_test_result_outcome** | [**AutotestResultOutcome**](AutotestResultOutcome.md) | Specifies an autotest outcome of the last test result to search for | [optional] 
**external_key** | **str** | Specifies an autotest external key to search for | [optional] 
**last_test_result_configuration_ids** | **List[str]** | Specifies an autotest configuration IDs of the last test result to search for | [optional] 

## Example

```python
from testit_api_client.models.autotest_filter_model import AutotestFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutotestFilterModel from a JSON string
autotest_filter_model_instance = AutotestFilterModel.from_json(json)
# print the JSON string representation of the object
print(AutotestFilterModel.to_json())

# convert the object into a dict
autotest_filter_model_dict = autotest_filter_model_instance.to_dict()
# create an instance of AutotestFilterModel from a dict
autotest_filter_model_from_dict = AutotestFilterModel.from_dict(autotest_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


