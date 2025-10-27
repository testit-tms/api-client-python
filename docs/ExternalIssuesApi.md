# testit_api_client.ExternalIssuesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_external_issues_suggestions_post**](ExternalIssuesApi.md#api_v2_external_issues_suggestions_post) | **POST** /api/v2/external-issues/suggestions | Returns list of suggestions from available external issues


# **api_v2_external_issues_suggestions_post**
> ExternalIssueApiFieldSuggestionReply api_v2_external_issues_suggestions_post()

Returns list of suggestions from available external issues

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import external_issues_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_external_issues_suggestions_post_request import ApiV2ExternalIssuesSuggestionsPostRequest
from testit_api_client.model.external_issue_api_field_suggestion_reply import ExternalIssueApiFieldSuggestionReply
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
    api_instance = external_issues_api.ExternalIssuesApi(api_client)
    api_v2_external_issues_suggestions_post_request = ApiV2ExternalIssuesSuggestionsPostRequest(None) # ApiV2ExternalIssuesSuggestionsPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns list of suggestions from available external issues
        api_response = api_instance.api_v2_external_issues_suggestions_post(api_v2_external_issues_suggestions_post_request=api_v2_external_issues_suggestions_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ExternalIssuesApi->api_v2_external_issues_suggestions_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_external_issues_suggestions_post_request** | [**ApiV2ExternalIssuesSuggestionsPostRequest**](ApiV2ExternalIssuesSuggestionsPostRequest.md)|  | [optional]

### Return type

[**ExternalIssueApiFieldSuggestionReply**](ExternalIssueApiFieldSuggestionReply.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
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

