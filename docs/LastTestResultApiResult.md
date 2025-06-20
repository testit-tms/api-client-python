# LastTestResultApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**test_run_id** | **str** |  | 
**auto_test_id** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**links** | [**List[LinkApiResult]**](LinkApiResult.md) |  | 
**work_item_version_id** | **str** |  | [optional] 
**attachments** | [**List[AttachmentApiResult]**](AttachmentApiResult.md) |  | 

## Example

```python
from testit_api_client.models.last_test_result_api_result import LastTestResultApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of LastTestResultApiResult from a JSON string
last_test_result_api_result_instance = LastTestResultApiResult.from_json(json)
# print the JSON string representation of the object
print LastTestResultApiResult.to_json()

# convert the object into a dict
last_test_result_api_result_dict = last_test_result_api_result_instance.to_dict()
# create an instance of LastTestResultApiResult from a dict
last_test_result_api_result_from_dict = LastTestResultApiResult.from_dict(last_test_result_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


