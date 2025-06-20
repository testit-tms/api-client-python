# AutoTestNamespacesCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespaces** | [**List[AutoTestNamespaceCountApiModel]**](AutoTestNamespaceCountApiModel.md) |  | 

## Example

```python
from testit_api_client.models.auto_test_namespaces_count_response import AutoTestNamespacesCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestNamespacesCountResponse from a JSON string
auto_test_namespaces_count_response_instance = AutoTestNamespacesCountResponse.from_json(json)
# print the JSON string representation of the object
print(AutoTestNamespacesCountResponse.to_json())

# convert the object into a dict
auto_test_namespaces_count_response_dict = auto_test_namespaces_count_response_instance.to_dict()
# create an instance of AutoTestNamespacesCountResponse from a dict
auto_test_namespaces_count_response_from_dict = AutoTestNamespacesCountResponse.from_dict(auto_test_namespaces_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


