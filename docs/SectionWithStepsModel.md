# SectionWithStepsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[AttachmentModel]**](AttachmentModel.md) |  | [optional] 
**precondition_steps** | [**List[StepModel]**](StepModel.md) |  | [optional] 
**postcondition_steps** | [**List[StepModel]**](StepModel.md) |  | [optional] 
**project_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**is_deleted** | **bool** |  | 
**id** | **str** |  | 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from testit_api_client.models.section_with_steps_model import SectionWithStepsModel

# TODO update the JSON string below
json = "{}"
# create an instance of SectionWithStepsModel from a JSON string
section_with_steps_model_instance = SectionWithStepsModel.from_json(json)
# print the JSON string representation of the object
print(SectionWithStepsModel.to_json())

# convert the object into a dict
section_with_steps_model_dict = section_with_steps_model_instance.to_dict()
# create an instance of SectionWithStepsModel from a dict
section_with_steps_model_from_dict = SectionWithStepsModel.from_dict(section_with_steps_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


