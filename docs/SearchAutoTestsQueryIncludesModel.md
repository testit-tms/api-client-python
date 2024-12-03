# SearchAutoTestsQueryIncludesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_steps** | **bool** | If autotest steps will be included | 
**include_links** | **bool** | If autotest links will be included | 
**include_labels** | **bool** | If autotest labels will be included | 

## Example

```python
from testit_api_client.models.search_auto_tests_query_includes_model import SearchAutoTestsQueryIncludesModel

# TODO update the JSON string below
json = "{}"
# create an instance of SearchAutoTestsQueryIncludesModel from a JSON string
search_auto_tests_query_includes_model_instance = SearchAutoTestsQueryIncludesModel.from_json(json)
# print the JSON string representation of the object
print(SearchAutoTestsQueryIncludesModel.to_json())

# convert the object into a dict
search_auto_tests_query_includes_model_dict = search_auto_tests_query_includes_model_instance.to_dict()
# create an instance of SearchAutoTestsQueryIncludesModel from a dict
search_auto_tests_query_includes_model_from_dict = SearchAutoTestsQueryIncludesModel.from_dict(search_auto_tests_query_includes_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


