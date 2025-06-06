# TestPlanGroupByStatusCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **str** |  | 
**value** | **int** |  | 

## Example

```python
from testit_api_client.models.test_plan_group_by_status_code import TestPlanGroupByStatusCode

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanGroupByStatusCode from a JSON string
test_plan_group_by_status_code_instance = TestPlanGroupByStatusCode.from_json(json)
# print the JSON string representation of the object
print(TestPlanGroupByStatusCode.to_json())

# convert the object into a dict
test_plan_group_by_status_code_dict = test_plan_group_by_status_code_instance.to_dict()
# create an instance of TestPlanGroupByStatusCode from a dict
test_plan_group_by_status_code_from_dict = TestPlanGroupByStatusCode.from_dict(test_plan_group_by_status_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


