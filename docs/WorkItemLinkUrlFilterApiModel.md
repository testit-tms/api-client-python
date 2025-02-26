# WorkItemLinkUrlFilterApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | [**List[WorkItemEntityTypes]**](WorkItemEntityTypes.md) |  | [optional] 
**search_url** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.work_item_link_url_filter_api_model import WorkItemLinkUrlFilterApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItemLinkUrlFilterApiModel from a JSON string
work_item_link_url_filter_api_model_instance = WorkItemLinkUrlFilterApiModel.from_json(json)
# print the JSON string representation of the object
print(WorkItemLinkUrlFilterApiModel.to_json())

# convert the object into a dict
work_item_link_url_filter_api_model_dict = work_item_link_url_filter_api_model_instance.to_dict()
# create an instance of WorkItemLinkUrlFilterApiModel from a dict
work_item_link_url_filter_api_model_from_dict = WorkItemLinkUrlFilterApiModel.from_dict(work_item_link_url_filter_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


