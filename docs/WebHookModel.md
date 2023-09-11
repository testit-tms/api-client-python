# WebHookModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**WebHookEventTypeModel**](WebHookEventTypeModel.md) |  | 
**request_type** | [**RequestTypeModel**](RequestTypeModel.md) |  | 
**should_send_body** | **bool** | Indicates if the webhook sends body | 
**is_enabled** | **bool** | Indicates if the webhook is active | 
**should_send_custom_body** | **bool** | Indicates if the webhook sends custom body | 
**should_replace_parameters** | **bool** | Indicates if the webhook injects parameters | 
**should_escape_parameters** | **bool** | Indicates if the webhook escapes invalid characters in parameters | 
**created_date** | **datetime** | Creation date of the webhook | 
**created_by_id** | **str** | Unique ID of user who created the webhook | 
**project_id** | **str** | Unique ID of project where the webhook is located | 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 
**name** | **str, none_type** | Name of the webhook | [optional] 
**description** | **str, none_type** | Description of the webhook | [optional] 
**url** | **str, none_type** | Url to which the webhook sends request | [optional] 
**headers** | **{str: (str, none_type)}, none_type** | Collection of headers which the webhook sends | [optional] 
**query_parameters** | **{str: (str, none_type)}, none_type** | Collection of query parameters which the webhook sends | [optional] 
**custom_body** | **str, none_type** | Custom body of the webhook | [optional] 
**custom_body_media_type** | **str, none_type** | MIME type of body of the webhook | [optional] 
**modified_date** | **datetime, none_type** | Last modification date of the webhook | [optional] 
**modified_by_id** | **str, none_type** | Unique ID of user who modified the webhook last time | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


