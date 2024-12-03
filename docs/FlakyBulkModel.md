# FlakyBulkModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autotest_select** | [**AutotestSelectModel**](AutotestSelectModel.md) |  | 
**value** | **bool** | Are autotests flaky | 

## Example

```python
from testit_api_client.models.flaky_bulk_model import FlakyBulkModel

# TODO update the JSON string below
json = "{}"
# create an instance of FlakyBulkModel from a JSON string
flaky_bulk_model_instance = FlakyBulkModel.from_json(json)
# print the JSON string representation of the object
print(FlakyBulkModel.to_json())

# convert the object into a dict
flaky_bulk_model_dict = flaky_bulk_model_instance.to_dict()
# create an instance of FlakyBulkModel from a dict
flaky_bulk_model_from_dict = FlakyBulkModel.from_dict(flaky_bulk_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


