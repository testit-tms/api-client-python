# AutoTestFlakyBulkApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_test_select** | [**AutoTestSelectApiModel**](AutoTestSelectApiModel.md) |  | 
**value** | **bool** | Are autotests flaky | 

## Example

```python
from testit_api_client.models.auto_test_flaky_bulk_api_model import AutoTestFlakyBulkApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestFlakyBulkApiModel from a JSON string
auto_test_flaky_bulk_api_model_instance = AutoTestFlakyBulkApiModel.from_json(json)
# print the JSON string representation of the object
print(AutoTestFlakyBulkApiModel.to_json())

# convert the object into a dict
auto_test_flaky_bulk_api_model_dict = auto_test_flaky_bulk_api_model_instance.to_dict()
# create an instance of AutoTestFlakyBulkApiModel from a dict
auto_test_flaky_bulk_api_model_from_dict = AutoTestFlakyBulkApiModel.from_dict(auto_test_flaky_bulk_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


