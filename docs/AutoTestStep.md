# AutoTestStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Step name. | 
**description** | **str** | Detailed step description. It appears when the step is unfolded. | [optional] 
**steps** | [**List[AutoTestStep]**](AutoTestStep.md) | Includes a nested step inside another step. The maximum nesting level is 15. | [optional] 

## Example

```python
from testit_api_client.models.auto_test_step import AutoTestStep

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestStep from a JSON string
auto_test_step_instance = AutoTestStep.from_json(json)
# print the JSON string representation of the object
print(AutoTestStep.to_json())

# convert the object into a dict
auto_test_step_dict = auto_test_step_instance.to_dict()
# create an instance of AutoTestStep from a dict
auto_test_step_from_dict = AutoTestStep.from_dict(auto_test_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


