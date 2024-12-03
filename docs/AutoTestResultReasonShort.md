# AutoTestResultReasonShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_category** | [**FailureCategoryModel**](FailureCategoryModel.md) |  | 
**name** | **str** |  | 

## Example

```python
from testit_api_client.models.auto_test_result_reason_short import AutoTestResultReasonShort

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestResultReasonShort from a JSON string
auto_test_result_reason_short_instance = AutoTestResultReasonShort.from_json(json)
# print the JSON string representation of the object
print(AutoTestResultReasonShort.to_json())

# convert the object into a dict
auto_test_result_reason_short_dict = auto_test_result_reason_short_instance.to_dict()
# create an instance of AutoTestResultReasonShort from a dict
auto_test_result_reason_short_from_dict = AutoTestResultReasonShort.from_dict(auto_test_result_reason_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


