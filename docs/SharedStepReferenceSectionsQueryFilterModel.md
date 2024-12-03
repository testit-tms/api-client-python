# SharedStepReferenceSectionsQueryFilterModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of section | [optional] 
**created_by_ids** | **List[str]** | Collection of identifiers of users who created work item | [optional] 
**modified_by_ids** | **List[str]** | Collection of identifiers of users who applied last modification to work item | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Date and time of work item creation | [optional] 
**modified_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Date and time of work item last modification | [optional] 

## Example

```python
from testit_api_client.models.shared_step_reference_sections_query_filter_model import SharedStepReferenceSectionsQueryFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of SharedStepReferenceSectionsQueryFilterModel from a JSON string
shared_step_reference_sections_query_filter_model_instance = SharedStepReferenceSectionsQueryFilterModel.from_json(json)
# print the JSON string representation of the object
print(SharedStepReferenceSectionsQueryFilterModel.to_json())

# convert the object into a dict
shared_step_reference_sections_query_filter_model_dict = shared_step_reference_sections_query_filter_model_instance.to_dict()
# create an instance of SharedStepReferenceSectionsQueryFilterModel from a dict
shared_step_reference_sections_query_filter_model_from_dict = SharedStepReferenceSectionsQueryFilterModel.from_dict(shared_step_reference_sections_query_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


