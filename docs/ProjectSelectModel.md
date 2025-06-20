# ProjectSelectModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**ProjectsFilterModel**](ProjectsFilterModel.md) |  | [optional] 
**extraction_model** | [**ProjectExtractionModel**](ProjectExtractionModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.project_select_model import ProjectSelectModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSelectModel from a JSON string
project_select_model_instance = ProjectSelectModel.from_json(json)
# print the JSON string representation of the object
print ProjectSelectModel.to_json()

# convert the object into a dict
project_select_model_dict = project_select_model_instance.to_dict()
# create an instance of ProjectSelectModel from a dict
project_select_model_from_dict = ProjectSelectModel.from_dict(project_select_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


