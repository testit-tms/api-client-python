# GenerateWorkItemPreviewsApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_service_id** | **str** |  | 
**task_key** | **str** |  | 
**section_id** | **str** |  | 

## Example

```python
from testit_api_client.models.generate_work_item_previews_api_model import GenerateWorkItemPreviewsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateWorkItemPreviewsApiModel from a JSON string
generate_work_item_previews_api_model_instance = GenerateWorkItemPreviewsApiModel.from_json(json)
# print the JSON string representation of the object
print(GenerateWorkItemPreviewsApiModel.to_json())

# convert the object into a dict
generate_work_item_previews_api_model_dict = generate_work_item_previews_api_model_instance.to_dict()
# create an instance of GenerateWorkItemPreviewsApiModel from a dict
generate_work_item_previews_api_model_from_dict = GenerateWorkItemPreviewsApiModel.from_dict(generate_work_item_previews_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


