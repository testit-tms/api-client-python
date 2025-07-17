# testit_api_client.AttachmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_attachments_id_delete**](AttachmentsApi.md#api_v2_attachments_id_delete) | **DELETE** /api/v2/attachments/{id} | Delete attachment file
[**api_v2_attachments_id_get**](AttachmentsApi.md#api_v2_attachments_id_get) | **GET** /api/v2/attachments/{id} | Download attachment file
[**api_v2_attachments_id_metadata_get**](AttachmentsApi.md#api_v2_attachments_id_metadata_get) | **GET** /api/v2/attachments/{id}/metadata | Get attachment metadata
[**api_v2_attachments_occupied_file_storage_size_get**](AttachmentsApi.md#api_v2_attachments_occupied_file_storage_size_get) | **GET** /api/v2/attachments/occupiedFileStorageSize | Get size of attachments storage in bytes
[**api_v2_attachments_post**](AttachmentsApi.md#api_v2_attachments_post) | **POST** /api/v2/attachments | Upload new attachment file


# **api_v2_attachments_id_delete**
> api_v2_attachments_id_delete(id)

Delete attachment file



### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
import testit_api_client
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
    api_instance = testit_api_client.AttachmentsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete attachment file
        api_instance.api_v2_attachments_id_delete(id)
    except Exception as e:
        print("Exception when calling AttachmentsApi->api_v2_attachments_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Attachment file was deleted successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Attachment file is already in use |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_attachments_id_get**
> api_v2_attachments_id_get(id, width=width, height=height, resize_type=resize_type, background_color=background_color, preview=preview)

Download attachment file



### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
import testit_api_client
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
    api_instance = testit_api_client.AttachmentsApi(api_client)
    id = 'id_example' # str | 
    width = 56 # int | Width of the result image (optional)
    height = 56 # int | Height of the result image (optional)
    resize_type = testit_api_client.ImageResizeType() # ImageResizeType | Type of resizing to apply to the result image (optional)
    background_color = 'background_color_example' # str | Color of the background if the `resizeType` is `AddBackgroundStripes` (optional)
    preview = True # bool | If image must be converted to a preview (lower quality, no animation) (optional)

    try:
        # Download attachment file
        api_instance.api_v2_attachments_id_get(id, width=width, height=height, resize_type=resize_type, background_color=background_color, preview=preview)
    except Exception as e:
        print("Exception when calling AttachmentsApi->api_v2_attachments_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **width** | **int**| Width of the result image | [optional] 
 **height** | **int**| Height of the result image | [optional] 
 **resize_type** | [**ImageResizeType**](.md)| Type of resizing to apply to the result image | [optional] 
 **background_color** | **str**| Color of the background if the &#x60;resizeType&#x60; is &#x60;AddBackgroundStripes&#x60; | [optional] 
 **preview** | **bool**| If image must be converted to a preview (lower quality, no animation) | [optional] 

### Return type

void (empty response body)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_attachments_id_metadata_get**
> AttachmentModel api_v2_attachments_id_metadata_get(id)

Get attachment metadata



### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
import testit_api_client
from testit_api_client.models.attachment_model import AttachmentModel
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
    api_instance = testit_api_client.AttachmentsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get attachment metadata
        api_response = api_instance.api_v2_attachments_id_metadata_get(id)
        print("The response of AttachmentsApi->api_v2_attachments_id_metadata_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->api_v2_attachments_id_metadata_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AttachmentModel**](AttachmentModel.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_attachments_occupied_file_storage_size_get**
> int api_v2_attachments_occupied_file_storage_size_get()

Get size of attachments storage in bytes



### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
import testit_api_client
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
    api_instance = testit_api_client.AttachmentsApi(api_client)

    try:
        # Get size of attachments storage in bytes
        api_response = api_instance.api_v2_attachments_occupied_file_storage_size_get()
        print("The response of AttachmentsApi->api_v2_attachments_occupied_file_storage_size_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->api_v2_attachments_occupied_file_storage_size_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**int**

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_attachments_post**
> AttachmentModel api_v2_attachments_post(file=file)

Upload new attachment file

File size is restricted to 1 GB (1 073 741 824 bytes)

### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
import testit_api_client
from testit_api_client.models.attachment_model import AttachmentModel
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
    api_instance = testit_api_client.AttachmentsApi(api_client)
    file = None # bytearray |  (optional)

    try:
        # Upload new attachment file
        api_response = api_instance.api_v2_attachments_post(file=file)
        print("The response of AttachmentsApi->api_v2_attachments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->api_v2_attachments_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 

### Return type

[**AttachmentModel**](AttachmentModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  - Invalid file contents  - Invalid HTTP headers |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

