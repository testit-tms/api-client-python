# WorkItemPutModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[AttachmentPutModel]**](AttachmentPutModel.md) |  | 
**iterations** | [**List[IterationPutModel]**](IterationPutModel.md) |  | [optional] 
**auto_tests** | [**List[AutoTestIdModel]**](AutoTestIdModel.md) |  | [optional] 
**id** | **str** |  | 
**section_id** | **str** |  | 
**description** | **str** |  | [optional] 
**state** | [**WorkItemStates**](WorkItemStates.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**steps** | [**List[StepPutModel]**](StepPutModel.md) |  | 
**precondition_steps** | [**List[StepPutModel]**](StepPutModel.md) |  | 
**postcondition_steps** | [**List[StepPutModel]**](StepPutModel.md) |  | 
**duration** | **int** |  | 
**attributes** | **Dict[str, object]** |  | 
**tags** | [**List[TagPutModel]**](TagPutModel.md) |  | 
**links** | [**List[LinkPutModel]**](LinkPutModel.md) |  | 
**name** | **str** |  | 

## Example

```python
from testit_api_client.models.work_item_put_model import WorkItemPutModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemPutModel from a JSON string
work_item_put_model_instance = WorkItemPutModel.from_json(json)
# print the JSON string representation of the object
print WorkItemPutModel.to_json()

# convert the object into a dict
work_item_put_model_dict = work_item_put_model_instance.to_dict()
# create an instance of WorkItemPutModel from a dict
work_item_put_model_from_dict = WorkItemPutModel.from_dict(work_item_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


