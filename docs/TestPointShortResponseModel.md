# TestPointShortResponseModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the test point | 
**created_date** | **datetime** | Creation date of the test point | 
**created_by_id** | **str** | Unique ID of the test point creator | 
**modified_date** | **datetime** | Last modification date of the test point | [optional] 
**modified_by_id** | **str** | Unique ID of the test point last editor | [optional] 
**tester_id** | **str** | Unique ID of the test point assigned user | [optional] 
**parameters** | **Dict[str, str]** | Collection of the test point parameters | [optional] 
**attributes** | **Dict[str, object]** | Collection of attributes of work item the test point represents | 
**tags** | **List[str]** | Collection of the test point tags | 
**links** | **List[str]** | Collection of the test point links | 
**test_suite_id** | **str** | Unique ID of test suite the test point assigned to | 
**test_suite_name** | **str** | Name of the test suite | 
**work_item_id** | **str** | Unique ID of work item the test point represents | 
**work_item_global_id** | **int** | Global ID of work item the test point represents | 
**work_item_version_id** | **str** | Unique ID of work item version the test point represents | 
**work_item_version_number** | **int** | Number of work item version the test point represents | 
**work_item_median_duration** | **int** | Median duration of work item the test point represents | [optional] 
**status** | [**TestPointStatus**](TestPointStatus.md) | Status of the test point | 
**status_model** | [**TestStatusApiResult**](TestStatusApiResult.md) | Status of the test point | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) | Priority of the test point | 
**source_type** | [**WorkItemSourceTypeModel**](WorkItemSourceTypeModel.md) | Source type of the test point | 
**is_automated** | **bool** | Indicates if the test point represents an autotest | 
**name** | **str** | Name of the test point | 
**configuration_id** | **str** | Unique ID of the test point configuration | 
**duration** | **int** | Duration of the test point | 
**section_id** | **str** | Unique ID of section where work item the test point represents is located | 
**section_name** | **str** | Name of section where work item the test point represents is located | [optional] 
**project_id** | **str** | Unique ID of the test point project | 
**last_test_result** | [**LastTestResultModel**](LastTestResultModel.md) | Model of the test point last test result | [optional] 
**iteration_id** | **str** | Unique ID of work item iteration the test point represents | 
**work_item_state** | [**WorkItemState**](WorkItemState.md) | Work item state | 
**work_item_created_by_id** | **str** | Unique ID of the work item creator | 
**work_item_created_date** | **datetime** | Creation date of work item | 
**work_item_modified_by_id** | **str** | Unique ID of the work item last editor | [optional] 
**work_item_modified_date** | **datetime** | Modified date of work item | [optional] 

## Example

```python
from testit_api_client.models.test_point_short_response_model import TestPointShortResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointShortResponseModel from a JSON string
test_point_short_response_model_instance = TestPointShortResponseModel.from_json(json)
# print the JSON string representation of the object
print TestPointShortResponseModel.to_json()

# convert the object into a dict
test_point_short_response_model_dict = test_point_short_response_model_instance.to_dict()
# create an instance of TestPointShortResponseModel from a dict
test_point_short_response_model_from_dict = TestPointShortResponseModel.from_dict(test_point_short_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


