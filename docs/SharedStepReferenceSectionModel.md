# SharedStepReferenceSectionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**has_this_shared_step_as_precondition** | **bool** |  | 
**has_this_shared_step_as_postcondition** | **bool** |  | 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**is_deleted** | **bool** |  | 

## Example

```python
from testit_api_client.models.shared_step_reference_section_model import SharedStepReferenceSectionModel

# TODO update the JSON string below
json = "{}"
# create an instance of SharedStepReferenceSectionModel from a JSON string
shared_step_reference_section_model_instance = SharedStepReferenceSectionModel.from_json(json)
# print the JSON string representation of the object
print(SharedStepReferenceSectionModel.to_json())

# convert the object into a dict
shared_step_reference_section_model_dict = shared_step_reference_section_model_instance.to_dict()
# create an instance of SharedStepReferenceSectionModel from a dict
shared_step_reference_section_model_from_dict = SharedStepReferenceSectionModel.from_dict(shared_step_reference_section_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


