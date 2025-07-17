# CustomAttributeChangeModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**old_attribute_name** | **str** |  | [optional] 
**new_attribute_name** | **str** |  | [optional] 
**old_value** | **object** |  | [optional] 
**new_value** | **object** |  | [optional] 

## Example

```python
from testit_api_client.models.custom_attribute_change_model import CustomAttributeChangeModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeChangeModel from a JSON string
custom_attribute_change_model_instance = CustomAttributeChangeModel.from_json(json)
# print the JSON string representation of the object
print CustomAttributeChangeModel.to_json()

# convert the object into a dict
custom_attribute_change_model_dict = custom_attribute_change_model_instance.to_dict()
# create an instance of CustomAttributeChangeModel from a dict
custom_attribute_change_model_from_dict = CustomAttributeChangeModel.from_dict(custom_attribute_change_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


