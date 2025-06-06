# SharedStepReferencesQueryFilterModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of work item | [optional] 
**global_ids** | **List[int]** | Collection of global (integer) identifiers | [optional] 
**section_ids** | **List[str]** | Collection of section identifiers | [optional] 
**created_by_ids** | **List[str]** | Collection of identifiers of users who created work item | [optional] 
**modified_by_ids** | **List[str]** | Collection of identifiers of users who applied last modification to work item | [optional] 
**states** | [**List[WorkItemStates]**](WorkItemStates.md) | Collection of states of work item | [optional] 
**priorities** | [**List[WorkItemPriorityModel]**](WorkItemPriorityModel.md) | Collection of priorities of work item | [optional] 
**entity_types** | **List[str]** | Collection of types of work item  Allowed values: &#x60;TestCases&#x60;, &#x60;CheckLists&#x60;, &#x60;SharedSteps&#x60; | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Date and time of work item creation | [optional] 
**modified_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Date and time of work item last modification | [optional] 
**is_automated** | **bool** | Is result must consist of only manual/automated work items | [optional] 
**tags** | **List[str]** | Collection of tags | [optional] 

## Example

```python
from testit_api_client.models.shared_step_references_query_filter_model import SharedStepReferencesQueryFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of SharedStepReferencesQueryFilterModel from a JSON string
shared_step_references_query_filter_model_instance = SharedStepReferencesQueryFilterModel.from_json(json)
# print the JSON string representation of the object
print(SharedStepReferencesQueryFilterModel.to_json())

# convert the object into a dict
shared_step_references_query_filter_model_dict = shared_step_references_query_filter_model_instance.to_dict()
# create an instance of SharedStepReferencesQueryFilterModel from a dict
shared_step_references_query_filter_model_from_dict = SharedStepReferencesQueryFilterModel.from_dict(shared_step_references_query_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


