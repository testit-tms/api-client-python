# AutoTestFilterApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **[str], none_type** | Specifies an autotest projects IDs to search for | [optional] 
**external_ids** | **[str], none_type** | Specifies an autotest external IDs to search for | [optional] 
**global_ids** | **[int], none_type** | Specifies an autotest global IDs to search for | [optional] 
**name** | **str, none_type** | Specifies an autotest name to search for | [optional] 
**is_flaky** | **bool, none_type** | Specifies an autotest flaky status to search for | [optional] 
**must_be_approved** | **bool, none_type** | Specifies an autotest unapproved changes status to search for | [optional] 
**stability_percentage** | [**AutoTestFilterApiModelStabilityPercentage**](AutoTestFilterApiModelStabilityPercentage.md) |  | [optional] 
**created_date** | [**AutoTestFilterApiModelCreatedDate**](AutoTestFilterApiModelCreatedDate.md) |  | [optional] 
**created_by_ids** | **[str], none_type** | Specifies an autotest creator IDs to search for | [optional] 
**modified_date** | [**AutoTestFilterApiModelModifiedDate**](AutoTestFilterApiModelModifiedDate.md) |  | [optional] 
**modified_by_ids** | **[str], none_type** | Specifies an autotest last editor IDs to search for | [optional] 
**is_deleted** | **bool, none_type** | Specifies an autotest deleted status to search for | [optional] 
**namespace** | **str, none_type** | Specifies an autotest namespace to search for | [optional] 
**is_empty_namespace** | **bool, none_type** | Specifies an autotest namespace name presence status to search for | [optional] 
**class_name** | **str, none_type** | Specifies an autotest class name to search for | [optional] 
**is_empty_class_name** | **bool, none_type** | Specifies an autotest class name presence status to search for | [optional] 
**last_test_result_outcome** | [**AutotestResultOutcome**](AutotestResultOutcome.md) |  | [optional] 
**last_test_result_status_code** | **str, none_type** | Specifies an autotest status code of the last test result to search for | [optional] 
**external_key** | **str, none_type** | Specifies an autotest external key to search for | [optional] 
**last_test_result_configuration_ids** | **[str], none_type** | Specifies an autotest configuration IDs of the last test result to search for | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


