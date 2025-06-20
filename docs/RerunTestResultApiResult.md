# RerunTestResultApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**outcome** | **str** |  | 
**status** | [**TestStatusApiResult**](TestStatusApiResult.md) |  | 
**run_number** | **int** |  | 

## Example

```python
from testit_api_client.models.rerun_test_result_api_result import RerunTestResultApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of RerunTestResultApiResult from a JSON string
rerun_test_result_api_result_instance = RerunTestResultApiResult.from_json(json)
# print the JSON string representation of the object
print RerunTestResultApiResult.to_json()

# convert the object into a dict
rerun_test_result_api_result_dict = rerun_test_result_api_result_instance.to_dict()
# create an instance of RerunTestResultApiResult from a dict
rerun_test_result_api_result_from_dict = RerunTestResultApiResult.from_dict(rerun_test_result_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


