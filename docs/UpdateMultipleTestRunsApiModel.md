# UpdateMultipleTestRunsApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select_model** | [**TestRunSelectApiModel**](TestRunSelectApiModel.md) | Test run selection model | 
**description** | **str** | Test run description | [optional] 
**attachment_update_scheme** | [**UpdateMultipleAttachmentsApiModel**](UpdateMultipleAttachmentsApiModel.md) | Set of attachment ids | [optional] 
**link_update_scheme** | [**UpdateMultipleLinksApiModel**](UpdateMultipleLinksApiModel.md) | Set of links | [optional] 

## Example

```python
from testit_api_client.models.update_multiple_test_runs_api_model import UpdateMultipleTestRunsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMultipleTestRunsApiModel from a JSON string
update_multiple_test_runs_api_model_instance = UpdateMultipleTestRunsApiModel.from_json(json)
# print the JSON string representation of the object
print UpdateMultipleTestRunsApiModel.to_json()

# convert the object into a dict
update_multiple_test_runs_api_model_dict = update_multiple_test_runs_api_model_instance.to_dict()
# create an instance of UpdateMultipleTestRunsApiModel from a dict
update_multiple_test_runs_api_model_from_dict = UpdateMultipleTestRunsApiModel.from_dict(update_multiple_test_runs_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


