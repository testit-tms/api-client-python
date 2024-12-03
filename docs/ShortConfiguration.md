# ShortConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from testit_api_client.models.short_configuration import ShortConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ShortConfiguration from a JSON string
short_configuration_instance = ShortConfiguration.from_json(json)
# print the JSON string representation of the object
print(ShortConfiguration.to_json())

# convert the object into a dict
short_configuration_dict = short_configuration_instance.to_dict()
# create an instance of ShortConfiguration from a dict
short_configuration_from_dict = ShortConfiguration.from_dict(short_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


