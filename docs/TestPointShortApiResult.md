# TestPointShortApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Test point unique internal identifier | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 
**status_model** | [**TestPointShortApiResultStatusModel**](TestPointShortApiResultStatusModel.md) |  | 
**iteration_id** | **str** | Iteration unique identifier | 
**test_suite_id** | **str** | Test suite to which test point relates unique identifier | 
**tester_id** | **str, none_type** | Tester who is responded for the test unique internal identifier | [optional] 
**work_item_id** | **str, none_type** | Workitem to which test point relates unique identifier | [optional] 
**configuration_id** | **str, none_type** | Configuration to which test point relates unique identifier | [optional] 
**status** | **str, none_type** | Test point status    Applies one of these values: Blocked, NoResults, Failed, Passed | [optional] 
**last_test_result_id** | **str, none_type** | Last test result unique identifier | [optional] 
**work_item_median_duration** | **int, none_type** | Median duration of work item the test point represents | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


