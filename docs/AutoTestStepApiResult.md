# AutoTestStepApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Step name. | 
**description** | **str** | Detailed step description. It appears when the step is unfolded. | [optional] 
**steps** | [**List[AutoTestStepApiResult]**](AutoTestStepApiResult.md) | Includes a nested step inside another step. The maximum nesting level is 15. | [optional] 

## Example

```python
from testit_api_client.models.auto_test_step_api_result import AutoTestStepApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestStepApiResult from a JSON string
auto_test_step_api_result_instance = AutoTestStepApiResult.from_json(json)
# print the JSON string representation of the object
print(AutoTestStepApiResult.to_json())

# convert the object into a dict
auto_test_step_api_result_dict = auto_test_step_api_result_instance.to_dict()
# create an instance of AutoTestStepApiResult from a dict
auto_test_step_api_result_from_dict = AutoTestStepApiResult.from_dict(auto_test_step_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


