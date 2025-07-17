# ProjectShortestModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of project | 
**is_deleted** | **bool** | Indicates whether the project is deleted | 
**global_id** | **int** | Global ID of project | 
**name** | **str** | Name of project | 
**type** | [**ProjectTypeModel**](ProjectTypeModel.md) | Type of the project | 

## Example

```python
from testit_api_client.models.project_shortest_model import ProjectShortestModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectShortestModel from a JSON string
project_shortest_model_instance = ProjectShortestModel.from_json(json)
# print the JSON string representation of the object
print ProjectShortestModel.to_json()

# convert the object into a dict
project_shortest_model_dict = project_shortest_model_instance.to_dict()
# create an instance of ProjectShortestModel from a dict
project_shortest_model_from_dict = ProjectShortestModel.from_dict(project_shortest_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


