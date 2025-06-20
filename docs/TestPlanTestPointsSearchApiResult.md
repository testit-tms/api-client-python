# TestPlanTestPointsSearchApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created** | [**AuditApiResult**](AuditApiResult.md) |  | 
**modified** | [**AuditApiResult**](AuditApiResult.md) |  | [optional] 
**status** | **str** |  | 
**status_model** | [**TestStatusShortApiResult**](TestStatusShortApiResult.md) |  | 
**in_progress** | **bool** |  | 
**configuration** | [**ConfigurationShortApiResult**](ConfigurationShortApiResult.md) |  | 
**tester** | [**UserNameApiResult**](UserNameApiResult.md) |  | [optional] 
**test_suite** | [**TestPlanTestPointsTestSuiteSearchApiResult**](TestPlanTestPointsTestSuiteSearchApiResult.md) |  | 
**work_item** | [**TestPlanTestPointsWorkItemSearchApiResult**](TestPlanTestPointsWorkItemSearchApiResult.md) |  | 
**parameters** | [**List[ParameterShortApiResult]**](ParameterShortApiResult.md) |  | 
**last_test_result** | [**LastTestResultApiResult**](LastTestResultApiResult.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_plan_test_points_search_api_result import TestPlanTestPointsSearchApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanTestPointsSearchApiResult from a JSON string
test_plan_test_points_search_api_result_instance = TestPlanTestPointsSearchApiResult.from_json(json)
# print the JSON string representation of the object
print(TestPlanTestPointsSearchApiResult.to_json())

# convert the object into a dict
test_plan_test_points_search_api_result_dict = test_plan_test_points_search_api_result_instance.to_dict()
# create an instance of TestPlanTestPointsSearchApiResult from a dict
test_plan_test_points_search_api_result_from_dict = TestPlanTestPointsSearchApiResult.from_dict(test_plan_test_points_search_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


