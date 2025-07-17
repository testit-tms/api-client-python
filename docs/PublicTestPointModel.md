# PublicTestPointModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_id** | **str** |  | 
**configuration_global_id** | **int** |  | 
**auto_test_ids** | **List[str]** |  | [optional] 
**iteration_id** | **str** |  | 
**parameter_models** | [**List[ParameterShortModel]**](ParameterShortModel.md) |  | [optional] 
**id** | **str** |  | 

## Example

```python
from testit_api_client.models.public_test_point_model import PublicTestPointModel

# TODO update the JSON string below
json = "{}"
# create an instance of PublicTestPointModel from a JSON string
public_test_point_model_instance = PublicTestPointModel.from_json(json)
# print the JSON string representation of the object
print PublicTestPointModel.to_json()

# convert the object into a dict
public_test_point_model_dict = public_test_point_model_instance.to_dict()
# create an instance of PublicTestPointModel from a dict
public_test_point_model_from_dict = PublicTestPointModel.from_dict(public_test_point_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


