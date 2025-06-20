# SearchWorkItemLinkUrlsApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WorkItemLinkUrlApiResult]**](WorkItemLinkUrlApiResult.md) |  | 

## Example

```python
from testit_api_client.models.search_work_item_link_urls_api_result import SearchWorkItemLinkUrlsApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchWorkItemLinkUrlsApiResult from a JSON string
search_work_item_link_urls_api_result_instance = SearchWorkItemLinkUrlsApiResult.from_json(json)
# print the JSON string representation of the object
print SearchWorkItemLinkUrlsApiResult.to_json()

# convert the object into a dict
search_work_item_link_urls_api_result_dict = search_work_item_link_urls_api_result_instance.to_dict()
# create an instance of SearchWorkItemLinkUrlsApiResult from a dict
search_work_item_link_urls_api_result_from_dict = SearchWorkItemLinkUrlsApiResult.from_dict(search_work_item_link_urls_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


