# TestRunGroupByFailureClassModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_category** | **str** |  | 
**value** | **int** |  | 

## Example

```python
from testit_api_client.models.test_run_group_by_failure_class_model import TestRunGroupByFailureClassModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunGroupByFailureClassModel from a JSON string
test_run_group_by_failure_class_model_instance = TestRunGroupByFailureClassModel.from_json(json)
# print the JSON string representation of the object
print(TestRunGroupByFailureClassModel.to_json())

# convert the object into a dict
test_run_group_by_failure_class_model_dict = test_run_group_by_failure_class_model_instance.to_dict()
# create an instance of TestRunGroupByFailureClassModel from a dict
test_run_group_by_failure_class_model_from_dict = TestRunGroupByFailureClassModel.from_dict(test_run_group_by_failure_class_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


