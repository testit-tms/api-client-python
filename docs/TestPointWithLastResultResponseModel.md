# TestPointWithLastResultResponseModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**work_item_name** | **str** |  | [optional] 
**is_automated** | **bool** |  | 
**tester_id** | **str** |  | [optional] 
**work_item_id** | **str** |  | 
**configuration_id** | **str** |  | [optional] 
**test_suite_id** | **str** |  | 
**last_test_result** | [**LastTestResultModel**](LastTestResultModel.md) |  | [optional] 
**status** | **str** |  | [optional] 
**status_model** | [**TestStatusApiResult**](TestStatusApiResult.md) |  | [optional] 
**work_item_global_id** | **int** |  | [optional] 
**work_item_entity_type_name** | **str** |  | [optional] 
**section_id** | **str** |  | 
**section_name** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 
**tag_names** | **List[str]** |  | [optional] 
**duration** | **int** |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**test_suite_name_bread_crumbs** | **List[str]** |  | [optional] 
**group_count** | **int** |  | [optional] 
**iteration** | [**IterationModel**](IterationModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_point_with_last_result_response_model import TestPointWithLastResultResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointWithLastResultResponseModel from a JSON string
test_point_with_last_result_response_model_instance = TestPointWithLastResultResponseModel.from_json(json)
# print the JSON string representation of the object
print TestPointWithLastResultResponseModel.to_json()

# convert the object into a dict
test_point_with_last_result_response_model_dict = test_point_with_last_result_response_model_instance.to_dict()
# create an instance of TestPointWithLastResultResponseModel from a dict
test_point_with_last_result_response_model_from_dict = TestPointWithLastResultResponseModel.from_dict(test_point_with_last_result_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


