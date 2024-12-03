# WebhooksFilterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies a webhook name to search for | [optional] 
**event_types** | [**List[WebHookEventTypeRequest]**](WebHookEventTypeRequest.md) | Specifies a webhook event types to search for | [optional] 
**methods** | [**List[RequestTypeRequest]**](RequestTypeRequest.md) | Specifies a webhook methods to search for | [optional] 
**project_ids** | **List[str]** | Specifies a webhook project IDs to search for | [optional] 

## Example

```python
from testit_api_client.models.webhooks_filter_request import WebhooksFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksFilterRequest from a JSON string
webhooks_filter_request_instance = WebhooksFilterRequest.from_json(json)
# print the JSON string representation of the object
print(WebhooksFilterRequest.to_json())

# convert the object into a dict
webhooks_filter_request_dict = webhooks_filter_request_instance.to_dict()
# create an instance of WebhooksFilterRequest from a dict
webhooks_filter_request_from_dict = WebhooksFilterRequest.from_dict(webhooks_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


