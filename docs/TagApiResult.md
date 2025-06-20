# TagApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the tag | 
**name** | **str** | Name of the tag | 
**created_date** | **datetime** | Creation date of the tag | 
**created_by_id** | **str** | ID of the user who created the tag | 
**modified_date** | **datetime** | Latest modification date of the tag | [optional] 
**modified_by_id** | **str** | ID of the user who last modified the tag | [optional] 

## Example

```python
from testit_api_client.models.tag_api_result import TagApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TagApiResult from a JSON string
tag_api_result_instance = TagApiResult.from_json(json)
# print the JSON string representation of the object
print TagApiResult.to_json()

# convert the object into a dict
tag_api_result_dict = tag_api_result_instance.to_dict()
# create an instance of TagApiResult from a dict
tag_api_result_from_dict = TagApiResult.from_dict(tag_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


