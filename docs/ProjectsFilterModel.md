# ProjectsFilterModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies a project name to search for | [optional] 
**is_favorite** | **bool** | Specifies a project favorite status to search for | [optional] 
**is_deleted** | **bool** | Specifies a project deleted status to search for | [optional] 
**test_cases_count** | [**Int32RangeSelectorModel**](Int32RangeSelectorModel.md) | Specifies a project range of test cases count to search for | [optional] 
**checklists_count** | [**Int32RangeSelectorModel**](Int32RangeSelectorModel.md) | Specifies a project range of checklists count to search for | [optional] 
**shared_steps_count** | [**Int32RangeSelectorModel**](Int32RangeSelectorModel.md) | Specifies a project range of shared steps count to search for | [optional] 
**autotests_count** | [**Int32RangeSelectorModel**](Int32RangeSelectorModel.md) | Specifies a project range of autotests count to search for | [optional] 
**global_ids** | **List[int]** | Specifies a project global IDs to search for | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a project range of creation date to search for | [optional] 
**created_by_ids** | **List[str]** | Specifies an autotest creator IDs to search for | [optional] 
**types** | [**List[ProjectTypeModel]**](ProjectTypeModel.md) | Collection of project types to search for | [optional] 

## Example

```python
from testit_api_client.models.projects_filter_model import ProjectsFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsFilterModel from a JSON string
projects_filter_model_instance = ProjectsFilterModel.from_json(json)
# print the JSON string representation of the object
print ProjectsFilterModel.to_json()

# convert the object into a dict
projects_filter_model_dict = projects_filter_model_instance.to_dict()
# create an instance of ProjectsFilterModel from a dict
projects_filter_model_from_dict = ProjectsFilterModel.from_dict(projects_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


