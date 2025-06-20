# WorkItemLocalFilterModel

Collection of filters to apply to search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**source_types** | [**List[WorkItemSourceTypeModel]**](WorkItemSourceTypeModel.md) | Collection of priorities of work item | [optional] 
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
from testit_api_client.models.work_item_local_filter_model import WorkItemLocalFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemLocalFilterModel from a JSON string
work_item_local_filter_model_instance = WorkItemLocalFilterModel.from_json(json)
# print the JSON string representation of the object
print(WorkItemLocalFilterModel.to_json())

# convert the object into a dict
work_item_local_filter_model_dict = work_item_local_filter_model_instance.to_dict()
# create an instance of WorkItemLocalFilterModel from a dict
work_item_local_filter_model_from_dict = WorkItemLocalFilterModel.from_dict(work_item_local_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


