# ProjectExternalServicesApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProjectExternalServiceApiResult]**](ProjectExternalServiceApiResult.md) | External services associated with a project | 

## Example

```python
from testit_api_client.models.project_external_services_api_result import ProjectExternalServicesApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectExternalServicesApiResult from a JSON string
project_external_services_api_result_instance = ProjectExternalServicesApiResult.from_json(json)
# print the JSON string representation of the object
print(ProjectExternalServicesApiResult.to_json())

# convert the object into a dict
project_external_services_api_result_dict = project_external_services_api_result_instance.to_dict()
# create an instance of ProjectExternalServicesApiResult from a dict
project_external_services_api_result_from_dict = ProjectExternalServicesApiResult.from_dict(project_external_services_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


