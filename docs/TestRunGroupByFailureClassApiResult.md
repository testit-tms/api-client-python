# TestRunGroupByFailureClassApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_category** | **str** |  | 
**value** | **int** |  | 

## Example

```python
from testit_api_client.models.test_run_group_by_failure_class_api_result import TestRunGroupByFailureClassApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunGroupByFailureClassApiResult from a JSON string
test_run_group_by_failure_class_api_result_instance = TestRunGroupByFailureClassApiResult.from_json(json)
# print the JSON string representation of the object
print TestRunGroupByFailureClassApiResult.to_json()

# convert the object into a dict
test_run_group_by_failure_class_api_result_dict = test_run_group_by_failure_class_api_result_instance.to_dict()
# create an instance of TestRunGroupByFailureClassApiResult from a dict
test_run_group_by_failure_class_api_result_from_dict = TestRunGroupByFailureClassApiResult.from_dict(test_run_group_by_failure_class_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


