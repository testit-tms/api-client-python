# WorkItemGroupGetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select_model** | [**WorkItemLocalSelectModel**](WorkItemLocalSelectModel.md) | Model containing options to filter work items | [optional] 
**group_type** | [**WorkItemGroupType**](WorkItemGroupType.md) |  | 
**custom_attribute_id** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.work_item_group_get_model import WorkItemGroupGetModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemGroupGetModel from a JSON string
work_item_group_get_model_instance = WorkItemGroupGetModel.from_json(json)
# print the JSON string representation of the object
print WorkItemGroupGetModel.to_json()

# convert the object into a dict
work_item_group_get_model_dict = work_item_group_get_model_instance.to_dict()
# create an instance of WorkItemGroupGetModel from a dict
work_item_group_get_model_from_dict = WorkItemGroupGetModel.from_dict(work_item_group_get_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


