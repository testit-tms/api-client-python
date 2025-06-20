# UpdateEmptyTestRunApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Test run unique identifier | 
**name** | **str** | Test run name | 
**description** | **str** | Test run description | [optional] 
**launch_source** | **str** | Test run launch source              Once launch source is specified it cannot be updated | [optional] 
**attachments** | [**List[AssignAttachmentApiModel]**](AssignAttachmentApiModel.md) | Collection of attachments related to the test run | [optional] 
**links** | [**List[UpdateLinkApiModel]**](UpdateLinkApiModel.md) | Collection of links related to the test run | [optional] 

## Example

```python
from testit_api_client.models.update_empty_test_run_api_model import UpdateEmptyTestRunApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEmptyTestRunApiModel from a JSON string
update_empty_test_run_api_model_instance = UpdateEmptyTestRunApiModel.from_json(json)
# print the JSON string representation of the object
print UpdateEmptyTestRunApiModel.to_json()

# convert the object into a dict
update_empty_test_run_api_model_dict = update_empty_test_run_api_model_instance.to_dict()
# create an instance of UpdateEmptyTestRunApiModel from a dict
update_empty_test_run_api_model_from_dict = UpdateEmptyTestRunApiModel.from_dict(update_empty_test_run_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


