# TestResultV2GetModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**ConfigurationModel**](ConfigurationModel.md) |  | [optional] 
**auto_test** | [**AutoTestModelV2GetModel**](AutoTestModelV2GetModel.md) |  | [optional] 
**id** | **str** |  | 
**configuration_id** | **str** |  | 
**work_item_version_id** | **str** |  | 
**auto_test_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**traces** | **str** |  | [optional] 
**started_on** | **datetime** |  | [optional] 
**completed_on** | **datetime** |  | [optional] 
**run_by_user_id** | **str** |  | [optional] 
**stopped_by_user_id** | **str** |  | [optional] 
**test_point_id** | **str** |  | [optional] 
**test_point** | [**TestPointShortModel**](TestPointShortModel.md) |  | [optional] 
**test_run_id** | **str** |  | 
**outcome** | **str** | Property can contain one of these values: Passed, Failed, InProgress, Blocked, Skipped | 
**comment** | **str** |  | [optional] 
**links** | [**List[LinkModel]**](LinkModel.md) |  | [optional] 
**attachments** | [**List[AttachmentModel]**](AttachmentModel.md) |  | [optional] 
**parameters** | **Dict[str, str]** |  | [optional] 
**properties** | **Dict[str, str]** |  | [optional] 

## Example

```python
from testit_api_client.models.test_result_v2_get_model import TestResultV2GetModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultV2GetModel from a JSON string
test_result_v2_get_model_instance = TestResultV2GetModel.from_json(json)
# print the JSON string representation of the object
print(TestResultV2GetModel.to_json())

# convert the object into a dict
test_result_v2_get_model_dict = test_result_v2_get_model_instance.to_dict()
# create an instance of TestResultV2GetModel from a dict
test_result_v2_get_model_from_dict = TestResultV2GetModel.from_dict(test_result_v2_get_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


