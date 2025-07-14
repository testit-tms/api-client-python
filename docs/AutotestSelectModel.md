# AutoTestSelectModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**AutoTestFilterModel**](AutoTestFilterModel.md) |  | 
**extraction_model** | [**AutoTestsExtractionModel**](AutoTestsExtractionModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.auto_test_select_model import AutoTestSelectModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestSelectModel from a JSON string
auto_test_select_model_instance = AutoTestSelectModel.from_json(json)
# print the JSON string representation of the object
print AutoTestSelectModel.to_json()

# convert the object into a dict
auto_test_select_model_dict = auto_test_select_model_instance.to_dict()
# create an instance of AutoTestSelectModel from a dict
auto_test_select_model_from_dict = AutoTestSelectModel.from_dict(auto_test_select_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


