# ApiV2WorkItemsSharedStepIdReferencesWorkItemsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Name of work item | [optional] 
**global_ids** | **[int], none_type** | Collection of global (integer) identifiers | [optional] 
**section_ids** | **[str], none_type** | Collection of section identifiers | [optional] 
**created_by_ids** | **[str], none_type** | Collection of identifiers of users who created work item | [optional] 
**modified_by_ids** | **[str], none_type** | Collection of identifiers of users who applied last modification to work item | [optional] 
**states** | [**[WorkItemStates], none_type**](WorkItemStates.md) | Collection of states of work item | [optional] 
**priorities** | [**[WorkItemPriorityModel], none_type**](WorkItemPriorityModel.md) | Collection of priorities of work item | [optional] 
**entity_types** | **[str], none_type** | Collection of types of work item  &lt;br&gt;Allowed values: &#x60;TestCases&#x60;, &#x60;CheckLists&#x60;, &#x60;SharedSteps&#x60; | [optional] 
**created_date** | [**SharedStepReferenceSectionsQueryFilterModelCreatedDate**](SharedStepReferenceSectionsQueryFilterModelCreatedDate.md) |  | [optional] 
**modified_date** | [**SharedStepReferenceSectionsQueryFilterModelModifiedDate**](SharedStepReferenceSectionsQueryFilterModelModifiedDate.md) |  | [optional] 
**is_automated** | **bool, none_type** | Is result must consist of only manual/automated work items | [optional] 
**tags** | **[str], none_type** | Collection of tags | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


