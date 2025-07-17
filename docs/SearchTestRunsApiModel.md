# SearchTestRunsApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**states** | [**List[TestRunState]**](TestRunState.md) |  | [optional] 
**status_codes** | **List[str]** |  | [optional] 
**started_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**completed_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**created_by_ids** | **List[str]** |  | [optional] 
**modified_by_ids** | **List[str]** |  | [optional] 

## Example

```python
from testit_api_client.models.search_test_runs_api_model import SearchTestRunsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTestRunsApiModel from a JSON string
search_test_runs_api_model_instance = SearchTestRunsApiModel.from_json(json)
# print the JSON string representation of the object
print SearchTestRunsApiModel.to_json()

# convert the object into a dict
search_test_runs_api_model_dict = search_test_runs_api_model_instance.to_dict()
# create an instance of SearchTestRunsApiModel from a dict
search_test_runs_api_model_from_dict = SearchTestRunsApiModel.from_dict(search_test_runs_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


