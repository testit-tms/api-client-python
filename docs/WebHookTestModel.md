# WebHookTestModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | [**RequestTypeModel**](RequestTypeModel.md) | Request method of the webhook | 
**url** | **str** | Request URL of the webhook | 

## Example

```python
from testit_api_client.models.web_hook_test_model import WebHookTestModel

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookTestModel from a JSON string
web_hook_test_model_instance = WebHookTestModel.from_json(json)
# print the JSON string representation of the object
print WebHookTestModel.to_json()

# convert the object into a dict
web_hook_test_model_dict = web_hook_test_model_instance.to_dict()
# create an instance of WebHookTestModel from a dict
web_hook_test_model_from_dict = WebHookTestModel.from_dict(web_hook_test_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


