# CreateProjectApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the project | 
**description** | **str** | Description of the project | [optional] 
**is_favorite** | **bool** | Indicates if the project is marked as favorite | [optional] 
**workflow_id** | **str** | Identifier of the workflow project should use | [optional] 

## Example

```python
from testit_api_client.models.create_project_api_model import CreateProjectApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectApiModel from a JSON string
create_project_api_model_instance = CreateProjectApiModel.from_json(json)
# print the JSON string representation of the object
print CreateProjectApiModel.to_json()

# convert the object into a dict
create_project_api_model_dict = create_project_api_model_instance.to_dict()
# create an instance of CreateProjectApiModel from a dict
create_project_api_model_from_dict = CreateProjectApiModel.from_dict(create_project_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


