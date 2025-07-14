# SectionPutModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**project_id** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**precondition_steps** | [**List[StepPutModel]**](StepPutModel.md) |  | [optional] 
**postcondition_steps** | [**List[StepPutModel]**](StepPutModel.md) |  | [optional] 
**attachments** | [**List[AttachmentPutModel]**](AttachmentPutModel.md) |  | 

## Example

```python
from testit_api_client.models.section_put_model import SectionPutModel

# TODO update the JSON string below
json = "{}"
# create an instance of SectionPutModel from a JSON string
section_put_model_instance = SectionPutModel.from_json(json)
# print the JSON string representation of the object
print SectionPutModel.to_json()

# convert the object into a dict
section_put_model_dict = section_put_model_instance.to_dict()
# create an instance of SectionPutModel from a dict
section_put_model_from_dict = SectionPutModel.from_dict(section_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


