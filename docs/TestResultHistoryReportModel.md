# TestResultHistoryReportModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | 
**user_id** | **str** | If test run was stopped, this property equals identifier of user who stopped it.Otherwise, the property equals identifier of user who created the test result | 
**is_automated** | **bool** |  | 
**created_by_id** | **str** |  | 
**test_run_id** | **str, none_type** |  | [optional] 
**test_run_name** | **str, none_type** |  | [optional] 
**created_by_user_name** | **str, none_type** |  | [optional] 
**test_plan_id** | **str, none_type** |  | [optional] 
**test_plan_global_id** | **int, none_type** |  | [optional] 
**test_plan_name** | **str, none_type** |  | [optional] 
**configuration_name** | **str, none_type** | If test point related to the test result has configuration, this property will be equal to the test point configuration name. Otherwise, this property will be equal to the test result configuration name | [optional] 
**outcome** | **str, none_type** | If any test result related to the test run is linked with autotest and the run has an outcome, the outcome value equalsto the worst outcome of the last modified test result.Otherwise, the outcome equals to the outcome of first created test result in the test run | [optional] 
**comment** | **str, none_type** | If any test result related to the test run is linked with autotest, comment will have default valueOtherwise, the comment equals to the comment of first created test result in the test run | [optional] 
**links** | [**[LinkModel], none_type**](LinkModel.md) | If any test result related to the test run is linked with autotest, link will be equal to the links of last modified test result.Otherwise, the links equals to the links of first created test result in the test run | [optional] 
**started_on** | **datetime, none_type** |  | [optional] 
**completed_on** | **datetime, none_type** |  | [optional] 
**duration** | **int, none_type** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**attachments** | [**[AttachmentModel], none_type**](AttachmentModel.md) | If any test result related to the test run is linked with autotest, attachments will be equal to the attachments of last modified test result.Otherwise, the attachments equals to the attachments of first created test result in the test run | [optional] 
**work_item_version_id** | **str, none_type** |  | [optional] 
**work_item_version_number** | **int, none_type** |  | [optional] 
**launch_source** | **str, none_type** |  | [optional] 
**failure_class_ids** | **[str], none_type** |  | [optional] 
**parameters** | **{str: (str, none_type)}, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


