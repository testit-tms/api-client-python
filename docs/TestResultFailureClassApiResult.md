# TestResultFailureClassApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_category** | [**FailureCategory**](FailureCategory.md) |  | 

## Example

```python
from testit_api_client.models.test_result_failure_class_api_result import TestResultFailureClassApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultFailureClassApiResult from a JSON string
test_result_failure_class_api_result_instance = TestResultFailureClassApiResult.from_json(json)
# print the JSON string representation of the object
print(TestResultFailureClassApiResult.to_json())

# convert the object into a dict
test_result_failure_class_api_result_dict = test_result_failure_class_api_result_instance.to_dict()
# create an instance of TestResultFailureClassApiResult from a dict
test_result_failure_class_api_result_from_dict = TestResultFailureClassApiResult.from_dict(test_result_failure_class_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


