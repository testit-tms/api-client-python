# WorkItemIdModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Used for search WorkItem. Internal identifier has a Guid data format. Global identifier has an integer data format | 

## Example

```python
from testit_api_client.models.work_item_id_model import WorkItemIdModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemIdModel from a JSON string
work_item_id_model_instance = WorkItemIdModel.from_json(json)
# print the JSON string representation of the object
print(WorkItemIdModel.to_json())

# convert the object into a dict
work_item_id_model_dict = work_item_id_model_instance.to_dict()
# create an instance of WorkItemIdModel from a dict
work_item_id_model_from_dict = WorkItemIdModel.from_dict(work_item_id_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


