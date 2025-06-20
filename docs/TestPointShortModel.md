# TestPointShortModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_suite_id** | **str** |  | 
**id** | **str** | Test point unique internal identifier | 
**tester_id** | **str** | Tester who is responded for the test unique internal identifier | [optional] 
**work_item_id** | **str** | Workitem to which test point relates unique identifier | [optional] 
**configuration_id** | **str** | Configuration to which test point relates unique identifier | [optional] 
**status** | **str** | Test point status  Applies one of these values: Blocked, NoResults, Failed, Passed | [optional] 
**last_test_result_id** | **str** | Last test result unique identifier | [optional] 
**iteration_id** | **str** | Iteration unique identifier | 
**work_item_median_duration** | **int** | Median duration of work item the test point represents | [optional] 

## Example

```python
from testit_api_client.models.test_point_short_model import TestPointShortModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointShortModel from a JSON string
test_point_short_model_instance = TestPointShortModel.from_json(json)
# print the JSON string representation of the object
print(TestPointShortModel.to_json())

# convert the object into a dict
test_point_short_model_dict = test_point_short_model_instance.to_dict()
# create an instance of TestPointShortModel from a dict
test_point_short_model_from_dict = TestPointShortModel.from_dict(test_point_short_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


