# AutoTestPutModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Used for search autotest. If value is null or equals Guid mask filled with zeros, search will be executed using ExternalId | [optional] 
**work_item_ids_for_link_with_auto_test** | **List[str]** |  | [optional] 
**external_id** | **str** | External ID of the autotest | 
**links** | [**List[LinkPutModel]**](LinkPutModel.md) | Collection of the autotest links | [optional] 
**project_id** | **str** | Unique ID of the autotest project | 
**name** | **str** | Name of the autotest | 
**namespace** | **str** | Name of the autotest namespace | [optional] 
**classname** | **str** | Name of the autotest class | [optional] 
**steps** | [**List[AutoTestStepModel]**](AutoTestStepModel.md) | Collection of the autotest steps | [optional] 
**setup** | [**List[AutoTestStepModel]**](AutoTestStepModel.md) | Collection of the autotest setup steps | [optional] 
**teardown** | [**List[AutoTestStepModel]**](AutoTestStepModel.md) | Collection of the autotest teardown steps | [optional] 
**title** | **str** | Name of the autotest in autotest&#39;s card | [optional] 
**description** | **str** | Description of the autotest in autotest&#39;s card | [optional] 
**labels** | [**List[LabelPostModel]**](LabelPostModel.md) | Collection of the autotest labels | [optional] 
**is_flaky** | **bool** | Indicates if the autotest is marked as flaky | [optional] 
**external_key** | **str** | External key of the autotest | [optional] 

## Example

```python
from testit_api_client.models.auto_test_put_model import AutoTestPutModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestPutModel from a JSON string
auto_test_put_model_instance = AutoTestPutModel.from_json(json)
# print the JSON string representation of the object
print AutoTestPutModel.to_json()

# convert the object into a dict
auto_test_put_model_dict = auto_test_put_model_instance.to_dict()
# create an instance of AutoTestPutModel from a dict
auto_test_put_model_from_dict = AutoTestPutModel.from_dict(auto_test_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


