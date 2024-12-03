# ProjectPutModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the project | 
**description** | **str** | Description of the project | [optional] 
**name** | **str** | Name of the project | 
**is_favorite** | **bool** | Indicates if the project is marked as favorite | [optional] 
**is_flaky_auto** | **bool** | Indicates if the status \&quot;Flaky/Stable\&quot; sets automatically | [optional] 
**type** | [**ProjectTypeModel**](ProjectTypeModel.md) | Type of the project | 

## Example

```python
from testit_api_client.models.project_put_model import ProjectPutModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPutModel from a JSON string
project_put_model_instance = ProjectPutModel.from_json(json)
# print the JSON string representation of the object
print(ProjectPutModel.to_json())

# convert the object into a dict
project_put_model_dict = project_put_model_instance.to_dict()
# create an instance of ProjectPutModel from a dict
project_put_model_from_dict = ProjectPutModel.from_dict(project_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


