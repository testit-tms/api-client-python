# SearchWorkflowsApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inquiry** | [**Inquiry**](Inquiry.md) |  | [optional] 

## Example

```python
from testit_api_client.models.search_workflows_api_model import SearchWorkflowsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of SearchWorkflowsApiModel from a JSON string
search_workflows_api_model_instance = SearchWorkflowsApiModel.from_json(json)
# print the JSON string representation of the object
print(SearchWorkflowsApiModel.to_json())

# convert the object into a dict
search_workflows_api_model_dict = search_workflows_api_model_instance.to_dict()
# create an instance of SearchWorkflowsApiModel from a dict
search_workflows_api_model_from_dict = SearchWorkflowsApiModel.from_dict(search_workflows_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


