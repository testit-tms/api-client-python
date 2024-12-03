# SectionRenameModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from testit_api_client.models.section_rename_model import SectionRenameModel

# TODO update the JSON string below
json = "{}"
# create an instance of SectionRenameModel from a JSON string
section_rename_model_instance = SectionRenameModel.from_json(json)
# print the JSON string representation of the object
print(SectionRenameModel.to_json())

# convert the object into a dict
section_rename_model_dict = section_rename_model_instance.to_dict()
# create an instance of SectionRenameModel from a dict
section_rename_model_from_dict = SectionRenameModel.from_dict(section_rename_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


