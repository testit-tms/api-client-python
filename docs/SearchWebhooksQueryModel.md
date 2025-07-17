# SearchWebhooksQueryModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies a webhook name to search for | [optional] 
**event_types** | [**List[WebHookEventTypeModel]**](WebHookEventTypeModel.md) | Specifies a webhook event types to search for | [optional] 
**methods** | [**List[RequestTypeModel]**](RequestTypeModel.md) | Specifies a webhook methods to search for | [optional] 
**project_ids** | **List[str]** | Specifies a webhook project IDs to search for | [optional] 
**is_enabled** | **bool** | Specifies a webhook deleted status to search for | [optional] 

## Example

```python
from testit_api_client.models.search_webhooks_query_model import SearchWebhooksQueryModel

# TODO update the JSON string below
json = "{}"
# create an instance of SearchWebhooksQueryModel from a JSON string
search_webhooks_query_model_instance = SearchWebhooksQueryModel.from_json(json)
# print the JSON string representation of the object
print SearchWebhooksQueryModel.to_json()

# convert the object into a dict
search_webhooks_query_model_dict = search_webhooks_query_model_instance.to_dict()
# create an instance of SearchWebhooksQueryModel from a dict
search_webhooks_query_model_from_dict = SearchWebhooksQueryModel.from_dict(search_webhooks_query_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


