# ParameterPostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the parameter | 
**name** | **str** | Key of the parameter | 

## Example

```python
from testit_api_client.models.parameter_post_model import ParameterPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterPostModel from a JSON string
parameter_post_model_instance = ParameterPostModel.from_json(json)
# print the JSON string representation of the object
print(ParameterPostModel.to_json())

# convert the object into a dict
parameter_post_model_dict = parameter_post_model_instance.to_dict()
# create an instance of ParameterPostModel from a dict
parameter_post_model_from_dict = ParameterPostModel.from_dict(parameter_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


