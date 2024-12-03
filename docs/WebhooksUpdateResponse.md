# WebhooksUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_count** | **int** |  | 

## Example

```python
from testit_api_client.models.webhooks_update_response import WebhooksUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksUpdateResponse from a JSON string
webhooks_update_response_instance = WebhooksUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(WebhooksUpdateResponse.to_json())

# convert the object into a dict
webhooks_update_response_dict = webhooks_update_response_instance.to_dict()
# create an instance of WebhooksUpdateResponse from a dict
webhooks_update_response_from_dict = WebhooksUpdateResponse.from_dict(webhooks_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


