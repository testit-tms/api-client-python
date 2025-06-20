# WebHookLogModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_hook_name** | **str** |  | 
**event_type** | [**WebHookEventTypeModel**](WebHookEventTypeModel.md) |  | 
**web_hook_id** | **str** |  | 
**request_body** | **str** |  | [optional] 
**request_meta** | **str** |  | [optional] 
**response_status_code** | **int** |  | 
**response_body** | **str** |  | [optional] 
**response_meta** | **str** |  | [optional] 
**project_id** | **str** |  | 
**url** | **str** |  | 
**request_type** | [**RequestTypeModel**](RequestTypeModel.md) |  | 
**created_date** | **datetime** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 

## Example

```python
from testit_api_client.models.web_hook_log_model import WebHookLogModel

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookLogModel from a JSON string
web_hook_log_model_instance = WebHookLogModel.from_json(json)
# print the JSON string representation of the object
print(WebHookLogModel.to_json())

# convert the object into a dict
web_hook_log_model_dict = web_hook_log_model_instance.to_dict()
# create an instance of WebHookLogModel from a dict
web_hook_log_model_from_dict = WebHookLogModel.from_dict(web_hook_log_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


