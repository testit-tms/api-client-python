# TestPointChangeViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**user_name** | **str** |  | [optional] 
**test_point_count** | **int** |  | 

## Example

```python
from testit_api_client.models.test_point_change_view_model import TestPointChangeViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointChangeViewModel from a JSON string
test_point_change_view_model_instance = TestPointChangeViewModel.from_json(json)
# print the JSON string representation of the object
print TestPointChangeViewModel.to_json()

# convert the object into a dict
test_point_change_view_model_dict = test_point_change_view_model_instance.to_dict()
# create an instance of TestPointChangeViewModel from a dict
test_point_change_view_model_from_dict = TestPointChangeViewModel.from_dict(test_point_change_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


