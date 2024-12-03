# WebhooksUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**WebhooksFilterRequest**](WebhooksFilterRequest.md) |  | 
**model** | [**WebhookBulkUpdateApiModel**](WebhookBulkUpdateApiModel.md) |  | 
**extractor** | [**WebhooksExtractionRequest**](WebhooksExtractionRequest.md) |  | 

## Example

```python
from testit_api_client.models.webhooks_update_request import WebhooksUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksUpdateRequest from a JSON string
webhooks_update_request_instance = WebhooksUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WebhooksUpdateRequest.to_json())

# convert the object into a dict
webhooks_update_request_dict = webhooks_update_request_instance.to_dict()
# create an instance of WebhooksUpdateRequest from a dict
webhooks_update_request_from_dict = WebhooksUpdateRequest.from_dict(webhooks_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


