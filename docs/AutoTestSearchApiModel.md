# AutoTestSearchApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**AutoTestFilterApiModel**](AutoTestFilterApiModel.md) | Object containing different filters to adjust search | [optional] 
**includes** | [**AutoTestSearchIncludeApiModel**](AutoTestSearchIncludeApiModel.md) | Object specifying data to be included | [optional] 

## Example

```python
from testit_api_client.models.auto_test_search_api_model import AutoTestSearchApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestSearchApiModel from a JSON string
auto_test_search_api_model_instance = AutoTestSearchApiModel.from_json(json)
# print the JSON string representation of the object
print(AutoTestSearchApiModel.to_json())

# convert the object into a dict
auto_test_search_api_model_dict = auto_test_search_api_model_instance.to_dict()
# create an instance of AutoTestSearchApiModel from a dict
auto_test_search_api_model_from_dict = AutoTestSearchApiModel.from_dict(auto_test_search_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


