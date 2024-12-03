# NamedEntityModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Entity name. | [readonly] 
**id** | **str** | Entity Id. | [readonly] 

## Example

```python
from testit_api_client.models.named_entity_model import NamedEntityModel

# TODO update the JSON string below
json = "{}"
# create an instance of NamedEntityModel from a JSON string
named_entity_model_instance = NamedEntityModel.from_json(json)
# print the JSON string representation of the object
print(NamedEntityModel.to_json())

# convert the object into a dict
named_entity_model_dict = named_entity_model_instance.to_dict()
# create an instance of NamedEntityModel from a dict
named_entity_model_from_dict = NamedEntityModel.from_dict(named_entity_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


