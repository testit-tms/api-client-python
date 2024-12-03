# WorkItemPostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type_name** | [**WorkItemEntityTypes**](WorkItemEntityTypes.md) |  | 
**description** | **str** |  | [optional] 
**state** | [**WorkItemStates**](WorkItemStates.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**steps** | [**List[StepPostModel]**](StepPostModel.md) |  | 
**precondition_steps** | [**List[StepPostModel]**](StepPostModel.md) |  | 
**postcondition_steps** | [**List[StepPostModel]**](StepPostModel.md) |  | 
**duration** | **int** | Must be 0 for shared steps and greater than 0 for the other types of work items | 
**attributes** | **Dict[str, object]** |  | 
**tags** | [**List[TagPostModel]**](TagPostModel.md) |  | 
**attachments** | [**List[AttachmentPutModel]**](AttachmentPutModel.md) |  | [optional] 
**iterations** | [**List[IterationPutModel]**](IterationPutModel.md) |  | [optional] 
**links** | [**List[LinkPostModel]**](LinkPostModel.md) |  | 
**name** | **str** |  | 
**project_id** | **str** | This property is used to link workitem with project | 
**section_id** | **str** |  | 
**auto_tests** | [**List[AutoTestIdModel]**](AutoTestIdModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.work_item_post_model import WorkItemPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemPostModel from a JSON string
work_item_post_model_instance = WorkItemPostModel.from_json(json)
# print the JSON string representation of the object
print(WorkItemPostModel.to_json())

# convert the object into a dict
work_item_post_model_dict = work_item_post_model_instance.to_dict()
# create an instance of WorkItemPostModel from a dict
work_item_post_model_from_dict = WorkItemPostModel.from_dict(work_item_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


