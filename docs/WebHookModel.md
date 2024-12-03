# WebHookModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the webhook | 
**event_type** | [**WebHookEventTypeModel**](WebHookEventTypeModel.md) | Type of event which triggers the webhook | 
**description** | **str** | Description of the webhook | [optional] 
**url** | **str** | Url to which the webhook sends request | 
**request_type** | [**RequestTypeModel**](RequestTypeModel.md) | Method which the webhook uses | 
**should_send_body** | **bool** | Indicates if the webhook sends body | 
**headers** | **Dict[str, str]** | Collection of headers which the webhook sends | [optional] 
**query_parameters** | **Dict[str, str]** | Collection of query parameters which the webhook sends | [optional] 
**is_enabled** | **bool** | Indicates if the webhook is active | 
**should_send_custom_body** | **bool** | Indicates if the webhook sends custom body | 
**custom_body** | **str** | Custom body of the webhook | [optional] 
**custom_body_media_type** | **str** | MIME type of body of the webhook | [optional] 
**should_replace_parameters** | **bool** | Indicates if the webhook injects parameters | 
**should_escape_parameters** | **bool** | Indicates if the webhook escapes invalid characters in parameters | 
**created_date** | **datetime** | Creation date of the webhook | 
**created_by_id** | **str** | Unique ID of user who created the webhook | 
**modified_date** | **datetime** | Last modification date of the webhook | [optional] 
**modified_by_id** | **str** | Unique ID of user who modified the webhook last time | [optional] 
**project_id** | **str** | Unique ID of project where the webhook is located | 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 

## Example

```python
from testit_api_client.models.web_hook_model import WebHookModel

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookModel from a JSON string
web_hook_model_instance = WebHookModel.from_json(json)
# print the JSON string representation of the object
print(WebHookModel.to_json())

# convert the object into a dict
web_hook_model_dict = web_hook_model_instance.to_dict()
# create an instance of WebHookModel from a dict
web_hook_model_from_dict = WebHookModel.from_dict(web_hook_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


