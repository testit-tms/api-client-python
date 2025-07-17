# ExternalServiceMetadataApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the external service | 
**code** | **str** | The code of the external service | 
**icon_url** | **str** | The icon URL of the external service | 
**category** | [**ExternalServiceCategoryApiResult**](ExternalServiceCategoryApiResult.md) | The category of the external service | 

## Example

```python
from testit_api_client.models.external_service_metadata_api_result import ExternalServiceMetadataApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalServiceMetadataApiResult from a JSON string
external_service_metadata_api_result_instance = ExternalServiceMetadataApiResult.from_json(json)
# print the JSON string representation of the object
print ExternalServiceMetadataApiResult.to_json()

# convert the object into a dict
external_service_metadata_api_result_dict = external_service_metadata_api_result_instance.to_dict()
# create an instance of ExternalServiceMetadataApiResult from a dict
external_service_metadata_api_result_from_dict = ExternalServiceMetadataApiResult.from_dict(external_service_metadata_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


