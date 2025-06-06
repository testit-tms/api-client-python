# WorkItemModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_id** | **str** | used for versioning changes in workitem | 
**median_duration** | **int** | used for getting a median duration of all autotests related to this workitem | 
**is_deleted** | **bool** |  | 
**project_id** | **str** |  | 
**entity_type_name** | [**WorkItemEntityTypes**](WorkItemEntityTypes.md) |  | 
**is_automated** | **bool** |  | 
**auto_tests** | [**List[AutoTestModel]**](AutoTestModel.md) |  | [optional] 
**attachments** | [**List[AttachmentModel]**](AttachmentModel.md) |  | [optional] 
**section_precondition_steps** | [**List[StepModel]**](StepModel.md) |  | [optional] 
**section_postcondition_steps** | [**List[StepModel]**](StepModel.md) |  | [optional] 
**version_number** | **int** | used for define chronology of workitem state in each version | 
**iterations** | [**List[IterationModel]**](IterationModel.md) |  | [optional] 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**global_id** | **int** |  | 
**id** | **str** |  | 
**section_id** | **str** |  | 
**description** | **str** |  | [optional] 
**state** | [**WorkItemStates**](WorkItemStates.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**source_type** | [**WorkItemSourceTypeModel**](WorkItemSourceTypeModel.md) |  | 
**steps** | [**List[StepModel]**](StepModel.md) |  | 
**precondition_steps** | [**List[StepModel]**](StepModel.md) |  | 
**postcondition_steps** | [**List[StepModel]**](StepModel.md) |  | 
**duration** | **int** |  | 
**attributes** | **Dict[str, object]** |  | 
**tags** | [**List[TagModel]**](TagModel.md) |  | 
**links** | [**List[LinkModel]**](LinkModel.md) |  | 
**name** | **str** |  | 

## Example

```python
from testit_api_client.models.work_item_model import WorkItemModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemModel from a JSON string
work_item_model_instance = WorkItemModel.from_json(json)
# print the JSON string representation of the object
print(WorkItemModel.to_json())

# convert the object into a dict
work_item_model_dict = work_item_model_instance.to_dict()
# create an instance of WorkItemModel from a dict
work_item_model_from_dict = WorkItemModel.from_dict(work_item_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


