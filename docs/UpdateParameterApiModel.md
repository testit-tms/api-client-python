# UpdateParameterApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID&#39;s of the parameter | 
**name** | **str** | Key of the parameter | 
**value** | **str** | Value of the parameter | 
**project_ids** | **List[str]** | List of projects where parameter should be available | [optional] 

## Example

```python
from testit_api_client.models.update_parameter_api_model import UpdateParameterApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateParameterApiModel from a JSON string
update_parameter_api_model_instance = UpdateParameterApiModel.from_json(json)
# print the JSON string representation of the object
print UpdateParameterApiModel.to_json()

# convert the object into a dict
update_parameter_api_model_dict = update_parameter_api_model_instance.to_dict()
# create an instance of UpdateParameterApiModel from a dict
update_parameter_api_model_from_dict = UpdateParameterApiModel.from_dict(update_parameter_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


