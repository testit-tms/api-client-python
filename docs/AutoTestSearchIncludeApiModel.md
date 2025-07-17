# AutoTestSearchIncludeApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_steps** | **bool** | If autotest steps will be included | [optional] 
**include_links** | **bool** | If autotest links will be included | [optional] 
**include_labels** | **bool** | If autotest labels will be included | [optional] 

## Example

```python
from testit_api_client.models.auto_test_search_include_api_model import AutoTestSearchIncludeApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestSearchIncludeApiModel from a JSON string
auto_test_search_include_api_model_instance = AutoTestSearchIncludeApiModel.from_json(json)
# print the JSON string representation of the object
print AutoTestSearchIncludeApiModel.to_json()

# convert the object into a dict
auto_test_search_include_api_model_dict = auto_test_search_include_api_model_instance.to_dict()
# create an instance of AutoTestSearchIncludeApiModel from a dict
auto_test_search_include_api_model_from_dict = AutoTestSearchIncludeApiModel.from_dict(auto_test_search_include_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


