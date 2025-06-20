# TestSuiteTestPlanApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Test suite nane | 
**configuration_ids** | **List[str]** | Configuration identifiers. Empty configurations means using default configurations | [optional] 
**type** | [**TestSuiteType**](TestSuiteType.md) | Type of the test suite | [optional] 
**save_structure** | **bool** | Indicates if the test suite retains section tree structure | [optional] 
**work_items_selector** | [**WorkItemSelectModel**](WorkItemSelectModel.md) | Model containing options to filter work items | 

## Example

```python
from testit_api_client.models.test_suite_test_plan_api_model import TestSuiteTestPlanApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestSuiteTestPlanApiModel from a JSON string
test_suite_test_plan_api_model_instance = TestSuiteTestPlanApiModel.from_json(json)
# print the JSON string representation of the object
print(TestSuiteTestPlanApiModel.to_json())

# convert the object into a dict
test_suite_test_plan_api_model_dict = test_suite_test_plan_api_model_instance.to_dict()
# create an instance of TestSuiteTestPlanApiModel from a dict
test_suite_test_plan_api_model_from_dict = TestSuiteTestPlanApiModel.from_dict(test_suite_test_plan_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


