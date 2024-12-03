# AutotestsSelectModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**AutotestFilterModel**](AutotestFilterModel.md) | Object containing different filters to adjust search | 
**includes** | [**SearchAutoTestsQueryIncludesModel**](SearchAutoTestsQueryIncludesModel.md) | Object specifying data to be included | 

## Example

```python
from testit_api_client.models.autotests_select_model import AutotestsSelectModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutotestsSelectModel from a JSON string
autotests_select_model_instance = AutotestsSelectModel.from_json(json)
# print the JSON string representation of the object
print(AutotestsSelectModel.to_json())

# convert the object into a dict
autotests_select_model_dict = autotests_select_model_instance.to_dict()
# create an instance of AutotestsSelectModel from a dict
autotests_select_model_from_dict = AutotestsSelectModel.from_dict(autotests_select_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


