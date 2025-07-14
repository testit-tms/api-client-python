# AutoTestApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**project_id** | **str** |  | 
**external_id** | **str** |  | [optional] 
**name** | **str** |  | 
**namespace** | **str** |  | [optional] 
**classname** | **str** |  | [optional] 
**steps** | [**List[AutoTestStepApiResult]**](AutoTestStepApiResult.md) |  | [optional] 
**setup** | [**List[AutoTestStepApiResult]**](AutoTestStepApiResult.md) |  | [optional] 
**teardown** | [**List[AutoTestStepApiResult]**](AutoTestStepApiResult.md) |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_flaky** | **bool** |  | 
**external_key** | **str** |  | [optional] 
**global_id** | **int** |  | 
**is_deleted** | **bool** |  | 
**must_be_approved** | **bool** |  | 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**last_test_run_id** | **str** |  | [optional] 
**last_test_run_name** | **str** |  | [optional] 
**last_test_result_id** | **str** |  | [optional] 
**last_test_result_configuration** | [**ConfigurationShortApiResult**](ConfigurationShortApiResult.md) |  | [optional] 
**last_test_result_outcome** | **str** |  | [optional] 
**last_test_result_status** | [**TestStatusApiResult**](TestStatusApiResult.md) |  | [optional] 
**stability_percentage** | **int** |  | [optional] 
**links** | [**List[LinkApiResult]**](LinkApiResult.md) |  | [optional] 
**labels** | [**List[LabelApiResult]**](LabelApiResult.md) |  | [optional] 

## Example

```python
from testit_api_client.models.auto_test_api_result import AutoTestApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestApiResult from a JSON string
auto_test_api_result_instance = AutoTestApiResult.from_json(json)
# print the JSON string representation of the object
print AutoTestApiResult.to_json()

# convert the object into a dict
auto_test_api_result_dict = auto_test_api_result_instance.to_dict()
# create an instance of AutoTestApiResult from a dict
auto_test_api_result_from_dict = AutoTestApiResult.from_dict(auto_test_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


