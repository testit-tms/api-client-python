# ManualRerunTestResultApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_result_ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Set of extracted test result IDs | [optional] 

## Example

```python
from testit_api_client.models.manual_rerun_test_result_api_model import ManualRerunTestResultApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of ManualRerunTestResultApiModel from a JSON string
manual_rerun_test_result_api_model_instance = ManualRerunTestResultApiModel.from_json(json)
# print the JSON string representation of the object
print(ManualRerunTestResultApiModel.to_json())

# convert the object into a dict
manual_rerun_test_result_api_model_dict = manual_rerun_test_result_api_model_instance.to_dict()
# create an instance of ManualRerunTestResultApiModel from a dict
manual_rerun_test_result_api_model_from_dict = ManualRerunTestResultApiModel.from_dict(manual_rerun_test_result_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


