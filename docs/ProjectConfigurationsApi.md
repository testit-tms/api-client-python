# testit_api_client.ProjectConfigurationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configurations_by_project_id**](ProjectConfigurationsApi.md#get_configurations_by_project_id) | **GET** /api/v2/projects/{projectId}/configurations | Get project configurations


# **get_configurations_by_project_id**
> List[ConfigurationModel] get_configurations_by_project_id(project_id)

Get project configurations


Use case

User sets project internal or global identifier

User runs method execution

System search project

System search all configurations related to project

System returns array of found configurations (listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
import testit_api_client
from testit_api_client.models.configuration_model import ConfigurationModel
from testit_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = testit_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer or PrivateToken
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectConfigurationsApi(api_client)
    project_id = 'project_id_example' # str | Project internal (UUID) or global (integer) identifier

    try:
        # Get project configurations
        api_response = api_instance.get_configurations_by_project_id(project_id)
        print("The response of ProjectConfigurationsApi->get_configurations_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectConfigurationsApi->get_configurations_by_project_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier | 

### Return type

[**List[ConfigurationModel]**](ConfigurationModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for configurations required |  -  |
**404** | Project with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

