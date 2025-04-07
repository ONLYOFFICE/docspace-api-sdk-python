# docspace.SecurityCSPApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**csp**](SecurityCSPApi.md#csp) | **POST** /api/2.0/security/csp | Csp
[**get_csp**](SecurityCSPApi.md#get_csp) | **GET** /api/2.0/security/csp | Gets csp


# **csp**
> CspWrapper csp(csp_requests_dto=csp_requests_dto)

Csp

Csp

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.csp_requests_dto import CspRequestsDto
from docspace.models.csp_wrapper import CspWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SecurityCSPApi(api_client)
    csp_requests_dto = docspace.CspRequestsDto() # CspRequestsDto |  (optional)

    try:
        # Csp
        api_response = api_instance.csp(csp_requests_dto=csp_requests_dto)
        print("The response of SecurityCSPApi->csp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityCSPApi->csp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csp_requests_dto** | [**CspRequestsDto**](CspRequestsDto.md)|  | [optional] 

### Return type

[**CspWrapper**](CspWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Exception in Domains |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csp**
> CspWrapper get_csp()

Gets csp

Gets csp

### Example


```python
import docspace
from docspace.models.csp_wrapper import CspWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SecurityCSPApi(api_client)

    try:
        # Gets csp
        api_response = api_instance.get_csp()
        print("The response of SecurityCSPApi->get_csp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityCSPApi->get_csp: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CspWrapper**](CspWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

