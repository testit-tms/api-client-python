# TestPointsExtractionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Extraction parameters for test points | [optional] 

## Example

```python
from testit_api_client.models.test_points_extraction_model import TestPointsExtractionModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointsExtractionModel from a JSON string
test_points_extraction_model_instance = TestPointsExtractionModel.from_json(json)
# print the JSON string representation of the object
print(TestPointsExtractionModel.to_json())

# convert the object into a dict
test_points_extraction_model_dict = test_points_extraction_model_instance.to_dict()
# create an instance of TestPointsExtractionModel from a dict
test_points_extraction_model_from_dict = TestPointsExtractionModel.from_dict(test_points_extraction_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


