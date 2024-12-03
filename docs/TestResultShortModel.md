# TestResultShortModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**outcome** | **str** |  | 
**traces** | **str** |  | [optional] 
**failure_type** | **str** |  | 
**message** | **str** |  | [optional] 
**test_point** | [**TestPointPutModel**](TestPointPutModel.md) |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**auto_test** | [**AutoTestShortModel**](AutoTestShortModel.md) |  | [optional] 
**attachments** | [**List[AttachmentModel]**](AttachmentModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_result_short_model import TestResultShortModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultShortModel from a JSON string
test_result_short_model_instance = TestResultShortModel.from_json(json)
# print the JSON string representation of the object
print(TestResultShortModel.to_json())

# convert the object into a dict
test_result_short_model_dict = test_result_short_model_instance.to_dict()
# create an instance of TestResultShortModel from a dict
test_result_short_model_from_dict = TestResultShortModel.from_dict(test_result_short_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


