# TagSelectModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TagsFilterModel**](TagsFilterModel.md) |  | [optional] 
**extraction_model** | [**TagExtractionModel**](TagExtractionModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.tag_select_model import TagSelectModel

# TODO update the JSON string below
json = "{}"
# create an instance of TagSelectModel from a JSON string
tag_select_model_instance = TagSelectModel.from_json(json)
# print the JSON string representation of the object
print TagSelectModel.to_json()

# convert the object into a dict
tag_select_model_dict = tag_select_model_instance.to_dict()
# create an instance of TagSelectModel from a dict
tag_select_model_from_dict = TagSelectModel.from_dict(tag_select_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


