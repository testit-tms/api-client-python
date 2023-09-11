# ApiV2TestPointsSearchPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_plan_ids** | **[str], none_type** | Specifies a test point test plan IDS to search for | [optional] 
**test_suite_ids** | **[str], none_type** | Specifies a test point test suite IDs to search for | [optional] 
**work_item_global_ids** | **[int], none_type** | Specifies a test point work item global IDs to search for | [optional] 
**work_item_median_duration** | [**TestPointFilterModelWorkItemMedianDuration**](TestPointFilterModelWorkItemMedianDuration.md) |  | [optional] 
**statuses** | [**[TestPointStatus], none_type**](TestPointStatus.md) | Specifies a test point statuses to search for | [optional] 
**priorities** | [**[WorkItemPriorityModel], none_type**](WorkItemPriorityModel.md) | Specifies a test point priorities to search for | [optional] 
**is_automated** | **bool, none_type** | Specifies a test point automation status to search for | [optional] 
**name** | **str, none_type** | Specifies a test point name to search for | [optional] 
**configuration_ids** | **[str], none_type** | Specifies a test point configuration IDs to search for | [optional] 
**tester_ids** | **[str], none_type** | Specifies a test point assigned user IDs to search for | [optional] 
**duration** | [**TestPointFilterModelDuration**](TestPointFilterModelDuration.md) |  | [optional] 
**section_ids** | **[str], none_type** | Specifies a test point work item section IDs to search for | [optional] 
**created_date** | [**TestPointFilterModelCreatedDate**](TestPointFilterModelCreatedDate.md) |  | [optional] 
**created_by_ids** | **[str], none_type** | Specifies a test point creator IDs to search for | [optional] 
**modified_date** | [**TestPointFilterModelModifiedDate**](TestPointFilterModelModifiedDate.md) |  | [optional] 
**modified_by_ids** | **[str], none_type** | Specifies a test point last editor IDs to search for | [optional] 
**tags** | **[str], none_type** | Specifies a test point tags to search for | [optional] 
**attributes** | **{str: ([str],)}, none_type** | Specifies a test point attributes to search for | [optional] 
**work_item_created_date** | [**TestPointFilterModelWorkItemCreatedDate**](TestPointFilterModelWorkItemCreatedDate.md) |  | [optional] 
**work_item_created_by_ids** | **[str], none_type** | Specifies a work item creator IDs to search for | [optional] 
**work_item_modified_date** | [**TestPointFilterModelWorkItemModifiedDate**](TestPointFilterModelWorkItemModifiedDate.md) |  | [optional] 
**work_item_modified_by_ids** | **[str], none_type** | Specifies a work item last editor IDs to search for | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


