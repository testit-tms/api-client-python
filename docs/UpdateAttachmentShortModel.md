# UpdateAttachmentShortModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ActionUpdate**](ActionUpdate.md) |  | 
**attachment_ids** | **List[str]** |  | [optional] 

## Example

```python
from testit_api_client.models.update_attachment_short_model import UpdateAttachmentShortModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAttachmentShortModel from a JSON string
update_attachment_short_model_instance = UpdateAttachmentShortModel.from_json(json)
# print the JSON string representation of the object
print(UpdateAttachmentShortModel.to_json())

# convert the object into a dict
update_attachment_short_model_dict = update_attachment_short_model_instance.to_dict()
# create an instance of UpdateAttachmentShortModel from a dict
update_attachment_short_model_from_dict = UpdateAttachmentShortModel.from_dict(update_attachment_short_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


