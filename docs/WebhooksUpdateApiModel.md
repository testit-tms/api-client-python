# WebhooksUpdateApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**WebhooksFilterApiModel**](WebhooksFilterApiModel.md) |  | 
**model** | [**WebhookBulkUpdateApiModel**](WebhookBulkUpdateApiModel.md) |  | 
**extractor** | [**WebhooksExtractionApiModel**](WebhooksExtractionApiModel.md) |  | 

## Example

```python
from testit_api_client.models.webhooks_update_api_model import WebhooksUpdateApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksUpdateApiModel from a JSON string
webhooks_update_api_model_instance = WebhooksUpdateApiModel.from_json(json)
# print the JSON string representation of the object
print(WebhooksUpdateApiModel.to_json())

# convert the object into a dict
webhooks_update_api_model_dict = webhooks_update_api_model_instance.to_dict()
# create an instance of WebhooksUpdateApiModel from a dict
webhooks_update_api_model_from_dict = WebhooksUpdateApiModel.from_dict(webhooks_update_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


