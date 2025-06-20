# WorkItemPreviewApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**action** | **str** |  | 
**expected** | **str** |  | 

## Example

```python
from testit_api_client.models.work_item_preview_api_model import WorkItemPreviewApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemPreviewApiModel from a JSON string
work_item_preview_api_model_instance = WorkItemPreviewApiModel.from_json(json)
# print the JSON string representation of the object
print(WorkItemPreviewApiModel.to_json())

# convert the object into a dict
work_item_preview_api_model_dict = work_item_preview_api_model_instance.to_dict()
# create an instance of WorkItemPreviewApiModel from a dict
work_item_preview_api_model_from_dict = WorkItemPreviewApiModel.from_dict(work_item_preview_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


