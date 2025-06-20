# TestPlanGroupByTesterAndStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**status** | **str** |  | 
**value** | **int** |  | 

## Example

```python
from testit_api_client.models.test_plan_group_by_tester_and_status import TestPlanGroupByTesterAndStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanGroupByTesterAndStatus from a JSON string
test_plan_group_by_tester_and_status_instance = TestPlanGroupByTesterAndStatus.from_json(json)
# print the JSON string representation of the object
print(TestPlanGroupByTesterAndStatus.to_json())

# convert the object into a dict
test_plan_group_by_tester_and_status_dict = test_plan_group_by_tester_and_status_instance.to_dict()
# create an instance of TestPlanGroupByTesterAndStatus from a dict
test_plan_group_by_tester_and_status_from_dict = TestPlanGroupByTesterAndStatus.from_dict(test_plan_group_by_tester_and_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


