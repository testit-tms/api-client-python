# ProjectShortModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the project | 
**description** | **str** | Description of the project | [optional] 
**name** | **str** | Name of the project | 
**is_favorite** | **bool** | Indicates if the project is marked as favorite | 
**test_cases_count** | **int** | Number of test cases in the project | [optional] 
**shared_steps_count** | **int** | Number of shared steps in the project | [optional] 
**check_lists_count** | **int** | Number of checklists in the project | [optional] 
**auto_tests_count** | **int** | Number of autotests in the project | [optional] 
**is_deleted** | **bool** | Indicates if the project is deleted | 
**created_date** | **datetime** | Creation date of the project | 
**modified_date** | **datetime** | Last modification date of the project | [optional] 
**created_by_id** | **str** | Unique ID of the project creator | 
**modified_by_id** | **str** | Unique ID of the project last editor | [optional] 
**global_id** | **int** | Global ID of the project | 
**type** | [**ProjectTypeModel**](ProjectTypeModel.md) | Type of the project | 
**is_flaky_auto** | **bool** | Indicates if the status \&quot;Flaky/Stable\&quot; sets automatically | 
**workflow_id** | **str** |  | 

## Example

```python
from testit_api_client.models.project_short_model import ProjectShortModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectShortModel from a JSON string
project_short_model_instance = ProjectShortModel.from_json(json)
# print the JSON string representation of the object
print ProjectShortModel.to_json()

# convert the object into a dict
project_short_model_dict = project_short_model_instance.to_dict()
# create an instance of ProjectShortModel from a dict
project_short_model_from_dict = ProjectShortModel.from_dict(project_short_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


