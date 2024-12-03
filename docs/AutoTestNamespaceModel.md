# AutoTestNamespaceModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**classes** | **List[str]** |  | [optional] 

## Example

```python
from testit_api_client.models.auto_test_namespace_model import AutoTestNamespaceModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestNamespaceModel from a JSON string
auto_test_namespace_model_instance = AutoTestNamespaceModel.from_json(json)
# print the JSON string representation of the object
print(AutoTestNamespaceModel.to_json())

# convert the object into a dict
auto_test_namespace_model_dict = auto_test_namespace_model_instance.to_dict()
# create an instance of AutoTestNamespaceModel from a dict
auto_test_namespace_model_from_dict = AutoTestNamespaceModel.from_dict(auto_test_namespace_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


