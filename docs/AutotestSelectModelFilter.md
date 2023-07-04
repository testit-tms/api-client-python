# AutotestSelectModelFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **[str], none_type** | Specifies an autotest projects IDs to search for | [optional] 
**external_ids** | **[str], none_type** | Specifies an autotest external IDs to search for | [optional] 
**global_ids** | **[int], none_type** | Specifies an autotest global IDs to search for | [optional] 
**name** | **str, none_type** | Specifies an autotest name to search for | [optional] 
**is_flaky** | **bool, none_type** | Specifies an autotest flaky status to search for | [optional] 
**must_be_approved** | **bool, none_type** | Specifies an autotest unapproved changes status to search for | [optional] 
**stability_percentage** | [**AutotestFilterModelStabilityPercentage**](AutotestFilterModelStabilityPercentage.md) |  | [optional] 
**created_date** | [**AutotestFilterModelCreatedDate**](AutotestFilterModelCreatedDate.md) |  | [optional] 
**created_by_ids** | **[str], none_type** | Specifies an autotest creator IDs to search for | [optional] 
**modified_date** | [**AutotestFilterModelModifiedDate**](AutotestFilterModelModifiedDate.md) |  | [optional] 
**modified_by_ids** | **[str], none_type** | Specifies an autotest last editor IDs to search for | [optional] 
**is_deleted** | **bool, none_type** | Specifies an autotest deleted status to search for | [optional] 
**namespace** | **str, none_type** | Specifies an autotest namespace to search for | [optional] 
**is_empty_namespace** | **bool, none_type** | Specifies an autotest namespace name presence status to search for | [optional] 
**class_name** | **str, none_type** | Specifies an autotest class name to search for | [optional] 
**is_empty_class_name** | **bool, none_type** | Specifies an autotest class name presence status to search for | [optional] 
**last_test_result_outcome** | **bool, date, datetime, dict, float, int, list, str, none_type** | Specifies an autotest outcome of the last test result to search for | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


