# ProjectExternalServiceApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the external service | 
**name** | **str** | The name of the external service | 
**metadata** | [**ExternalServiceMetadataApiResult**](ExternalServiceMetadataApiResult.md) | The metadata associated with the external service | 
**enabled** | **bool** | Indicates whether the external service is enabled or not | 

## Example

```python
from testit_api_client.models.project_external_service_api_result import ProjectExternalServiceApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectExternalServiceApiResult from a JSON string
project_external_service_api_result_instance = ProjectExternalServiceApiResult.from_json(json)
# print the JSON string representation of the object
print(ProjectExternalServiceApiResult.to_json())

# convert the object into a dict
project_external_service_api_result_dict = project_external_service_api_result_instance.to_dict()
# create an instance of ProjectExternalServiceApiResult from a dict
project_external_service_api_result_from_dict = ProjectExternalServiceApiResult.from_dict(project_external_service_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


