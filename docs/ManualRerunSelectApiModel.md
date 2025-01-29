# ManualRerunSelectApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TestResultsFilterApiModel**](TestResultsFilterApiModel.md) |  | [optional] 
**extraction_model** | [**TestResultsExtractionApiModel**](TestResultsExtractionApiModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.manual_rerun_select_api_model import ManualRerunSelectApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of ManualRerunSelectApiModel from a JSON string
manual_rerun_select_api_model_instance = ManualRerunSelectApiModel.from_json(json)
# print the JSON string representation of the object
print(ManualRerunSelectApiModel.to_json())

# convert the object into a dict
manual_rerun_select_api_model_dict = manual_rerun_select_api_model_instance.to_dict()
# create an instance of ManualRerunSelectApiModel from a dict
manual_rerun_select_api_model_from_dict = ManualRerunSelectApiModel.from_dict(manual_rerun_select_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


