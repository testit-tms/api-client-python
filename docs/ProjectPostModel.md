# ProjectPostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the project | [optional] 
**name** | **str** | Name of the project | 
**is_favorite** | **bool** | Indicates if the project is marked as favorite | [optional] 
**is_flaky_auto** | **bool** | Indicates if the status \&quot;Flaky/Stable\&quot; sets automatically | [optional] 

## Example

```python
from testit_api_client.models.project_post_model import ProjectPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPostModel from a JSON string
project_post_model_instance = ProjectPostModel.from_json(json)
# print the JSON string representation of the object
print(ProjectPostModel.to_json())

# convert the object into a dict
project_post_model_dict = project_post_model_instance.to_dict()
# create an instance of ProjectPostModel from a dict
project_post_model_from_dict = ProjectPostModel.from_dict(project_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


