# TestRunSelectApiModel

Model containing options to filter test runs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TestRunFilterApiModel**](TestRunFilterApiModel.md) |  | 
**extraction_model** | [**TestRunExtractionApiModel**](TestRunExtractionApiModel.md) | Rules for different level entities inclusion/exclusion | 

## Example

```python
from testit_api_client.models.test_run_select_api_model import TestRunSelectApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunSelectApiModel from a JSON string
test_run_select_api_model_instance = TestRunSelectApiModel.from_json(json)
# print the JSON string representation of the object
print(TestRunSelectApiModel.to_json())

# convert the object into a dict
test_run_select_api_model_dict = test_run_select_api_model_instance.to_dict()
# create an instance of TestRunSelectApiModel from a dict
test_run_select_api_model_from_dict = TestRunSelectApiModel.from_dict(test_run_select_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


