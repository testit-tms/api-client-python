# SectionModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**is_deleted** | **bool** |  | 
**id** | **str** |  | 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from testit_api_client.models.section_model import SectionModel

# TODO update the JSON string below
json = "{}"
# create an instance of SectionModel from a JSON string
section_model_instance = SectionModel.from_json(json)
# print the JSON string representation of the object
print SectionModel.to_json()

# convert the object into a dict
section_model_dict = section_model_instance.to_dict()
# create an instance of SectionModel from a dict
section_model_from_dict = SectionModel.from_dict(section_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


