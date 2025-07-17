# ExternalServicesMetadataApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExternalServiceMetadataApiResult]**](ExternalServiceMetadataApiResult.md) | External services metadata | 

## Example

```python
from testit_api_client.models.external_services_metadata_api_result import ExternalServicesMetadataApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalServicesMetadataApiResult from a JSON string
external_services_metadata_api_result_instance = ExternalServicesMetadataApiResult.from_json(json)
# print the JSON string representation of the object
print ExternalServicesMetadataApiResult.to_json()

# convert the object into a dict
external_services_metadata_api_result_dict = external_services_metadata_api_result_instance.to_dict()
# create an instance of ExternalServicesMetadataApiResult from a dict
external_services_metadata_api_result_from_dict = ExternalServicesMetadataApiResult.from_dict(external_services_metadata_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


