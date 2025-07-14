# TestPointShortApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Test point unique internal identifier | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 
**tester_id** | **str** | Tester who is responded for the test unique internal identifier | [optional] 
**work_item_id** | **str** | Workitem to which test point relates unique identifier | [optional] 
**configuration_id** | **str** | Configuration to which test point relates unique identifier | [optional] 
**status** | **str** | Test point status   Applies one of these values: Blocked, NoResults, Failed, Passed | [optional] 
**status_model** | [**TestStatusApiResult**](TestStatusApiResult.md) | Test point status | 
**last_test_result_id** | **str** | Last test result unique identifier | [optional] 
**iteration_id** | **str** | Iteration unique identifier | 
**work_item_median_duration** | **int** | Median duration of work item the test point represents | [optional] 
**test_suite_id** | **str** | Test suite to which test point relates unique identifier | 

## Example

```python
from testit_api_client.models.test_point_short_api_result import TestPointShortApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointShortApiResult from a JSON string
test_point_short_api_result_instance = TestPointShortApiResult.from_json(json)
# print the JSON string representation of the object
print TestPointShortApiResult.to_json()

# convert the object into a dict
test_point_short_api_result_dict = test_point_short_api_result_instance.to_dict()
# create an instance of TestPointShortApiResult from a dict
test_point_short_api_result_from_dict = TestPointShortApiResult.from_dict(test_point_short_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


