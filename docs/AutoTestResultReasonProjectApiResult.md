# AutoTestResultReasonProjectApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Failure category identifier | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 
**failure_category** | [**FailureCategory**](FailureCategory.md) |  | 
**created_date** | **datetime** | Failure category creation date | 
**created_by_id** | **str** | Failure category creator identifier | 
**projects** | [**[ProjectNameApiResult]**](ProjectNameApiResult.md) | Projects names | 
**failure_class_regexes** | [**[FailureClassRegexApiResult]**](FailureClassRegexApiResult.md) | Failure category regexes | 
**name** | **str, none_type** | Failure category name | [optional] 
**modified_date** | **datetime, none_type** | Failure category last modification date | [optional] 
**modified_by_id** | **str, none_type** | Failure category last modifier identifier | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


