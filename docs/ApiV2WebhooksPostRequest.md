# ApiV2WebhooksPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Unique ID of the webhook project | 
**event_type** | [**WebHookEventTypeModel**](WebHookEventTypeModel.md) |  | 
**url** | **str** | Request URL of the webhook | 
**request_type** | [**RequestTypeModel**](RequestTypeModel.md) |  | 
**should_send_body** | **bool** | Indicates if the webhook sends body | 
**headers** | **{str: (str,)}** | Collection of the webhook headers | 
**query_parameters** | **{str: (str,)}** | Collection of the webhook query parameters | 
**is_enabled** | **bool** | Indicates if the webhook is active | 
**should_send_custom_body** | **bool** | Indicates if the webhook sends custom body | 
**should_replace_parameters** | **bool** | Indicates if the webhook injects parameters | 
**should_escape_parameters** | **bool** | Indicates if the webhook escapes invalid characters in parameters | 
**name** | **str** | Name of the webhook | 
**description** | **str, none_type** | Description of the webhook | [optional] 
**custom_body** | **str, none_type** | Custom body of the webhook | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


