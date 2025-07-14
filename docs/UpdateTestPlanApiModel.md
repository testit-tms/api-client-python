# UpdateTestPlanApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Test plan unique internal identifier | 
**locked_by_id** | **str** | User who locked test plan modification internal identifier | [optional] 
**name** | **str** | Test plan name | 
**start_date** | **datetime** | Date and time of test plan start | [optional] 
**end_date** | **datetime** | Date and time of test plan end | [optional] 
**description** | **str** | Test plan description | [optional] 
**build** | **str** | Build of the application on which test plan is executed | [optional] 
**project_id** | **str** | Project unique identifier | 
**product_name** | **str** | Name of the testing product | [optional] 
**has_automatic_duration_timer** | **bool** | Boolean flag defines if test plan has automatic duration timer | [optional] 
**attributes** | **Dict[str, object]** | Key value pair of test plan custom attributes | [optional] 
**tags** | [**List[TagApiModel]**](TagApiModel.md) | Test plan tag names collection | [optional] 

## Example

```python
from testit_api_client.models.update_test_plan_api_model import UpdateTestPlanApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTestPlanApiModel from a JSON string
update_test_plan_api_model_instance = UpdateTestPlanApiModel.from_json(json)
# print the JSON string representation of the object
print UpdateTestPlanApiModel.to_json()

# convert the object into a dict
update_test_plan_api_model_dict = update_test_plan_api_model_instance.to_dict()
# create an instance of UpdateTestPlanApiModel from a dict
update_test_plan_api_model_from_dict = UpdateTestPlanApiModel.from_dict(update_test_plan_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


