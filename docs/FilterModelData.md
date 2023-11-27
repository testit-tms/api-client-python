# FilterModelData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **[str], none_type** | Collection of project identifiers | [optional] 
**name** | **str, none_type** | Name of work item | [optional] 
**ids** | **[str], none_type** | Specifies a work item unique IDs to search for | [optional] 
**global_ids** | **[int], none_type** | Collection of global (integer) identifiers | [optional] 
**attributes** | **{str: ([str], none_type)}, none_type** | Custom attributes of work item | [optional] 
**is_deleted** | **bool, none_type** | Is result must consist of only actual/deleted work items | [optional] 
**section_ids** | **[str], none_type** | Collection of section identifiers | [optional] 
**created_by_ids** | **[str], none_type** | Collection of identifiers of users who created work item | [optional] 
**modified_by_ids** | **[str], none_type** | Collection of identifiers of users who applied last modification to work item | [optional] 
**states** | [**[WorkItemStates], none_type**](WorkItemStates.md) | Collection of states of work item | [optional] 
**priorities** | [**[WorkItemPriorityModel], none_type**](WorkItemPriorityModel.md) | Collection of priorities of work item | [optional] 
**types** | [**[WorkItemEntityTypes], none_type**](WorkItemEntityTypes.md) | Collection of types of work item | [optional] 
**created_date** | [**TestPointFilterModelWorkItemCreatedDate**](TestPointFilterModelWorkItemCreatedDate.md) |  | [optional] 
**modified_date** | [**TestPointFilterModelWorkItemModifiedDate**](TestPointFilterModelWorkItemModifiedDate.md) |  | [optional] 
**duration** | [**TestSuiteWorkItemsSearchModelDuration**](TestSuiteWorkItemsSearchModelDuration.md) |  | [optional] 
**median_duration** | [**TestSuiteWorkItemsSearchModelMedianDuration**](TestSuiteWorkItemsSearchModelMedianDuration.md) |  | [optional] 
**is_automated** | **bool, none_type** | Is result must consist of only manual/automated work items | [optional] 
**tags** | **[str], none_type** | Collection of tags | [optional] 
**auto_test_ids** | **[str], none_type** | Collection of identifiers of linked autotests | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


