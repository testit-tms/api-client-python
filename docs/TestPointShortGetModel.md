# TestPointShortGetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TestPointStatus**](TestPointStatus.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**last_test_result** | [**LastTestResultModel**](LastTestResultModel.md) |  | 
**id** | **str** | Unique ID of the test point | [optional] 
**created_date** | **datetime** | Creation date of the test point | [optional] 
**created_by_id** | **str** | Unique ID of the test point creator | [optional] 
**modified_date** | **datetime, none_type** | Last modification date of the test point | [optional] 
**modified_by_id** | **str, none_type** | Unique ID of the test point last editor | [optional] 
**tester_id** | **str, none_type** | Unique ID of the test point assigned user | [optional] 
**parameters** | **{str: (str, none_type)}, none_type** | Collection of the test point parameters | [optional] 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Collection of attributes of work item the test point represents | [optional] 
**tags** | **[str], none_type** | Collection of the test point tags | [optional] 
**links** | **[str], none_type** | Collection of the test point links | [optional] 
**test_suite_id** | **str** | Unique ID of test suite the test point assigned to | [optional] 
**work_item_id** | **str** | Unique ID of work item the test point represents | [optional] 
**work_item_global_id** | **int** | Global ID of work item the test point represents | [optional] 
**work_item_version_id** | **str** | Unique ID of work item version the test point represents | [optional] 
**is_automated** | **bool** | Indicates if the test point represents an autotest | [optional] 
**name** | **str, none_type** | Name of the test point | [optional] 
**configuration_id** | **str** | Unique ID of the test point configuration | [optional] 
**duration** | **int** | Duration of the test point | [optional] 
**section_id** | **str** | Unique ID of section where work item the test point represents is located | [optional] 
**section_name** | **str, none_type** | Name of section where work item the test point represents is located | [optional] 
**project_id** | **str** | Unique ID of the test point project | [optional] 
**iteration_id** | **str** | Unique ID of work item iteration the test point represents | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


