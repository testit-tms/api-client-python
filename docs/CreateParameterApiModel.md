# CreateParameterApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Key of the parameter | 
**value** | **str** | Value of the parameter | 
**project_ids** | **List[str]** | List of projects where parameter should be available | [optional] 

## Example

```python
from testit_api_client.models.create_parameter_api_model import CreateParameterApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateParameterApiModel from a JSON string
create_parameter_api_model_instance = CreateParameterApiModel.from_json(json)
# print the JSON string representation of the object
print CreateParameterApiModel.to_json()

# convert the object into a dict
create_parameter_api_model_dict = create_parameter_api_model_instance.to_dict()
# create an instance of CreateParameterApiModel from a dict
create_parameter_api_model_from_dict = CreateParameterApiModel.from_dict(create_parameter_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


