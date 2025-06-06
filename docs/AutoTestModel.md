# AutoTestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_id** | **int** | Global ID of the autotest | 
**is_deleted** | **bool** | Indicates if the autotest is deleted | 
**must_be_approved** | **bool** | Indicates if the autotest has unapproved changes from linked work items | 
**id** | **str** | Unique ID of the autotest | 
**created_date** | **datetime** | Creation date of the autotest | 
**modified_date** | **datetime** | Last modification date of the project | [optional] 
**created_by_id** | **str** | Unique ID of the project creator | 
**modified_by_id** | **str** | Unique ID of the project last editor | [optional] 
**last_test_run_id** | **str** | Unique ID of the autotest last test run | [optional] 
**last_test_run_name** | **str** | Name of the autotest last test run | [optional] 
**last_test_result_id** | **str** | Unique ID of the autotest last test result | [optional] 
**last_test_result_configuration** | [**ConfigurationShortModel**](ConfigurationShortModel.md) | Configuration of the autotest last test result | [optional] 
**last_test_result_outcome** | **str** | Outcome of the autotest last test result | [optional] 
**last_test_result_status** | [**TestStatusModel**](TestStatusModel.md) | Status of the autotest last test result | 
**stability_percentage** | **int** | Stability percentage of the autotest | [optional] 
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
**labels** | [**List[LabelShortModel]**](LabelShortModel.md) | Collection of the autotest labels | [optional] 
**is_flaky** | **bool** | Indicates if the autotest is marked as flaky | [optional] 
**external_key** | **str** | External key of the autotest | [optional] 

## Example

```python
from testit_api_client.models.auto_test_model import AutoTestModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestModel from a JSON string
auto_test_model_instance = AutoTestModel.from_json(json)
# print the JSON string representation of the object
print(AutoTestModel.to_json())

# convert the object into a dict
auto_test_model_dict = auto_test_model_instance.to_dict()
# create an instance of AutoTestModel from a dict
auto_test_model_from_dict = AutoTestModel.from_dict(auto_test_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


