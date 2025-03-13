# ProjectExternalServiceSettingsApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | **object** | External service settings | [optional] 

## Example

```python
from testit_api_client.models.project_external_service_settings_api_result import ProjectExternalServiceSettingsApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectExternalServiceSettingsApiResult from a JSON string
project_external_service_settings_api_result_instance = ProjectExternalServiceSettingsApiResult.from_json(json)
# print the JSON string representation of the object
print(ProjectExternalServiceSettingsApiResult.to_json())

# convert the object into a dict
project_external_service_settings_api_result_dict = project_external_service_settings_api_result_instance.to_dict()
# create an instance of ProjectExternalServiceSettingsApiResult from a dict
project_external_service_settings_api_result_from_dict = ProjectExternalServiceSettingsApiResult.from_dict(project_external_service_settings_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


