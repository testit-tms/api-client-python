# TestRunByAutoTestApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 
**state_name** | [**TestRunState**](TestRunState.md) | Test run state | 
**status** | [**TestStatusApiResult**](TestStatusApiResult.md) | Test run status | 
**project_id** | **str** | Project internal identifier | 
**test_plan_id** | **str** | Test plan internal identifier | [optional] 
**name** | **str** | Test run name | [optional] 
**description** | **str** | Test run description | [optional] 

## Example

```python
from testit_api_client.models.test_run_by_auto_test_api_result import TestRunByAutoTestApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunByAutoTestApiResult from a JSON string
test_run_by_auto_test_api_result_instance = TestRunByAutoTestApiResult.from_json(json)
# print the JSON string representation of the object
print(TestRunByAutoTestApiResult.to_json())

# convert the object into a dict
test_run_by_auto_test_api_result_dict = test_run_by_auto_test_api_result_instance.to_dict()
# create an instance of TestRunByAutoTestApiResult from a dict
test_run_by_auto_test_api_result_from_dict = TestRunByAutoTestApiResult.from_dict(test_run_by_auto_test_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


