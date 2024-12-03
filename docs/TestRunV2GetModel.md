# TestRunV2GetModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started_on** | **datetime** |  | [optional] 
**completed_on** | **datetime** |  | [optional] 
**state_name** | [**TestRunState**](TestRunState.md) |  | 
**project_id** | **str** | This property is used to link test run with project | 
**test_plan_id** | **str** | This property is used to link test run with test plan | [optional] 
**test_results** | [**List[TestResultV2GetModel]**](TestResultV2GetModel.md) |  | [optional] 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**created_by_user_name** | **str** |  | [optional] 
**attachments** | [**List[AttachmentModel]**](AttachmentModel.md) |  | 
**links** | [**List[LinkModel]**](LinkModel.md) |  | 
**custom_parameters** | **Dict[str, str]** |  | [optional] 
**webhooks** | [**List[NamedEntityModel]**](NamedEntityModel.md) |  | 
**run_count** | **int** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**launch_source** | **str** | Once launch source is specified it cannot be updated | [optional] 

## Example

```python
from testit_api_client.models.test_run_v2_get_model import TestRunV2GetModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunV2GetModel from a JSON string
test_run_v2_get_model_instance = TestRunV2GetModel.from_json(json)
# print the JSON string representation of the object
print(TestRunV2GetModel.to_json())

# convert the object into a dict
test_run_v2_get_model_dict = test_run_v2_get_model_instance.to_dict()
# create an instance of TestRunV2GetModel from a dict
test_run_v2_get_model_from_dict = TestRunV2GetModel.from_dict(test_run_v2_get_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


