# TagsExtractionApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Specifies tags unique ID&#39;s to search for | [optional] 

## Example

```python
from testit_api_client.models.tags_extraction_api_model import TagsExtractionApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TagsExtractionApiModel from a JSON string
tags_extraction_api_model_instance = TagsExtractionApiModel.from_json(json)
# print the JSON string representation of the object
print TagsExtractionApiModel.to_json()

# convert the object into a dict
tags_extraction_api_model_dict = tags_extraction_api_model_instance.to_dict()
# create an instance of TagsExtractionApiModel from a dict
tags_extraction_api_model_from_dict = TagsExtractionApiModel.from_dict(tags_extraction_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


