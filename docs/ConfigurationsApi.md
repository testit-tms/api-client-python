# testit_api_client.ConfigurationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_configurations_create_by_parameters_post**](ConfigurationsApi.md#api_v2_configurations_create_by_parameters_post) | **POST** /api/v2/configurations/createByParameters | Create Configurations by parameters
[**api_v2_configurations_search_post**](ConfigurationsApi.md#api_v2_configurations_search_post) | **POST** /api/v2/configurations/search | Search for configurations
[**create_configuration**](ConfigurationsApi.md#create_configuration) | **POST** /api/v2/configurations | Create Configuration
[**get_configuration_by_id**](ConfigurationsApi.md#get_configuration_by_id) | **GET** /api/v2/configurations/{id} | Get configuration by internal or global ID
[**update_configuration**](ConfigurationsApi.md#update_configuration) | **PUT** /api/v2/configurations | Update Configuration


# **api_v2_configurations_create_by_parameters_post**
> [str] api_v2_configurations_create_by_parameters_post()

Create Configurations by parameters

<br>Use case  <br>User sets request model (listed in the request example)  <br>User runs method execution  <br>System creates configurations  <br>System returns created configuration ids (listed in the response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.configuration_by_parameters_model import ConfigurationByParametersModel
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
configuration.api_key['Bearer or PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configurations_api.ConfigurationsApi(api_client)
    configuration_by_parameters_model = ConfigurationByParametersModel(
        project_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        parameter_ids=[
            "parameter_ids_example",
        ],
    ) # ConfigurationByParametersModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Configurations by parameters
        api_response = api_instance.api_v2_configurations_create_by_parameters_post(configuration_by_parameters_model=configuration_by_parameters_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->api_v2_configurations_create_by_parameters_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_by_parameters_model** | [**ConfigurationByParametersModel**](ConfigurationByParametersModel.md)|  | [optional]

### Return type

**[str]**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | &lt;br&gt;Project by identifier not found  &lt;br&gt;Parameters by identifies not found |  -  |
**400** | &lt;br&gt;Project identifier is empty  &lt;br&gt;List of parameters identifiers is empty |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configurations_search_post**
> [ConfigurationModel] api_v2_configurations_search_post()

Search for configurations

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
from testit_api_client.model.configuration_model import ConfigurationModel
from testit_api_client.model.configuration_select_model import ConfigurationSelectModel
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
configuration.api_key['Bearer or PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configurations_api.ConfigurationsApi(api_client)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    configuration_select_model = ConfigurationSelectModel(
        project_ids=[
            "project_ids_example",
        ],
        name="name_example",
        is_deleted=True,
        global_ids=[
            1,
        ],
    ) # ConfigurationSelectModel | Model containing all the filters (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for configurations
        api_response = api_instance.api_v2_configurations_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, configuration_select_model=configuration_select_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->api_v2_configurations_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **configuration_select_model** | [**ConfigurationSelectModel**](ConfigurationSelectModel.md)| Model containing all the filters | [optional]

### Return type

[**[ConfigurationModel]**](ConfigurationModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_configuration**
> ConfigurationModel create_configuration()

Create Configuration

<br>Use case  <br>User sets configuration model (listed in the request example)  <br>User runs method execution  <br>System creates configuration  <br>System returns created configuration (listed in the response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.configuration_model import ConfigurationModel
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.configuration_post_model import ConfigurationPostModel
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
configuration.api_key['Bearer or PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configurations_api.ConfigurationsApi(api_client)
    configuration_post_model = ConfigurationPostModel(
        description="Default configuration",
        is_active=True,
        capabilities={
            "key": "key_example",
        },
        project_id="project_id_example",
        is_default=True,
        name="Default",
    ) # ConfigurationPostModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Configuration
        api_response = api_instance.create_configuration(configuration_post_model=configuration_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->create_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_post_model** | [**ConfigurationPostModel**](ConfigurationPostModel.md)|  | [optional]

### Return type

[**ConfigurationModel**](ConfigurationModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Update permission for configuration required |  -  |
**201** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**409** | Configuration with the same name already exists! |  -  |
**400** | &lt;br&gt;Capabilities are invalid  &lt;br&gt;- Capability keys must be unique  &lt;br&gt;- Capability keys must not be empty  &lt;br&gt;- Capability values must not be empty |  -  |
**404** | Can&#39;t find project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_by_id**
> ConfigurationModel get_configuration_by_id(id)

Get configuration by internal or global ID

<br>Use case  <br>User sets configuration internal (guid format) or global (integer format) identifier  <br>User runs method execution  <br>System search configuration using the identifier  <br>System returns configuration

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.configuration_model import ConfigurationModel
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
configuration.api_key['Bearer or PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configurations_api.ConfigurationsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get configuration by internal or global ID
        api_response = api_instance.get_configuration_by_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->get_configuration_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ConfigurationModel**](ConfigurationModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Can&#39;t find configuration with id |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for configuration required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration**
> update_configuration()

Update Configuration

<br>Use case  <br>User sets configuration updated properties(listed in the request example)  <br>User runs method execution  <br>System updated configuration using updated properties  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.configuration_put_model import ConfigurationPutModel
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
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
configuration.api_key['Bearer or PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configurations_api.ConfigurationsApi(api_client)
    configuration_put_model = ConfigurationPutModel(
        id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        description="Default configuration",
        is_active=True,
        capabilities={
            "key": "key_example",
        },
        project_id="project_id_example",
        is_default=True,
        name="Default",
    ) # ConfigurationPutModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Configuration
        api_instance.update_configuration(configuration_put_model=configuration_put_model)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->update_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_put_model** | [**ConfigurationPutModel**](ConfigurationPutModel.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Can&#39;t change projectId |  -  |
**204** | Successful operation |  -  |
**400** | &lt;br&gt;- Capabilities are invalid  &lt;br&gt;- Capability keys must be unique  &lt;br&gt;- Capability keys must not be empty  &lt;br&gt;- Capability values must not be empty |  -  |
**401** | Unauthorized |  -  |
**403** |  |  -  |
**404** | Can&#39;t find a Configuration with id |  -  |
**409** | Configuration with the same name already exists! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

