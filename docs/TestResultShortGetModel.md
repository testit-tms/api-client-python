# TestResultShortGetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the test result | 
**name** | **str** | Name of autotest represented by the test result | 
**autotest_global_id** | **int** | Global ID of autotest represented by the test result | 
**test_run_id** | **str** | Unique ID of test run where the test result is located | 
**configuration_id** | **str** | Unique ID of configuration which the test result uses | 
**configuration_name** | **str** | Name of configuration which the test result uses | 
**outcome** | **str** | Outcome of the test result | 
**result_reasons** | [**[AutotestResultReasonSubGetModel]**](AutotestResultReasonSubGetModel.md) | Collection of result reasons which the test result have | 
**date** | **datetime** | Date when the test result has been set | 
**links** | [**[LinkSubGetModel]**](LinkSubGetModel.md) | Collection of links attached to the test result | 
**attachments** | [**[AttachmentModel]**](AttachmentModel.md) | Collection of files attached to the test result | 
**comment** | **str, none_type** | Comment to the test result | [optional] 
**duration** | **int, none_type** | Time which it took to run the test | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


