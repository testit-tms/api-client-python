# CreateWorkItemPreviewsApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section_id** | **str** |  | 
**previews** | [**List[WorkItemPreviewApiModel]**](WorkItemPreviewApiModel.md) |  | 
**attributes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from testit_api_client.models.create_work_item_previews_api_model import CreateWorkItemPreviewsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkItemPreviewsApiModel from a JSON string
create_work_item_previews_api_model_instance = CreateWorkItemPreviewsApiModel.from_json(json)
# print the JSON string representation of the object
print(CreateWorkItemPreviewsApiModel.to_json())

# convert the object into a dict
create_work_item_previews_api_model_dict = create_work_item_previews_api_model_instance.to_dict()
# create an instance of CreateWorkItemPreviewsApiModel from a dict
create_work_item_previews_api_model_from_dict = CreateWorkItemPreviewsApiModel.from_dict(create_work_item_previews_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


