# AutoTestPostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_item_ids_for_link_with_auto_test** | **List[str]** | Specifies the IDs of work items to link your autotest to. You can specify several IDs. | [optional] 
**should_create_work_item** | **bool** | Creates a test case linked to the autotest. | [optional] 
**attributes** | **Dict[str, object]** | Key value pair of custom work item attributes | [optional] 
**external_id** | **str** | External ID of the autotest | 
**links** | [**List[LinkPostModel]**](LinkPostModel.md) | Collection of the autotest links | [optional] 
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
from testit_api_client.models.auto_test_post_model import AutoTestPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestPostModel from a JSON string
auto_test_post_model_instance = AutoTestPostModel.from_json(json)
# print the JSON string representation of the object
print(AutoTestPostModel.to_json())

# convert the object into a dict
auto_test_post_model_dict = auto_test_post_model_instance.to_dict()
# create an instance of AutoTestPostModel from a dict
auto_test_post_model_from_dict = AutoTestPostModel.from_dict(auto_test_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


