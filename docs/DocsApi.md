# docspace_api_sdk.DocsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_file**](#convert_file) | **POST** /api/2.0/docs/converter | Convert a file
[**run_builder_script**](#run_builder_script) | **POST** /api/2.0/docs/builder | Run a document builder script


# **convert_file**
> FileWrapper convert_file(convert_file_request_dto=convert_file_request_dto)

Converts a portal file into another format and saves the result as a new file, answering with that file. The
caller needs read access to a source that may be copied and the right to create files in `folderId`; without
`folderId` the result goes to the My documents section of the caller, so a guest, who has none, has to pass
it. A file in a private room or in a room with a watermark is not converted, as it would leave the room without
its protection, and no result is saved into such a room. `outputtype` is the only parameter a plain
conversion needs; the other fields are passed to the document service under its own names, while the source
format, name and cache key are taken from the file. The call is mutating and not idempotent: the source is kept,
and each call adds another file under a free name. It answers once the conversion is done, so a large file keeps
the request open. Only files stored in the portal itself are accepted. To convert while copying into another
folder, a third-party one included, use `POST api/2.0/files/file/{fileId}/copyas`; to convert into the portal's
own editable format beside the source, use `PUT api/2.0/files/file/{fileId}/checkconversion`. A missing or
unsupported `outputtype` is refused with 400, and so is a source the document service rejects: a wrong or
missing `password`, or a file too large to convert; retrying the same request will not help. Missing access or a
protected room is refused with 403 and an unknown file or folder with 404, both before any conversion starts. A
result that does not fit the storage quota of the portal, the room or the caller is refused with 402. A
conversion the document service fails is answered with 502: the service may be down or the file damaged; a retry
helps only in the first case.

Raises the `file.created` webhook.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **convert_file_request_dto** | [**ConvertFileRequestDto**](ConvertFileRequestDto.md)|  | [optional] 

### Return type

[**FileWrapper**](FileWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.convert_file_request_dto import ConvertFileRequestDto
from docspace_api_sdk.models.file_wrapper import FileWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.DocsApi(api_client)
    convert_file_request_dto = docspace_api_sdk.ConvertFileRequestDto() # ConvertFileRequestDto |  (optional)

    try:
        # Convert a file
        api_response = api_instance.convert_file(convert_file_request_dto=convert_file_request_dto)
        print("The response of DocsApi->convert_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocsApi->convert_file: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The converted file, as it was saved in the portal |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | `outputtype` is missing or the file cannot be converted to it, `folderId` is missing for a caller without My documents, or the document service rejects the source: a wrong or missing password, or a file too large |  -  |
**402** | The result does not fit the storage quota of the portal, the room or the caller |  -  |
**403** | You cannot read or copy the file or create files in the folder, the file lies in a private room or in a room with a watermark, or the folder lies in a private room or in a room with a watermark |  -  |
**404** | The file or the folder does not exist |  -  |
**502** | The document service is unreachable or failed the conversion without naming the reason; the source may be damaged |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_builder_script**
> FileOperationWrapper run_builder_script(run_builder_script_request_dto=run_builder_script_request_dto)

Queues a background run of a document builder script and answers with the operation just started. The script
names portal files by identifier - `builder.OpenFile(1234)` - where the document builder documentation writes
an address; only portal files can be opened, and none from a private room or a room with a watermark, nor is a
result saved into such a room. A script may call OpenFile and SaveFile at most 20 times each, counting every
call written in it. The caller needs edit access to every file the script opens, which may also be copied, and
to each file `outputs` replaces, which must not be locked or open in an editor, and the right to create files in
each folder a result is saved into. Each file the script saves goes where `outputs` says, keyed by the name
given to SaveFile: `fileId` stores it as a new version of that file, `folderId` as a new file there; an unlisted
file goes to `folderId` or to the folder of the opened file. Each entry of `outputs` names exactly one of
`fileId` and `folderId`; `title` goes only with `folderId`, since a replaced file keeps its title, and a result
stored over `fileId` has to be in that file's format. The call is not idempotent: each call is a new run. Poll
`GET api/2.0/files/fileops` with the returned `id` until the operation reports `finished`: `files` then lists
the saved files, a replaced one with its new version, including those saved before a failure, and `error` the
reason a failed build gave. A build that has not finished after 10 minutes is given up and reported as failed. A
caller runs one script at a time: a new request while an earlier one is queued or running is refused with 403,
so wait for `finished` before starting the next. For a plain format change use `POST api/2.0/docs/converter`.
What can be refused in advance fails at once with 400, 403 or 404.

Raises the `file.created` and `file.updated` webhooks for each file the queued script saves: `file.created` for a new file, `file.updated` for an existing one.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_builder_script_request_dto** | [**RunBuilderScriptRequestDto**](RunBuilderScriptRequestDto.md)|  | [optional] 

### Return type

[**FileOperationWrapper**](FileOperationWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_operation_wrapper import FileOperationWrapper
from docspace_api_sdk.models.run_builder_script_request_dto import RunBuilderScriptRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.DocsApi(api_client)
    run_builder_script_request_dto = docspace_api_sdk.RunBuilderScriptRequestDto() # RunBuilderScriptRequestDto |  (optional)

    try:
        # Run a document builder script
        api_response = api_instance.run_builder_script(run_builder_script_request_dto=run_builder_script_request_dto)
        print("The response of DocsApi->run_builder_script:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocsApi->run_builder_script: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The queued document builder operation to poll |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The script or the argument is malformed or too long, the script calls OpenFile or SaveFile too often, a file is addressed by an address, an `outputs` entry breaks the rules above, or a saved file has nowhere to go |  -  |
**403** | You cannot edit or copy a file the script opens or write a result, a file the script opens lies in a private room or in a room with a watermark, the file to replace or a target folder lies in a private room or in a room with a watermark, the file to replace is locked, being edited or in the trash, or another script of yours is still queued or running |  -  |
**404** | A file the script opens or replaces, or a target folder, does not exist |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

