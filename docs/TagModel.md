# TagModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.tag_model import TagModel

# TODO update the JSON string below
json = "{}"
# create an instance of TagModel from a JSON string
tag_model_instance = TagModel.from_json(json)
# print the JSON string representation of the object
print TagModel.to_json()

# convert the object into a dict
tag_model_dict = tag_model_instance.to_dict()
# create an instance of TagModel from a dict
tag_model_from_dict = TagModel.from_dict(tag_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


