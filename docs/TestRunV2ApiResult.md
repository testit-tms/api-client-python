# TestRunV2ApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Test run unique identifier | 
**name** | **str** | Test run name | 
**state_name** | [**TestRunState**](TestRunState.md) |  | 
**status** | [**TestRunByAutoTestApiResultStatus**](TestRunByAutoTestApiResultStatus.md) |  | 
**project_id** | **str** | Project unique identifier              This property is used to link test run with project. | 
**created_date** | **datetime** | Date and time of test run creation | 
**created_by_id** | **str** | Unique identifier of user who created test run | 
**attachments** | [**[AttachmentApiResult]**](AttachmentApiResult.md) | Collection of attachments related to the test run | 
**links** | [**[LinkApiResult]**](LinkApiResult.md) | Collection of links related to the test run | 
**webhooks** | [**[NamedEntityApiModel]**](NamedEntityApiModel.md) | Enabled webhooks | 
**run_count** | **int** | Run count | 
**tags** | **[str]** | Collection of tags associated with the test run | 
**description** | **str, none_type** | Test run description | [optional] 
**launch_source** | **str, none_type** | Test run launch source              Once launch source is specified it cannot be updated. | [optional] 
**started_on** | **datetime, none_type** | Date and time of test run start | [optional] 
**completed_on** | **datetime, none_type** | Date and time of test run end | [optional] 
**test_plan_id** | **str, none_type** | Test plan unique identifier              This property is used to link test run with test plan. | [optional] 
**test_results** | [**[TestResultV2GetModel], none_type**](TestResultV2GetModel.md) | Enumeration of test results related to test run | [optional] 
**modified_date** | **datetime, none_type** | Date and time of last test run  modification | [optional] 
**modified_by_id** | **str, none_type** | Unique identifier of user who applied last test run  modification | [optional] 
**created_by_user_name** | **str, none_type** | Username of user who created test run | [optional] 
**custom_parameters** | **{str: (str,)}, none_type** | Customers test run parameters | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


