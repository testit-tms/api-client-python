# WorkItemExtractionApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Extraction parameters for projects | [optional] 
**ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Extraction parameters for work items | [optional] 
**section_ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Extraction parameters for sections | [optional] 

## Example

```python
from testit_api_client.models.work_item_extraction_api_model import WorkItemExtractionApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemExtractionApiModel from a JSON string
work_item_extraction_api_model_instance = WorkItemExtractionApiModel.from_json(json)
# print the JSON string representation of the object
print(WorkItemExtractionApiModel.to_json())

# convert the object into a dict
work_item_extraction_api_model_dict = work_item_extraction_api_model_instance.to_dict()
# create an instance of WorkItemExtractionApiModel from a dict
work_item_extraction_api_model_from_dict = WorkItemExtractionApiModel.from_dict(work_item_extraction_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


