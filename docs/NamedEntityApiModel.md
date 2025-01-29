# NamedEntityApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Entity name. | 
**id** | **str** | Entity Id. | 

## Example

```python
from testit_api_client.models.named_entity_api_model import NamedEntityApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of NamedEntityApiModel from a JSON string
named_entity_api_model_instance = NamedEntityApiModel.from_json(json)
# print the JSON string representation of the object
print(NamedEntityApiModel.to_json())

# convert the object into a dict
named_entity_api_model_dict = named_entity_api_model_instance.to_dict()
# create an instance of NamedEntityApiModel from a dict
named_entity_api_model_from_dict = NamedEntityApiModel.from_dict(named_entity_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


