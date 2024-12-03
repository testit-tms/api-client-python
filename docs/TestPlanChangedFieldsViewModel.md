# TestPlanChangedFieldsViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**StringChangedFieldWithDiffsViewModel**](StringChangedFieldWithDiffsViewModel.md) |  | [optional] 
**description** | [**StringChangedFieldWithDiffsViewModel**](StringChangedFieldWithDiffsViewModel.md) |  | [optional] 
**product_name** | [**StringChangedFieldWithDiffsViewModel**](StringChangedFieldWithDiffsViewModel.md) |  | [optional] 
**build** | [**StringChangedFieldWithDiffsViewModel**](StringChangedFieldWithDiffsViewModel.md) |  | [optional] 
**period** | [**PeriodViewModelChangedFieldViewModel**](PeriodViewModelChangedFieldViewModel.md) |  | [optional] 
**status** | [**StringChangedFieldWithDiffsViewModel**](StringChangedFieldWithDiffsViewModel.md) |  | [optional] 
**tags** | [**StringArrayChangedFieldViewModel**](StringArrayChangedFieldViewModel.md) |  | [optional] 
**test_suite** | [**TestSuiteChangeViewModelChangedFieldViewModel**](TestSuiteChangeViewModelChangedFieldViewModel.md) |  | [optional] 
**test_points** | [**TestPointChangeViewModelChangedFieldViewModel**](TestPointChangeViewModelChangedFieldViewModel.md) |  | [optional] 
**test_results** | [**TestResultChangeViewModelChangedFieldViewModel**](TestResultChangeViewModelChangedFieldViewModel.md) |  | [optional] 
**locking** | [**BooleanChangedFieldViewModel**](BooleanChangedFieldViewModel.md) |  | [optional] 
**has_automatic_duration_timer** | [**BooleanNullableChangedFieldViewModel**](BooleanNullableChangedFieldViewModel.md) |  | [optional] 
**attributes** | [**Dict[str, CustomAttributeChangeModel]**](CustomAttributeChangeModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_plan_changed_fields_view_model import TestPlanChangedFieldsViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanChangedFieldsViewModel from a JSON string
test_plan_changed_fields_view_model_instance = TestPlanChangedFieldsViewModel.from_json(json)
# print the JSON string representation of the object
print(TestPlanChangedFieldsViewModel.to_json())

# convert the object into a dict
test_plan_changed_fields_view_model_dict = test_plan_changed_fields_view_model_instance.to_dict()
# create an instance of TestPlanChangedFieldsViewModel from a dict
test_plan_changed_fields_view_model_from_dict = TestPlanChangedFieldsViewModel.from_dict(test_plan_changed_fields_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


