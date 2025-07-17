# AutoTestNamespaceCountApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**count** | **int** |  | 
**classes** | [**List[AutoTestClassCountApiModel]**](AutoTestClassCountApiModel.md) |  | 

## Example

```python
from testit_api_client.models.auto_test_namespace_count_api_model import AutoTestNamespaceCountApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestNamespaceCountApiModel from a JSON string
auto_test_namespace_count_api_model_instance = AutoTestNamespaceCountApiModel.from_json(json)
# print the JSON string representation of the object
print AutoTestNamespaceCountApiModel.to_json()

# convert the object into a dict
auto_test_namespace_count_api_model_dict = auto_test_namespace_count_api_model_instance.to_dict()
# create an instance of AutoTestNamespaceCountApiModel from a dict
auto_test_namespace_count_api_model_from_dict = AutoTestNamespaceCountApiModel.from_dict(auto_test_namespace_count_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


