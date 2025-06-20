# WorkItemGroupModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **object** |  | [optional] 
**size** | **int** |  | 
**work_items** | [**List[WorkItemShortModel]**](WorkItemShortModel.md) |  | 

## Example

```python
from testit_api_client.models.work_item_group_model import WorkItemGroupModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemGroupModel from a JSON string
work_item_group_model_instance = WorkItemGroupModel.from_json(json)
# print the JSON string representation of the object
print WorkItemGroupModel.to_json()

# convert the object into a dict
work_item_group_model_dict = work_item_group_model_instance.to_dict()
# create an instance of WorkItemGroupModel from a dict
work_item_group_model_from_dict = WorkItemGroupModel.from_dict(work_item_group_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


