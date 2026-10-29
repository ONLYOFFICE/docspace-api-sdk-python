# docspace_api_sdk.MetadataApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_meta_fill**](#ai_meta_fill) | **POST** /api/2.0/ai/meta/fill | Fill metadata values
[**ai_meta_generate**](#ai_meta_generate) | **POST** /api/2.0/ai/meta/generate | Generate metadata fields


# **ai_meta_fill**
> AiMetaFill200Response ai_meta_fill(ai_meta_fill_request)

Fills the metadata of one file from its text and writes the result. `kind` names the entry's table and `id` its integer identifier; only `file` is accepted for now, a folder or a room answers 400 until it is settled whether their metadata should describe the entry itself or its files; `prompt` is an optional note for the model on what to pay attention to, passed as a hint, never as an instruction; `overwrite` (default false) also replaces the fields that already carry a value, otherwise only the empty ones are filled and the rest are reported as `already_set`; `dryRun` (default true) resolves the values but writes nothing, so the caller shows them for confirmation and saves the accepted ones itself; only an explicit `dryRun: false` writes, and it is meant for a caller that has already collected the user's confirmation. The fields are the entry's own: every field of the visible templates it carries, assigned or inherited through a cascade - a hidden template is skipped as the UI and the search skip it - and its existing custom fields - no field is created here, use `POST api/2.0/ai/meta/generate` and the Files metadata API for that. The text is the file itself, converted to plain text under the caller's rights and cut to the same budgets as the generate route. The model bound to `GenerateMeta` (`Default` when that slot is empty) runs once, without tools, and is told to answer null for a value the text does not state. Each value is then checked the way the client's info panel checks a typed value - an integer for a number, a calendar date for a date, one of the field's own options for a choice - and the ones that pass are written with `PUT api/2.0/files/metadata/{kind}/{id}/values` and `.../customFields`, so the caller needs the rights those routes need; a write the portal refuses is reported per field as `write_failed`, and the call fails with the portal's status only when nothing was written at all. The answer carries `dryRun` as it was applied, the entry's metadata after the write (or as it stands, with `dryRun`), the values written or proposed, the fields left empty with the reason for each, and the documents that were read.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_meta_fill_request** | [**AiMetaFillRequest**](AiMetaFillRequest.md)|  | 

### Return type

[**AiMetaFill200Response**](AiMetaFill200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_meta_fill200_response import AiMetaFill200Response
from docspace_api_sdk.models.ai_meta_fill_request import AiMetaFillRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    ai_meta_fill_request = docspace_api_sdk.AiMetaFillRequest() # AiMetaFillRequest | 

    try:
        # Fill metadata values
        api_response = api_instance.ai_meta_fill(ai_meta_fill_request)
        print("The response of MetadataApi->ai_meta_fill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->ai_meta_fill: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether it was a dry run, the entry's metadata, the values written or proposed, the fields left empty with the reason for each, and the documents the values were read from. |  -  |
**400** | `kind` is not `file` (folders and rooms are not accepted for now), `id` is not an integer id, `prompt` is not a string, or `overwrite` / `dryRun` is not a boolean. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**402** | The model provider refused the request for lack of credit; `code` and `providerMessage` carry its own words. |  -  |
**403** | The caller cannot read the entry, or cannot edit it when the values are written. |  -  |
**404** | The entry does not exist. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**422** | The entry has no metadata fields to fill, or none of its content could be read as text. |  -  |
**429** | The model provider is rate-limiting requests; `code` and `providerMessage` carry its own words. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |
**502** | The model request failed; `code` says how and `providerMessage` carries the provider's own words when it gave any. |  -  |
**503** | No profile is bound to `GenerateMeta` and the `Default` slot is empty too. |  -  |
**504** | Reading the files or the model round did not finish within the time budget. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_meta_generate**
> AiMetaGenerate200Response ai_meta_generate(ai_meta_generate_request)

Reads one file as text and asks the model bound to the `GenerateMeta` action - the `Default` slot when that action has no profile of its own - which custom metadata fields describe it, and what their values are. `kind` names the entry's table and `id` its integer identifier, the same way as `POST api/2.0/ai/meta/fill`; only `file` is accepted for now, a folder or a room answers 400 until it is settled whether their metadata should describe the entry itself or its files; `prompt` is an optional note on the kind of fields the caller is interested in, which is passed to the model as a hint, never as an instruction. The text is the file itself, converted to plain text through the portal's own conversion (word-processing and presentation formats, pdf included, to txt; spreadsheets to csv), under the caller's rights, so a file the caller cannot read is skipped as `forbidden` rather than failing the call. Each document is cut at 40 000 characters and the whole set at 240 000, which `sources[].truncated` reports. The model runs once, without tools, and the answer is validated: field names are trimmed, deduplicated regardless of case and capped at 50, the portal's own limit for custom fields on one entry; each field carries the value the text supports as a string, or `null` when the text does not state one, since a custom field on the portal is text and cannot be saved empty. Nothing is written: the caller decides which fields to create and saves them through the Files metadata API.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_meta_generate_request** | [**AiMetaGenerateRequest**](AiMetaGenerateRequest.md)|  | 

### Return type

[**AiMetaGenerate200Response**](AiMetaGenerate200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_meta_generate200_response import AiMetaGenerate200Response
from docspace_api_sdk.models.ai_meta_generate_request import AiMetaGenerateRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.MetadataApi(api_client)
    ai_meta_generate_request = docspace_api_sdk.AiMetaGenerateRequest() # AiMetaGenerateRequest | 

    try:
        # Generate metadata fields
        api_response = api_instance.ai_meta_generate(ai_meta_generate_request)
        print("The response of MetadataApi->ai_meta_generate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->ai_meta_generate: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The proposed fields, each with a name and the value found or null, the documents the proposal was read from, and the entries that were left out with the reason for each. |  -  |
**400** | `kind` is not `file` (folders and rooms are not accepted for now), `id` is not an integer id, or `prompt` is not a string. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**402** | The model provider refused the request for lack of credit; `code` and `providerMessage` carry its own words. |  -  |
**403** | The caller cannot open the entry. |  -  |
**404** | The entry does not exist. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**422** | The content could not be read as text; `skipped` says why. |  -  |
**429** | The model provider is rate-limiting requests; `code` and `providerMessage` carry its own words. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |
**502** | The model request failed; `code` says how and `providerMessage` carries the provider's own words when it gave any. |  -  |
**503** | No profile is bound to `GenerateMeta` and the `Default` slot is empty too. |  -  |
**504** | Reading the files or the model round did not finish within the time budget. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

