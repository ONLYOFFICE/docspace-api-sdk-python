# docspace-api-sdk.CapabilitiesApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_portal_capabilities**](#get_portal_capabilities) | **GET** /api/2.0/capabilities | Get portal capabilities


# **get_portal_capabilities**
> CapabilitiesWrapper get_portal_capabilities()

Returns the information about portal capabilities.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**CapabilitiesWrapper**](CapabilitiesWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.capabilities_wrapper import CapabilitiesWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.CapabilitiesApi(api_client)

    try:
        # Get portal capabilities
        api_response = api_instance.get_portal_capabilities()
        print("The response of CapabilitiesApi->get_portal_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapabilitiesApi->get_portal_capabilities: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Portal capabilities |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

