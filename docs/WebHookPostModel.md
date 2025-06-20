# WebHookPostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Unique ID of the webhook project | 
**event_type** | [**WebHookEventTypeModel**](WebHookEventTypeModel.md) | Type of event which triggers the webhook | 
**description** | **str** | Description of the webhook | [optional] 
**url** | **str** | Request URL of the webhook | 
**request_type** | [**RequestTypeModel**](RequestTypeModel.md) | Request method of the webhook | 
**should_send_body** | **bool** | Indicates if the webhook sends body | 
**headers** | **Dict[str, str]** | Collection of the webhook headers | 
**query_parameters** | **Dict[str, str]** | Collection of the webhook query parameters | 
**is_enabled** | **bool** | Indicates if the webhook is active | 
**should_send_custom_body** | **bool** | Indicates if the webhook sends custom body | 
**custom_body** | **str** | Custom body of the webhook | [optional] 
**should_replace_parameters** | **bool** | Indicates if the webhook injects parameters | 
**should_escape_parameters** | **bool** | Indicates if the webhook escapes invalid characters in parameters | 
**name** | **str** | Name of the webhook | 

## Example

```python
from testit_api_client.models.web_hook_post_model import WebHookPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookPostModel from a JSON string
web_hook_post_model_instance = WebHookPostModel.from_json(json)
# print the JSON string representation of the object
print(WebHookPostModel.to_json())

# convert the object into a dict
web_hook_post_model_dict = web_hook_post_model_instance.to_dict()
# create an instance of WebHookPostModel from a dict
web_hook_post_model_from_dict = WebHookPostModel.from_dict(web_hook_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


