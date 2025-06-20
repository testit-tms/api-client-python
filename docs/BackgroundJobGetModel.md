# BackgroundJobGetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**job_id** | **str** |  | 
**job_type** | [**BackgroundJobType**](BackgroundJobType.md) |  | 
**state** | [**BackgroundJobState**](BackgroundJobState.md) |  | 
**is_deleted** | **bool** |  | 
**progress** | **int** |  | 
**created_date** | **datetime** |  | 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**error** | **str** |  | [optional] 
**attachments** | [**List[BackgroundJobAttachmentModel]**](BackgroundJobAttachmentModel.md) |  | 

## Example

```python
from testit_api_client.models.background_job_get_model import BackgroundJobGetModel

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundJobGetModel from a JSON string
background_job_get_model_instance = BackgroundJobGetModel.from_json(json)
# print the JSON string representation of the object
print BackgroundJobGetModel.to_json()

# convert the object into a dict
background_job_get_model_dict = background_job_get_model_instance.to_dict()
# create an instance of BackgroundJobGetModel from a dict
background_job_get_model_from_dict = BackgroundJobGetModel.from_dict(background_job_get_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


