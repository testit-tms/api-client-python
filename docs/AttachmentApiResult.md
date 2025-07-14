# AttachmentApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the attachment | 
**file_id** | **str** | Unique ID of the attachment file | 
**type** | **str** | MIME type of the attachment | 
**size** | **float** | Size in bytes of the attachment file | 
**created_date** | **datetime** | Creation date of the attachment | 
**modified_date** | **datetime** | Last modification date of the attachment | [optional] 
**created_by_id** | **str** | Unique ID of the attachment creator | 
**modified_by_id** | **str** | Unique ID of the attachment last editor | [optional] 
**name** | **str** | Name of the attachment file | 

## Example

```python
from testit_api_client.models.attachment_api_result import AttachmentApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentApiResult from a JSON string
attachment_api_result_instance = AttachmentApiResult.from_json(json)
# print the JSON string representation of the object
print AttachmentApiResult.to_json()

# convert the object into a dict
attachment_api_result_dict = attachment_api_result_instance.to_dict()
# create an instance of AttachmentApiResult from a dict
attachment_api_result_from_dict = AttachmentApiResult.from_dict(attachment_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


