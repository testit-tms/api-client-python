# AttachmentUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the attachment | 

## Example

```python
from testit_api_client.models.attachment_update_request import AttachmentUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentUpdateRequest from a JSON string
attachment_update_request_instance = AttachmentUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AttachmentUpdateRequest.to_json())

# convert the object into a dict
attachment_update_request_dict = attachment_update_request_instance.to_dict()
# create an instance of AttachmentUpdateRequest from a dict
attachment_update_request_from_dict = AttachmentUpdateRequest.from_dict(attachment_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


