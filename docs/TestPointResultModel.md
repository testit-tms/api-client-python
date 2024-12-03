# TestPointResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_point_id** | **str** |  | [optional] 
**aggregated_outcome** | **str** |  | [optional] 
**work_item_global_id** | **int** |  | [optional] 
**work_item_name** | **str** |  | [optional] 
**configuration_name** | **str** |  | [optional] 
**test_results** | [**List[TestResultShortModel]**](TestResultShortModel.md) |  | [optional] 
**attachments** | [**List[AttachmentModel]**](AttachmentModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_point_result_model import TestPointResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointResultModel from a JSON string
test_point_result_model_instance = TestPointResultModel.from_json(json)
# print the JSON string representation of the object
print(TestPointResultModel.to_json())

# convert the object into a dict
test_point_result_model_dict = test_point_result_model_instance.to_dict()
# create an instance of TestPointResultModel from a dict
test_point_result_model_from_dict = TestPointResultModel.from_dict(test_point_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


