# WorkItemLinkExtractionApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | [**GuidExtractionModel**](GuidExtractionModel.md) |  | [optional] 
**work_item_ids** | [**GuidExtractionModel**](GuidExtractionModel.md) |  | [optional] 
**link_urls** | [**StringExtractionModel**](StringExtractionModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.work_item_link_extraction_api_model import WorkItemLinkExtractionApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemLinkExtractionApiModel from a JSON string
work_item_link_extraction_api_model_instance = WorkItemLinkExtractionApiModel.from_json(json)
# print the JSON string representation of the object
print WorkItemLinkExtractionApiModel.to_json()

# convert the object into a dict
work_item_link_extraction_api_model_dict = work_item_link_extraction_api_model_instance.to_dict()
# create an instance of WorkItemLinkExtractionApiModel from a dict
work_item_link_extraction_api_model_from_dict = WorkItemLinkExtractionApiModel.from_dict(work_item_link_extraction_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


