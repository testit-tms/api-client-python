# WebhooksDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**WebhooksDeleteFilterRequest**](WebhooksDeleteFilterRequest.md) |  | 
**extractor** | [**WebhooksExtractionRequest**](WebhooksExtractionRequest.md) |  | 

## Example

```python
from testit_api_client.models.webhooks_delete_request import WebhooksDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksDeleteRequest from a JSON string
webhooks_delete_request_instance = WebhooksDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(WebhooksDeleteRequest.to_json())

# convert the object into a dict
webhooks_delete_request_dict = webhooks_delete_request_instance.to_dict()
# create an instance of WebhooksDeleteRequest from a dict
webhooks_delete_request_from_dict = WebhooksDeleteRequest.from_dict(webhooks_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


