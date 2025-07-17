# AttachmentChangeViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**size** | **float** |  | 

## Example

```python
from testit_api_client.models.attachment_change_view_model import AttachmentChangeViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentChangeViewModel from a JSON string
attachment_change_view_model_instance = AttachmentChangeViewModel.from_json(json)
# print the JSON string representation of the object
print AttachmentChangeViewModel.to_json()

# convert the object into a dict
attachment_change_view_model_dict = attachment_change_view_model_instance.to_dict()
# create an instance of AttachmentChangeViewModel from a dict
attachment_change_view_model_from_dict = AttachmentChangeViewModel.from_dict(attachment_change_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


