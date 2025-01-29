# CreateTestPlanApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[TagPostModel]**](TagPostModel.md) | Test plan tag names collection | [optional] 
**name** | **str** | Test plan name | 
**start_date** | **datetime** | Date and time of test plan start | [optional] 
**end_date** | **datetime** | Date and time of test plan end | [optional] 
**description** | **str** | Test plan description | [optional] 
**build** | **str** | Build of the application on which test plan is executed | [optional] 
**project_id** | **str** | Project unique identifier | 
**product_name** | **str** | Name of the testing product | [optional] 
**has_automatic_duration_timer** | **bool** | Boolean flag defines if test plan has automatic duration timer | [optional] 
**attributes** | **Dict[str, Optional[object]]** | Key value pair of test plan custom attributes | 
**test_suite** | [**TestSuiteTestPlanApiModel**](TestSuiteTestPlanApiModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.create_test_plan_api_model import CreateTestPlanApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTestPlanApiModel from a JSON string
create_test_plan_api_model_instance = CreateTestPlanApiModel.from_json(json)
# print the JSON string representation of the object
print(CreateTestPlanApiModel.to_json())

# convert the object into a dict
create_test_plan_api_model_dict = create_test_plan_api_model_instance.to_dict()
# create an instance of CreateTestPlanApiModel from a dict
create_test_plan_api_model_from_dict = CreateTestPlanApiModel.from_dict(create_test_plan_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


