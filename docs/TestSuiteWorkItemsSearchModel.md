# TestSuiteWorkItemsSearchModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_names** | **List[str]** | Collection of tags | [optional] 
**entity_types** | [**List[WorkItemEntityTypes]**](WorkItemEntityTypes.md) | Collection of types of work item   Allowed values: &#x60;TestCases&#x60;, &#x60;CheckLists&#x60;, &#x60;SharedSteps&#x60; | [optional] 
**name_or_id** | **str** | Name or identifier (UUID) of work item | [optional] 
**include_ids** | **List[str]** | Collection of identifiers of work items which need to be included in result regardless of filtering | [optional] 
**exclude_ids** | **List[str]** | Collection of identifiers of work items which need to be excluded from result regardless of filtering | [optional] 
**project_ids** | **List[str]** | Collection of project identifiers | [optional] 
**links** | [**WorkItemLinkFilterModel**](WorkItemLinkFilterModel.md) | Specifies a work item filter by its links | [optional] 
**name** | **str** | Name of work item | [optional] 
**ids** | **List[str]** | Specifies a work item unique IDs to search for | [optional] 
**global_ids** | **List[int]** | Collection of global (integer) identifiers | [optional] 
**attributes** | **Dict[str, Optional[List[str]]]** | Custom attributes of work item | [optional] 
**is_deleted** | **bool** | Is result must consist of only actual/deleted work items | [optional] 
**section_ids** | **List[str]** | Collection of section identifiers | [optional] 
**created_by_ids** | **List[str]** | Collection of identifiers of users who created work item | [optional] 
**modified_by_ids** | **List[str]** | Collection of identifiers of users who applied last modification to work item | [optional] 
**states** | [**List[WorkItemStates]**](WorkItemStates.md) | Collection of states of work item | [optional] 
**priorities** | [**List[WorkItemPriorityModel]**](WorkItemPriorityModel.md) | Collection of priorities of work item | [optional] 
**types** | [**List[WorkItemEntityTypes]**](WorkItemEntityTypes.md) | Collection of types of work item | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a work item range of creation date to search for | [optional] 
**modified_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a work item range of last modification date to search for | [optional] 
**duration** | [**Int32RangeSelectorModel**](Int32RangeSelectorModel.md) | Specifies a work item duration range to search for | [optional] 
**median_duration** | [**Int64RangeSelectorModel**](Int64RangeSelectorModel.md) | Specifies a work item median duration range to search for | [optional] 
**is_automated** | **bool** | Is result must consist of only manual/automated work items | [optional] 
**tags** | **List[str]** | Collection of tags | [optional] 
**auto_test_ids** | **List[str]** | Collection of identifiers of linked autotests | [optional] 
**work_item_version_ids** | **List[str]** | Collection of identifiers work items versions. | [optional] 

## Example

```python
from testit_api_client.models.test_suite_work_items_search_model import TestSuiteWorkItemsSearchModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestSuiteWorkItemsSearchModel from a JSON string
test_suite_work_items_search_model_instance = TestSuiteWorkItemsSearchModel.from_json(json)
# print the JSON string representation of the object
print(TestSuiteWorkItemsSearchModel.to_json())

# convert the object into a dict
test_suite_work_items_search_model_dict = test_suite_work_items_search_model_instance.to_dict()
# create an instance of TestSuiteWorkItemsSearchModel from a dict
test_suite_work_items_search_model_from_dict = TestSuiteWorkItemsSearchModel.from_dict(test_suite_work_items_search_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


