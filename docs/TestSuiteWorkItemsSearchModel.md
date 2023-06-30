# TestSuiteWorkItemsSearchModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Name of work item | [optional] 
**global_ids** | **[int], none_type** | Collection of global (integer) identifiers | [optional] 
**section_ids** | **[str], none_type** | Collection of section identifiers | [optional] 
**priorities** | [**[WorkItemPriorityModel], none_type**](WorkItemPriorityModel.md) | Collection of priorities of work item | [optional] 
**is_automated** | **bool, none_type** | Is result must consist of only manual/automated work items | [optional] 
**states** | [**[WorkItemStates], none_type**](WorkItemStates.md) | Collection of states of work item | [optional] 
**duration** | [**TestSuiteWorkItemsSearchModelDuration**](TestSuiteWorkItemsSearchModelDuration.md) |  | [optional] 
**created_date** | [**TestSuiteWorkItemsSearchModelCreatedDate**](TestSuiteWorkItemsSearchModelCreatedDate.md) |  | [optional] 
**modified_date** | [**TestSuiteWorkItemsSearchModelModifiedDate**](TestSuiteWorkItemsSearchModelModifiedDate.md) |  | [optional] 
**created_by_ids** | **[str], none_type** | Collection of identifiers of users who created work item | [optional] 
**modified_by_ids** | **[str], none_type** | Collection of identifiers of users who applied last modification to work item | [optional] 
**attributes** | **{str: ([str],)}, none_type** | Custom attributes of work item | [optional] 
**is_deleted** | **bool, none_type** | Is result must consist of only actual/deleted work items | [optional] 
**tag_names** | **[str], none_type** | Collection of tags | [optional] 
**entity_types** | **[str], none_type** | Collection of types of work item  &lt;br&gt;Allowed values: &#x60;TestCases&#x60;, &#x60;CheckLists&#x60;, &#x60;SharedSteps&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


