# WebhooksDeleteFilterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies a webhook name to search for | [optional] 
**event_types** | [**List[WebHookEventTypeRequest]**](WebHookEventTypeRequest.md) | Specifies a webhook event types to search for | [optional] 
**methods** | [**List[RequestTypeRequest]**](RequestTypeRequest.md) | Specifies a webhook methods to search for | [optional] 
**project_ids** | **List[str]** | Specifies a webhook project IDs to search for | [optional] 
**is_enabled** | **bool** | Specifies a webhook deleted status to search for | [optional] 

## Example

```python
from testit_api_client.models.webhooks_delete_filter_request import WebhooksDeleteFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksDeleteFilterRequest from a JSON string
webhooks_delete_filter_request_instance = WebhooksDeleteFilterRequest.from_json(json)
# print the JSON string representation of the object
print(WebhooksDeleteFilterRequest.to_json())

# convert the object into a dict
webhooks_delete_filter_request_dict = webhooks_delete_filter_request_instance.to_dict()
# create an instance of WebhooksDeleteFilterRequest from a dict
webhooks_delete_filter_request_from_dict = WebhooksDeleteFilterRequest.from_dict(webhooks_delete_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


