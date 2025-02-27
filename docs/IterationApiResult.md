# IterationApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**parameters** | [**List[ParameterShortApiResult]**](ParameterShortApiResult.md) |  | [optional] 

## Example

```python
from testit_api_client.models.iteration_api_result import IterationApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of IterationApiResult from a JSON string
iteration_api_result_instance = IterationApiResult.from_json(json)
# print the JSON string representation of the object
print(IterationApiResult.to_json())

# convert the object into a dict
iteration_api_result_dict = iteration_api_result_instance.to_dict()
# create an instance of IterationApiResult from a dict
iteration_api_result_from_dict = IterationApiResult.from_dict(iteration_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


