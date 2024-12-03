# AutotestSelectModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**AutotestFilterModel**](AutotestFilterModel.md) |  | 
**extraction_model** | [**AutotestsExtractionModel**](AutotestsExtractionModel.md) |  | 

## Example

```python
from testit_api_client.models.autotest_select_model import AutotestSelectModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutotestSelectModel from a JSON string
autotest_select_model_instance = AutotestSelectModel.from_json(json)
# print the JSON string representation of the object
print(AutotestSelectModel.to_json())

# convert the object into a dict
autotest_select_model_dict = autotest_select_model_instance.to_dict()
# create an instance of AutotestSelectModel from a dict
autotest_select_model_from_dict = AutotestSelectModel.from_dict(autotest_select_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


