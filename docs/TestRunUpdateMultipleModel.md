# TestRunUpdateMultipleModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select_model** | [**TestRunSelectModel**](TestRunSelectModel.md) | Model containing options to filter test runs | 
**description** | **str** |  | [optional] 
**attachment_update_scheme** | [**UpdateAttachmentShortModel**](UpdateAttachmentShortModel.md) |  | 
**link_update_scheme** | [**UpdateLinkShortModel**](UpdateLinkShortModel.md) |  | 

## Example

```python
from testit_api_client.models.test_run_update_multiple_model import TestRunUpdateMultipleModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunUpdateMultipleModel from a JSON string
test_run_update_multiple_model_instance = TestRunUpdateMultipleModel.from_json(json)
# print the JSON string representation of the object
print(TestRunUpdateMultipleModel.to_json())

# convert the object into a dict
test_run_update_multiple_model_dict = test_run_update_multiple_model_instance.to_dict()
# create an instance of TestRunUpdateMultipleModel from a dict
test_run_update_multiple_model_from_dict = TestRunUpdateMultipleModel.from_dict(test_run_update_multiple_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


