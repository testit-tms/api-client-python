# BackgroundJobAttachmentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**size** | **float** |  | 

## Example

```python
from testit_api_client.models.background_job_attachment_model import BackgroundJobAttachmentModel

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundJobAttachmentModel from a JSON string
background_job_attachment_model_instance = BackgroundJobAttachmentModel.from_json(json)
# print the JSON string representation of the object
print(BackgroundJobAttachmentModel.to_json())

# convert the object into a dict
background_job_attachment_model_dict = background_job_attachment_model_instance.to_dict()
# create an instance of BackgroundJobAttachmentModel from a dict
background_job_attachment_model_from_dict = BackgroundJobAttachmentModel.from_dict(background_job_attachment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


