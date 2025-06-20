# TestResultsLocalFilterModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_ids** | **List[str]** | Specifies a test result configuration IDs to search for | [optional] 
**outcomes** | [**List[TestResultOutcome]**](TestResultOutcome.md) | Specifies a test result outcomes to search for | [optional] 
**status_codes** | **List[str]** | Specifies a test result status codes to search for | [optional] 
**failure_categories** | [**List[FailureCategoryModel]**](FailureCategoryModel.md) | Specifies a test result failure categories to search for | [optional] 
**namespace** | **str** | Specifies a test result namespace to search for | [optional] 
**class_name** | **str** | Specifies a test result class name to search for | [optional] 

## Example

```python
from testit_api_client.models.test_results_local_filter_model import TestResultsLocalFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsLocalFilterModel from a JSON string
test_results_local_filter_model_instance = TestResultsLocalFilterModel.from_json(json)
# print the JSON string representation of the object
print(TestResultsLocalFilterModel.to_json())

# convert the object into a dict
test_results_local_filter_model_dict = test_results_local_filter_model_instance.to_dict()
# create an instance of TestResultsLocalFilterModel from a dict
test_results_local_filter_model_from_dict = TestResultsLocalFilterModel.from_dict(test_results_local_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


