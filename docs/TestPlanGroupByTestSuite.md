# TestPlanGroupByTestSuite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_suite_id** | **str** |  | 
**test_suite_name** | **str** |  | 
**value** | **int** |  | 

## Example

```python
from testit_api_client.models.test_plan_group_by_test_suite import TestPlanGroupByTestSuite

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanGroupByTestSuite from a JSON string
test_plan_group_by_test_suite_instance = TestPlanGroupByTestSuite.from_json(json)
# print the JSON string representation of the object
print(TestPlanGroupByTestSuite.to_json())

# convert the object into a dict
test_plan_group_by_test_suite_dict = test_plan_group_by_test_suite_instance.to_dict()
# create an instance of TestPlanGroupByTestSuite from a dict
test_plan_group_by_test_suite_from_dict = TestPlanGroupByTestSuite.from_dict(test_plan_group_by_test_suite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


