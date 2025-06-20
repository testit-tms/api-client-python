# ManualRerunApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_results_count** | **int** |  | 

## Example

```python
from testit_api_client.models.manual_rerun_api_result import ManualRerunApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of ManualRerunApiResult from a JSON string
manual_rerun_api_result_instance = ManualRerunApiResult.from_json(json)
# print the JSON string representation of the object
print(ManualRerunApiResult.to_json())

# convert the object into a dict
manual_rerun_api_result_dict = manual_rerun_api_result_instance.to_dict()
# create an instance of ManualRerunApiResult from a dict
manual_rerun_api_result_from_dict = ManualRerunApiResult.from_dict(manual_rerun_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


