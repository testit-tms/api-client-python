# ConfigurationShortApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from testit_api_client.models.configuration_short_api_result import ConfigurationShortApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationShortApiResult from a JSON string
configuration_short_api_result_instance = ConfigurationShortApiResult.from_json(json)
# print the JSON string representation of the object
print ConfigurationShortApiResult.to_json()

# convert the object into a dict
configuration_short_api_result_dict = configuration_short_api_result_instance.to_dict()
# create an instance of ConfigurationShortApiResult from a dict
configuration_short_api_result_from_dict = ConfigurationShortApiResult.from_dict(configuration_short_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


