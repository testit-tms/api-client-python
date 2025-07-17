# TagsFilterApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies a tag name to search for | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a tag range of creation date to search for | [optional] 
**created_by_ids** | **List[str]** | Specifies a tag creator IDs to search for | [optional] 

## Example

```python
from testit_api_client.models.tags_filter_api_model import TagsFilterApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TagsFilterApiModel from a JSON string
tags_filter_api_model_instance = TagsFilterApiModel.from_json(json)
# print the JSON string representation of the object
print TagsFilterApiModel.to_json()

# convert the object into a dict
tags_filter_api_model_dict = tags_filter_api_model_instance.to_dict()
# create an instance of TagsFilterApiModel from a dict
tags_filter_api_model_from_dict = TagsFilterApiModel.from_dict(tags_filter_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


