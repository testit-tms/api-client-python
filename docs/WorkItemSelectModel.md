# WorkItemSelectModel

Model containing options to filter work items

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**WorkItemFilterModel**](WorkItemFilterModel.md) | Collection of filters to apply to search | 
**extraction_model** | [**WorkItemExtractionModel**](WorkItemExtractionModel.md) | Rules for different level entities inclusion/exclusion | [optional] 

## Example

```python
from testit_api_client.models.work_item_select_model import WorkItemSelectModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemSelectModel from a JSON string
work_item_select_model_instance = WorkItemSelectModel.from_json(json)
# print the JSON string representation of the object
print WorkItemSelectModel.to_json()

# convert the object into a dict
work_item_select_model_dict = work_item_select_model_instance.to_dict()
# create an instance of WorkItemSelectModel from a dict
work_item_select_model_from_dict = WorkItemSelectModel.from_dict(work_item_select_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


