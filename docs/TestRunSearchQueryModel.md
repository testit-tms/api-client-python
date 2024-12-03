# TestRunSearchQueryModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**states** | [**List[TestRunState]**](TestRunState.md) |  | [optional] 
**started_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**completed_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**created_by_ids** | **List[str]** |  | [optional] 
**modified_by_ids** | **List[str]** |  | [optional] 

## Example

```python
from testit_api_client.models.test_run_search_query_model import TestRunSearchQueryModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunSearchQueryModel from a JSON string
test_run_search_query_model_instance = TestRunSearchQueryModel.from_json(json)
# print the JSON string representation of the object
print(TestRunSearchQueryModel.to_json())

# convert the object into a dict
test_run_search_query_model_dict = test_run_search_query_model_instance.to_dict()
# create an instance of TestRunSearchQueryModel from a dict
test_run_search_query_model_from_dict = TestRunSearchQueryModel.from_dict(test_run_search_query_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


