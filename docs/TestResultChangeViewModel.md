# TestResultChangeViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_point_count** | **int** |  | 

## Example

```python
from testit_api_client.models.test_result_change_view_model import TestResultChangeViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultChangeViewModel from a JSON string
test_result_change_view_model_instance = TestResultChangeViewModel.from_json(json)
# print the JSON string representation of the object
print TestResultChangeViewModel.to_json()

# convert the object into a dict
test_result_change_view_model_dict = test_result_change_view_model_instance.to_dict()
# create an instance of TestResultChangeViewModel from a dict
test_result_change_view_model_from_dict = TestResultChangeViewModel.from_dict(test_result_change_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


