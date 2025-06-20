# LastTestResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**test_run_id** | **str** |  | 
**auto_test_id** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**links** | [**List[LinkModel]**](LinkModel.md) |  | [optional] 
**work_item_version_id** | **str** |  | 
**attachments** | [**List[AttachmentModel]**](AttachmentModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.last_test_result_model import LastTestResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of LastTestResultModel from a JSON string
last_test_result_model_instance = LastTestResultModel.from_json(json)
# print the JSON string representation of the object
print(LastTestResultModel.to_json())

# convert the object into a dict
last_test_result_model_dict = last_test_result_model_instance.to_dict()
# create an instance of LastTestResultModel from a dict
last_test_result_model_from_dict = LastTestResultModel.from_dict(last_test_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


