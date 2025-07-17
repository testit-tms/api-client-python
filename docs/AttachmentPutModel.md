# AttachmentPutModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the attachment | 

## Example

```python
from testit_api_client.models.attachment_put_model import AttachmentPutModel

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentPutModel from a JSON string
attachment_put_model_instance = AttachmentPutModel.from_json(json)
# print the JSON string representation of the object
print AttachmentPutModel.to_json()

# convert the object into a dict
attachment_put_model_dict = attachment_put_model_instance.to_dict()
# create an instance of AttachmentPutModel from a dict
attachment_put_model_from_dict = AttachmentPutModel.from_dict(attachment_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


