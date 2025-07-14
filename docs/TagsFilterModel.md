# TagsFilterModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies a tag name to search for | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a tag range of creation date to search for | [optional] 
**created_by_ids** | **List[str]** | Specifies a tag creator IDs to search for | [optional] 

## Example

```python
from testit_api_client.models.tags_filter_model import TagsFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of TagsFilterModel from a JSON string
tags_filter_model_instance = TagsFilterModel.from_json(json)
# print the JSON string representation of the object
print TagsFilterModel.to_json()

# convert the object into a dict
tags_filter_model_dict = tags_filter_model_instance.to_dict()
# create an instance of TagsFilterModel from a dict
tags_filter_model_from_dict = TagsFilterModel.from_dict(tags_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


