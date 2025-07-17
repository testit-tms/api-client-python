# GenerateWorkItemPreviewsApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previews** | [**List[WorkItemPreviewApiModel]**](WorkItemPreviewApiModel.md) |  | 
**link** | [**PreviewsIssueLinkApiResult**](PreviewsIssueLinkApiResult.md) |  | [optional] 

## Example

```python
from testit_api_client.models.generate_work_item_previews_api_result import GenerateWorkItemPreviewsApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateWorkItemPreviewsApiResult from a JSON string
generate_work_item_previews_api_result_instance = GenerateWorkItemPreviewsApiResult.from_json(json)
# print the JSON string representation of the object
print GenerateWorkItemPreviewsApiResult.to_json()

# convert the object into a dict
generate_work_item_previews_api_result_dict = generate_work_item_previews_api_result_instance.to_dict()
# create an instance of GenerateWorkItemPreviewsApiResult from a dict
generate_work_item_previews_api_result_from_dict = GenerateWorkItemPreviewsApiResult.from_dict(generate_work_item_previews_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


