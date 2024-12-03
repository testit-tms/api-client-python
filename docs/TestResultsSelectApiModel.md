# TestResultsSelectApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TestResultsFilterRequest**](TestResultsFilterRequest.md) | Test result filters | 
**extraction_model** | [**TestResultsExtractionApiModel**](TestResultsExtractionApiModel.md) | Test results extraction model | 

## Example

```python
from testit_api_client.models.test_results_select_api_model import TestResultsSelectApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsSelectApiModel from a JSON string
test_results_select_api_model_instance = TestResultsSelectApiModel.from_json(json)
# print the JSON string representation of the object
print(TestResultsSelectApiModel.to_json())

# convert the object into a dict
test_results_select_api_model_dict = test_results_select_api_model_instance.to_dict()
# create an instance of TestResultsSelectApiModel from a dict
test_results_select_api_model_from_dict = TestResultsSelectApiModel.from_dict(test_results_select_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


