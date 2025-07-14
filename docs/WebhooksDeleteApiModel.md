# WebhooksDeleteApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**WebhooksDeleteFilterApiModel**](WebhooksDeleteFilterApiModel.md) |  | 
**extractor** | [**WebhooksExtractionApiModel**](WebhooksExtractionApiModel.md) |  | 

## Example

```python
from testit_api_client.models.webhooks_delete_api_model import WebhooksDeleteApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksDeleteApiModel from a JSON string
webhooks_delete_api_model_instance = WebhooksDeleteApiModel.from_json(json)
# print the JSON string representation of the object
print WebhooksDeleteApiModel.to_json()

# convert the object into a dict
webhooks_delete_api_model_dict = webhooks_delete_api_model_instance.to_dict()
# create an instance of WebhooksDeleteApiModel from a dict
webhooks_delete_api_model_from_dict = WebhooksDeleteApiModel.from_dict(webhooks_delete_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


