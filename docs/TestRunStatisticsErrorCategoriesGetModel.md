# TestRunStatisticsErrorCategoriesGetModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infrastructure_defect** | **int** | Number of test results which outcomes were caused by some infrastructure defect | 
**product_defect** | **int** | Number of test results which outcomes were caused by some tested product defect | 
**test_defect** | **int** | Number of test results which outcomes were caused by test itself | 

## Example

```python
from testit_api_client.models.test_run_statistics_error_categories_get_model import TestRunStatisticsErrorCategoriesGetModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunStatisticsErrorCategoriesGetModel from a JSON string
test_run_statistics_error_categories_get_model_instance = TestRunStatisticsErrorCategoriesGetModel.from_json(json)
# print the JSON string representation of the object
print(TestRunStatisticsErrorCategoriesGetModel.to_json())

# convert the object into a dict
test_run_statistics_error_categories_get_model_dict = test_run_statistics_error_categories_get_model_instance.to_dict()
# create an instance of TestRunStatisticsErrorCategoriesGetModel from a dict
test_run_statistics_error_categories_get_model_from_dict = TestRunStatisticsErrorCategoriesGetModel.from_dict(test_run_statistics_error_categories_get_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


