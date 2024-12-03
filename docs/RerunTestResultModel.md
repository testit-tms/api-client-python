# RerunTestResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**outcome** | **str** |  | [optional] 
**run_number** | **int** |  | 

## Example

```python
from testit_api_client.models.rerun_test_result_model import RerunTestResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of RerunTestResultModel from a JSON string
rerun_test_result_model_instance = RerunTestResultModel.from_json(json)
# print the JSON string representation of the object
print(RerunTestResultModel.to_json())

# convert the object into a dict
rerun_test_result_model_dict = rerun_test_result_model_instance.to_dict()
# create an instance of RerunTestResultModel from a dict
rerun_test_result_model_from_dict = RerunTestResultModel.from_dict(rerun_test_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


