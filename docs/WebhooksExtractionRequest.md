# WebhooksExtractionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**GuidExtractionModel**](GuidExtractionModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.webhooks_extraction_request import WebhooksExtractionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksExtractionRequest from a JSON string
webhooks_extraction_request_instance = WebhooksExtractionRequest.from_json(json)
# print the JSON string representation of the object
print(WebhooksExtractionRequest.to_json())

# convert the object into a dict
webhooks_extraction_request_dict = webhooks_extraction_request_instance.to_dict()
# create an instance of WebhooksExtractionRequest from a dict
webhooks_extraction_request_from_dict = WebhooksExtractionRequest.from_dict(webhooks_extraction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


