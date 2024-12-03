# SharedStepReferenceModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**global_id** | **int** |  | 
**name** | **str** |  | 
**entity_type_name** | **str** |  | 
**has_this_shared_step_as_step** | **bool** |  | 
**has_this_shared_step_as_precondition** | **bool** |  | 
**has_this_shared_step_as_postcondition** | **bool** |  | 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**state** | **str** |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**is_deleted** | **bool** |  | 
**version_id** | **str** | used for versioning changes in workitem | 
**is_automated** | **bool** |  | 
**section_id** | **str** |  | 
**tags** | [**List[TagModel]**](TagModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.shared_step_reference_model import SharedStepReferenceModel

# TODO update the JSON string below
json = "{}"
# create an instance of SharedStepReferenceModel from a JSON string
shared_step_reference_model_instance = SharedStepReferenceModel.from_json(json)
# print the JSON string representation of the object
print(SharedStepReferenceModel.to_json())

# convert the object into a dict
shared_step_reference_model_dict = shared_step_reference_model_instance.to_dict()
# create an instance of SharedStepReferenceModel from a dict
shared_step_reference_model_from_dict = SharedStepReferenceModel.from_dict(shared_step_reference_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


