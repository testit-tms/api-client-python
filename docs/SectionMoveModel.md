# SectionMoveModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the section | 
**old_parent_id** | **str** | Unique ID of the section&#39;s current parent section | 
**parent_id** | **str** | Unique ID of the section&#39;s target parent section | 
**next_section_id** | **str** | Unique ID of the section&#39;s following section | [optional] 

## Example

```python
from testit_api_client.models.section_move_model import SectionMoveModel

# TODO update the JSON string below
json = "{}"
# create an instance of SectionMoveModel from a JSON string
section_move_model_instance = SectionMoveModel.from_json(json)
# print the JSON string representation of the object
print SectionMoveModel.to_json()

# convert the object into a dict
section_move_model_dict = section_move_model_instance.to_dict()
# create an instance of SectionMoveModel from a dict
section_move_model_from_dict = SectionMoveModel.from_dict(section_move_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


