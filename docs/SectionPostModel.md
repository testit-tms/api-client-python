# SectionPostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**project_id** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**precondition_steps** | [**List[StepPostModel]**](StepPostModel.md) |  | [optional] 
**postcondition_steps** | [**List[StepPostModel]**](StepPostModel.md) |  | [optional] 
**attachments** | [**List[AttachmentPutModel]**](AttachmentPutModel.md) |  | 

## Example

```python
from testit_api_client.models.section_post_model import SectionPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of SectionPostModel from a JSON string
section_post_model_instance = SectionPostModel.from_json(json)
# print the JSON string representation of the object
print(SectionPostModel.to_json())

# convert the object into a dict
section_post_model_dict = section_post_model_instance.to_dict()
# create an instance of SectionPostModel from a dict
section_post_model_from_dict = SectionPostModel.from_dict(section_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


