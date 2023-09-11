# TestResultShortGetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the test result | 
**autotest_global_id** | **int** | Global ID of autotest represented by the test result | 
**test_run_id** | **str** | Unique ID of test run where the test result is located | 
**configuration_id** | **str** | Unique ID of configuration which the test result uses | 
**date** | **datetime** | Date when the test result has been set | 
**name** | **str, none_type** | Name of autotest represented by the test result | [optional] 
**configuration_name** | **str, none_type** | Name of configuration which the test result uses | [optional] 
**outcome** | **str, none_type** | Outcome of the test result | [optional] 
**result_reasons** | [**[AutotestResultReasonSubGetModel], none_type**](AutotestResultReasonSubGetModel.md) | Collection of result reasons which the test result have | [optional] 
**comment** | **str, none_type** | Comment to the test result | [optional] 
**duration** | **int, none_type** | Time which it took to run the test | [optional] 
**links** | [**[LinkSubGetModel], none_type**](LinkSubGetModel.md) | Collection of links attached to the test result | [optional] 
**attachments** | [**[AttachmentModel], none_type**](AttachmentModel.md) | Collection of files attached to the test result | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


