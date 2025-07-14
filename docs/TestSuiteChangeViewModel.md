# TestSuiteChangeViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**configurations** | [**List[ShortConfiguration]**](ShortConfiguration.md) |  | [optional] 
**work_item_count** | **int** |  | 

## Example

```python
from testit_api_client.models.test_suite_change_view_model import TestSuiteChangeViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestSuiteChangeViewModel from a JSON string
test_suite_change_view_model_instance = TestSuiteChangeViewModel.from_json(json)
# print the JSON string representation of the object
print TestSuiteChangeViewModel.to_json()

# convert the object into a dict
test_suite_change_view_model_dict = test_suite_change_view_model_instance.to_dict()
# create an instance of TestSuiteChangeViewModel from a dict
test_suite_change_view_model_from_dict = TestSuiteChangeViewModel.from_dict(test_suite_change_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


