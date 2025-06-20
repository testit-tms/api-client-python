# WorkItemExtractionModel

Rules for different level entities inclusion/exclusion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Extraction parameters for projects | [optional] 
**ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Extraction parameters for work items | [optional] 
**section_ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Extraction parameters for sections | [optional] 

## Example

```python
from testit_api_client.models.work_item_extraction_model import WorkItemExtractionModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemExtractionModel from a JSON string
work_item_extraction_model_instance = WorkItemExtractionModel.from_json(json)
# print the JSON string representation of the object
print WorkItemExtractionModel.to_json()

# convert the object into a dict
work_item_extraction_model_dict = work_item_extraction_model_instance.to_dict()
# create an instance of WorkItemExtractionModel from a dict
work_item_extraction_model_from_dict = WorkItemExtractionModel.from_dict(work_item_extraction_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


