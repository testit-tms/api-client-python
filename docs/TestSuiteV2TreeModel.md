# TestSuiteV2TreeModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the test suite | 
**test_plan_id** | **str** | Unique ID of test plan to which the test suite belongs | 
**name** | **str** | Name of the test suite | 
**children** | [**[TestSuiteV2TreeModel], none_type**](TestSuiteV2TreeModel.md) | nested enumeration of children is allowed | [optional] 
**refresh_date** | **datetime, none_type** | Date of the last refresh of the test suite | [optional] 
**parent_id** | **str, none_type** | Unique ID of the parent test suite in hierarchy | [optional] 
**type** | [**TestSuiteType**](TestSuiteType.md) |  | [optional] 
**save_structure** | **bool, none_type** | Indicates if the test suite retains section tree structure | [optional] 
**auto_refresh** | **bool, none_type** | Indicates if scheduled auto refresh is enabled for the test suite | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


