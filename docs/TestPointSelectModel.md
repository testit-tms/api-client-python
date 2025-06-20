# TestPointSelectModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TestPointFilterModel**](TestPointFilterModel.md) |  | [optional] 
**extraction_model** | [**TestPointsExtractionModel**](TestPointsExtractionModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_point_select_model import TestPointSelectModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointSelectModel from a JSON string
test_point_select_model_instance = TestPointSelectModel.from_json(json)
# print the JSON string representation of the object
print(TestPointSelectModel.to_json())

# convert the object into a dict
test_point_select_model_dict = test_point_select_model_instance.to_dict()
# create an instance of TestPointSelectModel from a dict
test_point_select_model_from_dict = TestPointSelectModel.from_dict(test_point_select_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


