# TagApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Tag name | 

## Example

```python
from testit_api_client.models.tag_api_model import TagApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TagApiModel from a JSON string
tag_api_model_instance = TagApiModel.from_json(json)
# print the JSON string representation of the object
print(TagApiModel.to_json())

# convert the object into a dict
tag_api_model_dict = tag_api_model_instance.to_dict()
# create an instance of TagApiModel from a dict
tag_api_model_from_dict = TagApiModel.from_dict(tag_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


