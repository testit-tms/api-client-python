# TestPointResultApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_point_id** | **str** |  | [optional] 
**aggregated_outcome** | **str** |  | [optional] 
**aggregated_status** | [**TestStatusApiResult**](TestStatusApiResult.md) |  | [optional] 
**work_item_global_id** | **int** |  | [optional] 
**work_item_name** | **str** |  | [optional] 
**configuration_name** | **str** |  | [optional] 
**test_results** | [**List[TestResultShortApiResult]**](TestResultShortApiResult.md) |  | 

## Example

```python
from testit_api_client.models.test_point_result_api_result import TestPointResultApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointResultApiResult from a JSON string
test_point_result_api_result_instance = TestPointResultApiResult.from_json(json)
# print the JSON string representation of the object
print TestPointResultApiResult.to_json()

# convert the object into a dict
test_point_result_api_result_dict = test_point_result_api_result_instance.to_dict()
# create an instance of TestPointResultApiResult from a dict
test_point_result_api_result_from_dict = TestPointResultApiResult.from_dict(test_point_result_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


