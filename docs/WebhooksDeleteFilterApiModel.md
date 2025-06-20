# WebhooksDeleteFilterApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies a webhook name to search for | [optional] 
**event_types** | [**List[WebHookEventTypeRequest]**](WebHookEventTypeRequest.md) | Specifies a webhook event types to search for | [optional] 
**methods** | [**List[RequestTypeApiModel]**](RequestTypeApiModel.md) | Specifies a webhook methods to search for | [optional] 
**project_ids** | **List[str]** | Specifies a webhook project IDs to search for | [optional] 
**is_enabled** | **bool** | Specifies a webhook deleted status to search for | [optional] 

## Example

```python
from testit_api_client.models.webhooks_delete_filter_api_model import WebhooksDeleteFilterApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksDeleteFilterApiModel from a JSON string
webhooks_delete_filter_api_model_instance = WebhooksDeleteFilterApiModel.from_json(json)
# print the JSON string representation of the object
print(WebhooksDeleteFilterApiModel.to_json())

# convert the object into a dict
webhooks_delete_filter_api_model_dict = webhooks_delete_filter_api_model_instance.to_dict()
# create an instance of WebhooksDeleteFilterApiModel from a dict
webhooks_delete_filter_api_model_from_dict = WebhooksDeleteFilterApiModel.from_dict(webhooks_delete_filter_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


