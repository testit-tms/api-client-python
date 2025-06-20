# AutoTestModelV2GetModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | This property is used to set autotest identifier from client system | 
**links** | [**List[LinkModel]**](LinkModel.md) |  | [optional] 
**project_id** | **str** | This property is used to link autotest with project | 
**name** | **str** |  | 
**namespace** | **str** |  | [optional] 
**classname** | **str** |  | [optional] 
**steps** | [**List[AutoTestStepModel]**](AutoTestStepModel.md) |  | [optional] 
**setup** | [**List[AutoTestStepModel]**](AutoTestStepModel.md) |  | [optional] 
**teardown** | [**List[AutoTestStepModel]**](AutoTestStepModel.md) |  | [optional] 
**global_id** | **int** |  | 
**created_date** | **datetime** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**labels** | [**List[LabelShortModel]**](LabelShortModel.md) |  | [optional] 
**external_key** | **str** |  | [optional] 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 

## Example

```python
from testit_api_client.models.auto_test_model_v2_get_model import AutoTestModelV2GetModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestModelV2GetModel from a JSON string
auto_test_model_v2_get_model_instance = AutoTestModelV2GetModel.from_json(json)
# print the JSON string representation of the object
print(AutoTestModelV2GetModel.to_json())

# convert the object into a dict
auto_test_model_v2_get_model_dict = auto_test_model_v2_get_model_instance.to_dict()
# create an instance of AutoTestModelV2GetModel from a dict
auto_test_model_v2_get_model_from_dict = AutoTestModelV2GetModel.from_dict(auto_test_model_v2_get_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


