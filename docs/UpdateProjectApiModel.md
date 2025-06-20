# UpdateProjectApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the project | 
**name** | **str** | Name of the project | 
**description** | **str** | Description of the project | [optional] 
**is_favorite** | **bool** | Indicates if the project is marked as favorite | [optional] 
**workflow_id** | **str** | Identifier of the workflow project should use | [optional] 

## Example

```python
from testit_api_client.models.update_project_api_model import UpdateProjectApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectApiModel from a JSON string
update_project_api_model_instance = UpdateProjectApiModel.from_json(json)
# print the JSON string representation of the object
print UpdateProjectApiModel.to_json()

# convert the object into a dict
update_project_api_model_dict = update_project_api_model_instance.to_dict()
# create an instance of UpdateProjectApiModel from a dict
update_project_api_model_from_dict = UpdateProjectApiModel.from_dict(update_project_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


