# AutoTestSelectApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**AutoTestFilterApiModel**](AutoTestFilterApiModel.md) |  | [optional] 
**extraction_model** | [**AutoTestExtractionApiModel**](AutoTestExtractionApiModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.auto_test_select_api_model import AutoTestSelectApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestSelectApiModel from a JSON string
auto_test_select_api_model_instance = AutoTestSelectApiModel.from_json(json)
# print the JSON string representation of the object
print AutoTestSelectApiModel.to_json()

# convert the object into a dict
auto_test_select_api_model_dict = auto_test_select_api_model_instance.to_dict()
# create an instance of AutoTestSelectApiModel from a dict
auto_test_select_api_model_from_dict = AutoTestSelectApiModel.from_dict(auto_test_select_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


