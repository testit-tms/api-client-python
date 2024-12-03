# WorkItemVersionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_id** | **str** | used for versioning changes in workitem | 
**version_number** | **int** | used for define chronology of workitem state in each version | 
**modified_date** | **datetime** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.work_item_version_model import WorkItemVersionModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemVersionModel from a JSON string
work_item_version_model_instance = WorkItemVersionModel.from_json(json)
# print the JSON string representation of the object
print(WorkItemVersionModel.to_json())

# convert the object into a dict
work_item_version_model_dict = work_item_version_model_instance.to_dict()
# create an instance of WorkItemVersionModel from a dict
work_item_version_model_from_dict = WorkItemVersionModel.from_dict(work_item_version_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


