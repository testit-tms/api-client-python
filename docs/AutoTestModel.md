# AutoTestModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | Specifies the ID of your autotest in the external system.&lt;br /&gt;  To test the method, you can use any ID. | 
**project_id** | **str** | Specifies the project GUID.&lt;br /&gt;  You can get it using the &#x60;GET /api/v2/projects&#x60; method. | 
**name** | **str** | Specifies autotest name in the test management system. | 
**global_id** | **int** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**must_be_approved** | **bool, none_type** |  | [optional] 
**id** | **str** |  | [optional] 
**created_date** | **datetime, none_type** |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**last_test_run_id** | **str, none_type** |  | [optional] 
**last_test_run_name** | **str, none_type** |  | [optional] 
**last_test_result_id** | **str, none_type** |  | [optional] 
**last_test_result_outcome** | **str, none_type** | Property can contain one of these values: Passed, Failed, InProgress, Blocked, Skipped | [optional] 
**stability_percentage** | **int, none_type** |  | [optional] 
**links** | [**[LinkPutModel], none_type**](LinkPutModel.md) | Specifies the links in the autotest. | [optional] 
**namespace** | **str, none_type** | Specifies the name of the namespace in the test management system. | [optional] 
**classname** | **str, none_type** | Specifies the class name in the test management system. | [optional] 
**steps** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) | Specifies the steps in the autotest. | [optional] 
**setup** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) | Specifies the setup steps and relates them to the autotest. Supported values are the same as in the &#x60;steps&#x60; parameter. | [optional] 
**teardown** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) | Specifies the teardown steps and relates them to the autotest. Supported values are the same as in the &#x60;steps&#x60; parameter. | [optional] 
**title** | **str, none_type** | Specifies the name of the autotest in the autotest card.   The &#x60;Name&#x60; parameter is responsible for the name in the table. | [optional] 
**description** | **str, none_type** | Specifies the autotest description in the test management system. | [optional] 
**labels** | [**[LabelShortModel], none_type**](LabelShortModel.md) | Specifies autotest labels. | [optional] 
**is_flaky** | **bool** | Marks the autotest as flaky. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


