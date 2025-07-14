# TestPlanGroupByStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**value** | **int** |  | 

## Example

```python
from testit_api_client.models.test_plan_group_by_status import TestPlanGroupByStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanGroupByStatus from a JSON string
test_plan_group_by_status_instance = TestPlanGroupByStatus.from_json(json)
# print the JSON string representation of the object
print TestPlanGroupByStatus.to_json()

# convert the object into a dict
test_plan_group_by_status_dict = test_plan_group_by_status_instance.to_dict()
# create an instance of TestPlanGroupByStatus from a dict
test_plan_group_by_status_from_dict = TestPlanGroupByStatus.from_dict(test_plan_group_by_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


