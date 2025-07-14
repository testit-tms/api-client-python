# AutoTestBulkDeleteApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_count** | **int** |  | 
**in_progress_count** | **int** |  | 

## Example

```python
from testit_api_client.models.auto_test_bulk_delete_api_result import AutoTestBulkDeleteApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestBulkDeleteApiResult from a JSON string
auto_test_bulk_delete_api_result_instance = AutoTestBulkDeleteApiResult.from_json(json)
# print the JSON string representation of the object
print AutoTestBulkDeleteApiResult.to_json()

# convert the object into a dict
auto_test_bulk_delete_api_result_dict = auto_test_bulk_delete_api_result_instance.to_dict()
# create an instance of AutoTestBulkDeleteApiResult from a dict
auto_test_bulk_delete_api_result_from_dict = AutoTestBulkDeleteApiResult.from_dict(auto_test_bulk_delete_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


