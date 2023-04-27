# TestResultShortGetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome** | [**TestResultOutcome**](TestResultOutcome.md) |  | 
**id** | **str** | Unique ID of test result | [optional] 
**name** | **str, none_type** | Name of autotest represented by the test result | [optional] 
**autotest_global_id** | **int** | Global ID of autotest represented by test result | [optional] 
**test_run_id** | **str** | Unique ID of test run where test result is located | [optional] 
**configuration_id** | **str** | Unique ID of configuration which test result uses | [optional] 
**configuration_name** | **str, none_type** | Name of configuration which test result uses | [optional] 
**result_reasons** | [**[AutotestResultReasonSubGetModel], none_type**](AutotestResultReasonSubGetModel.md) | Collection of result reasons which test result have | [optional] 
**comment** | **str, none_type** | Comment to test result | [optional] 
**date** | **datetime** | Date when test result has been set | [optional] 
**duration** | **int, none_type** | Time which it took to run the test | [optional] 
**links** | [**[LinkSubGetModel], none_type**](LinkSubGetModel.md) | Collection of links attached to test result | [optional] 
**attachments** | [**[AttachmentSubGetModel], none_type**](AttachmentSubGetModel.md) | Collection of files attached to test result | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


