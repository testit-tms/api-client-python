# WorkItemLinkFilterModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | [**List[LinkType]**](LinkType.md) |  | [optional] 
**title** | **str** |  | [optional] 
**urls** | **List[str]** |  | [optional] 
**only_without_links** | **bool** |  | [optional] 

## Example

```python
from testit_api_client.models.work_item_link_filter_model import WorkItemLinkFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemLinkFilterModel from a JSON string
work_item_link_filter_model_instance = WorkItemLinkFilterModel.from_json(json)
# print the JSON string representation of the object
print(WorkItemLinkFilterModel.to_json())

# convert the object into a dict
work_item_link_filter_model_dict = work_item_link_filter_model_instance.to_dict()
# create an instance of WorkItemLinkFilterModel from a dict
work_item_link_filter_model_from_dict = WorkItemLinkFilterModel.from_dict(work_item_link_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


