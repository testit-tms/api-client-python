# ManualRerunSelectModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extraction_model** | [**TestResultExtractionModel**](TestResultExtractionModel.md) |  | [optional] 
**filter** | [**TestResultsFilterModel**](TestResultsFilterModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.manual_rerun_select_model import ManualRerunSelectModel

# TODO update the JSON string below
json = "{}"
# create an instance of ManualRerunSelectModel from a JSON string
manual_rerun_select_model_instance = ManualRerunSelectModel.from_json(json)
# print the JSON string representation of the object
print(ManualRerunSelectModel.to_json())

# convert the object into a dict
manual_rerun_select_model_dict = manual_rerun_select_model_instance.to_dict()
# create an instance of ManualRerunSelectModel from a dict
manual_rerun_select_model_from_dict = ManualRerunSelectModel.from_dict(manual_rerun_select_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


