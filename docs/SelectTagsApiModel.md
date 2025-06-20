# SelectTagsApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TagsFilterApiModel**](TagsFilterApiModel.md) | Filters to select tags | [optional] 
**extraction_model** | [**TagsExtractionApiModel**](TagsExtractionApiModel.md) | Filters to extract tags | [optional] 

## Example

```python
from testit_api_client.models.select_tags_api_model import SelectTagsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of SelectTagsApiModel from a JSON string
select_tags_api_model_instance = SelectTagsApiModel.from_json(json)
# print the JSON string representation of the object
print(SelectTagsApiModel.to_json())

# convert the object into a dict
select_tags_api_model_dict = select_tags_api_model_instance.to_dict()
# create an instance of SelectTagsApiModel from a dict
select_tags_api_model_from_dict = SelectTagsApiModel.from_dict(select_tags_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


