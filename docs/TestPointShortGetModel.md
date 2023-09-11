# TestPointShortGetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the test point | 
**created_date** | **datetime** | Creation date of the test point | 
**created_by_id** | **str** | Unique ID of the test point creator | 
**test_suite_id** | **str** | Unique ID of test suite the test point assigned to | 
**work_item_id** | **str** | Unique ID of work item the test point represents | 
**work_item_global_id** | **int** | Global ID of work item the test point represents | 
**work_item_version_id** | **str** | Unique ID of work item version the test point represents | 
**status** | [**TestPointStatus**](TestPointStatus.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**is_automated** | **bool** | Indicates if the test point represents an autotest | 
**configuration_id** | **str** | Unique ID of the test point configuration | 
**duration** | **int** | Duration of the test point | 
**section_id** | **str** | Unique ID of section where work item the test point represents is located | 
**project_id** | **str** | Unique ID of the test point project | 
**last_test_result** | [**TestPointShortGetModelLastTestResult**](TestPointShortGetModelLastTestResult.md) |  | 
**iteration_id** | **str** | Unique ID of work item iteration the test point represents | 
**work_item_state** | [**WorkItemState**](WorkItemState.md) |  | 
**work_item_created_by_id** | **str** | Unique ID of the work item creator | 
**work_item_created_date** | **datetime** | Creation date of work item | 
**modified_date** | **datetime, none_type** | Last modification date of the test point | [optional] 
**modified_by_id** | **str, none_type** | Unique ID of the test point last editor | [optional] 
**tester_id** | **str, none_type** | Unique ID of the test point assigned user | [optional] 
**parameters** | **{str: (str, none_type)}, none_type** | Collection of the test point parameters | [optional] 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Collection of attributes of work item the test point represents | [optional] 
**tags** | **[str], none_type** | Collection of the test point tags | [optional] 
**links** | **[str], none_type** | Collection of the test point links | [optional] 
**work_item_median_duration** | **int, none_type** | Median duration of work item the test point represents | [optional] 
**name** | **str, none_type** | Name of the test point | [optional] 
**section_name** | **str, none_type** | Name of section where work item the test point represents is located | [optional] 
**work_item_modified_by_id** | **str, none_type** | Unique ID of the work item last editor | [optional] 
**work_item_modified_date** | **datetime, none_type** | Modified date of work item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


