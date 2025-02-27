# AutoTestShortApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**project_id** | **str** |  | 
**name** | **str** |  | 
**external_id** | **str** |  | 
**global_id** | **int** |  | 

## Example

```python
from testit_api_client.models.auto_test_short_api_result import AutoTestShortApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestShortApiResult from a JSON string
auto_test_short_api_result_instance = AutoTestShortApiResult.from_json(json)
# print the JSON string representation of the object
print(AutoTestShortApiResult.to_json())

# convert the object into a dict
auto_test_short_api_result_dict = auto_test_short_api_result_instance.to_dict()
# create an instance of AutoTestShortApiResult from a dict
auto_test_short_api_result_from_dict = AutoTestShortApiResult.from_dict(auto_test_short_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


