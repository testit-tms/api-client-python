# ProjectShortApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of project | 
**is_deleted** | **bool** | Indicates whether the project is deleted | 
**global_id** | **int** | Global ID of project | 
**name** | **str** | Name of project | 
**type** | [**ProjectType**](ProjectType.md) | Type of the project | 
**is_favorite** | **bool** | Indicates if the project is marked as favorite | 

## Example

```python
from testit_api_client.models.project_short_api_result import ProjectShortApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectShortApiResult from a JSON string
project_short_api_result_instance = ProjectShortApiResult.from_json(json)
# print the JSON string representation of the object
print(ProjectShortApiResult.to_json())

# convert the object into a dict
project_short_api_result_dict = project_short_api_result_instance.to_dict()
# create an instance of ProjectShortApiResult from a dict
project_short_api_result_from_dict = ProjectShortApiResult.from_dict(project_short_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


