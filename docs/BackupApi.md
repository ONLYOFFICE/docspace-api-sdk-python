# docspace.BackupApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_backup_schedule**](BackupApi.md#create_backup_schedule) | **POST** /api/2.0/backup/createbackupschedule | Create the backup schedule
[**delete_backup**](BackupApi.md#delete_backup) | **DELETE** /api/2.0/backup/deletebackup/{id} | Delete the backup
[**delete_backup_history**](BackupApi.md#delete_backup_history) | **DELETE** /api/2.0/backup/deletebackuphistory | Delete the backup history
[**delete_backup_schedule**](BackupApi.md#delete_backup_schedule) | **DELETE** /api/2.0/backup/deletebackupschedule | Delete the backup schedule
[**get_backup_history**](BackupApi.md#get_backup_history) | **GET** /api/2.0/backup/getbackuphistory | Get the backup history
[**get_backup_progress**](BackupApi.md#get_backup_progress) | **GET** /api/2.0/backup/getbackupprogress | Get the backup progress
[**get_backup_schedule**](BackupApi.md#get_backup_schedule) | **GET** /api/2.0/backup/getbackupschedule | Get the backup schedule
[**get_restore_progress**](BackupApi.md#get_restore_progress) | **GET** /api/2.0/backup/getrestoreprogress | Get the restoring progress
[**start_backup**](BackupApi.md#start_backup) | **POST** /api/2.0/backup/startbackup | Start the backup
[**start_backup_restore**](BackupApi.md#start_backup_restore) | **POST** /api/2.0/backup/startrestore | Start the restoring process


# **create_backup_schedule**
> BooleanWrapper create_backup_schedule(backup_schedule_dto=backup_schedule_dto)

Create the backup schedule

Creates the backup schedule of the current portal with the parameters specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.backup_schedule_dto import BackupScheduleDto
from docspace.models.boolean_wrapper import BooleanWrapper
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
    api_instance = docspace.BackupApi(api_client)
    backup_schedule_dto = docspace.BackupScheduleDto() # BackupScheduleDto |  (optional)

    try:
        # Create the backup schedule
        api_response = api_instance.create_backup_schedule(backup_schedule_dto=backup_schedule_dto)
        print("The response of BackupApi->create_backup_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->create_backup_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_schedule_dto** | [**BackupScheduleDto**](BackupScheduleDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**400** | BackupStored must be 1 - 30 or backup can not start as dump |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |
**403** | You don&#39;t have enough permission to create |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_backup**
> BooleanWrapper delete_backup(id)

Delete the backup

Deletes the backup with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.boolean_wrapper import BooleanWrapper
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
    api_instance = docspace.BackupApi(api_client)
    id = '75a5f745-f697-4418-b38d-0fe0d277e258' # str | Backup Id

    try:
        # Delete the backup
        api_response = api_instance.delete_backup(id)
        print("The response of BackupApi->delete_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->delete_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Backup Id | 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_backup_history**
> BooleanWrapper delete_backup_history()

Delete the backup history

Deletes the backup history of the current portal.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.boolean_wrapper import BooleanWrapper
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
    api_instance = docspace.BackupApi(api_client)

    try:
        # Delete the backup history
        api_response = api_instance.delete_backup_history()
        print("The response of BackupApi->delete_backup_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->delete_backup_history: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_backup_schedule**
> BooleanWrapper delete_backup_schedule()

Delete the backup schedule

Deletes the backup schedule of the current portal.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.boolean_wrapper import BooleanWrapper
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
    api_instance = docspace.BackupApi(api_client)

    try:
        # Delete the backup schedule
        api_response = api_instance.delete_backup_schedule()
        print("The response of BackupApi->delete_backup_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->delete_backup_schedule: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_history**
> BackupHistoryRecordArrayWrapper get_backup_history()

Get the backup history

Returns the history of the started backup.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.backup_history_record_array_wrapper import BackupHistoryRecordArrayWrapper
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
    api_instance = docspace.BackupApi(api_client)

    try:
        # Get the backup history
        api_response = api_instance.get_backup_history()
        print("The response of BackupApi->get_backup_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->get_backup_history: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BackupHistoryRecordArrayWrapper**](BackupHistoryRecordArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of backup history records |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_progress**
> BackupProgressWrapper get_backup_progress()

Get the backup progress

Returns the progress of the started backup.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.backup_progress_wrapper import BackupProgressWrapper
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
    api_instance = docspace.BackupApi(api_client)

    try:
        # Get the backup progress
        api_response = api_instance.get_backup_progress()
        print("The response of BackupApi->get_backup_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->get_backup_progress: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BackupProgressWrapper**](BackupProgressWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Backup progress: completed or not, progress percentage, error, tenant ID, backup progress item (Backup, Restore, Transfer), link |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_schedule**
> ScheduleWrapper get_backup_schedule()

Get the backup schedule

Returns the backup schedule of the current portal.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.schedule_wrapper import ScheduleWrapper
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
    api_instance = docspace.BackupApi(api_client)

    try:
        # Get the backup schedule
        api_response = api_instance.get_backup_schedule()
        print("The response of BackupApi->get_backup_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->get_backup_schedule: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ScheduleWrapper**](ScheduleWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Backup schedule |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_restore_progress**
> BackupProgressWrapper get_restore_progress()

Get the restoring progress

Returns the progress of the started restoring process.

### Example


```python
import docspace
from docspace.models.backup_progress_wrapper import BackupProgressWrapper
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
    api_instance = docspace.BackupApi(api_client)

    try:
        # Get the restoring progress
        api_response = api_instance.get_restore_progress()
        print("The response of BackupApi->get_restore_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->get_restore_progress: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BackupProgressWrapper**](BackupProgressWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Backup progress: completed or not, progress percentage, error, tenant ID, backup progress item (Backup, Restore, Transfer), link |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_backup**
> BackupProgressWrapper start_backup(backup_dto=backup_dto)

Start the backup

Starts the backup of the current portal with the parameters specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.backup_dto import BackupDto
from docspace.models.backup_progress_wrapper import BackupProgressWrapper
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
    api_instance = docspace.BackupApi(api_client)
    backup_dto = docspace.BackupDto() # BackupDto |  (optional)

    try:
        # Start the backup
        api_response = api_instance.start_backup(backup_dto=backup_dto)
        print("The response of BackupApi->start_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->start_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_dto** | [**BackupDto**](BackupDto.md)|  | [optional] 

### Return type

[**BackupProgressWrapper**](BackupProgressWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Backup progress: completed or not, progress percentage, error, tenant ID, backup progress item (Backup, Restore, Transfer), link |  -  |
**400** | Wrong folder type or backup can&#x60;t start as dump |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |
**403** | You don&#39;t have enough permission to create |  -  |
**404** | The required folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_backup_restore**
> BackupProgressWrapper start_backup_restore(backup_restore_dto=backup_restore_dto)

Start the restoring process

Starts the data restoring process of the current portal with the parameters specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.backup_progress_wrapper import BackupProgressWrapper
from docspace.models.backup_restore_dto import BackupRestoreDto
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
    api_instance = docspace.BackupApi(api_client)
    backup_restore_dto = docspace.BackupRestoreDto() # BackupRestoreDto |  (optional)

    try:
        # Start the restoring process
        api_response = api_instance.start_backup_restore(backup_restore_dto=backup_restore_dto)
        print("The response of BackupApi->start_backup_restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->start_backup_restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_restore_dto** | [**BackupRestoreDto**](BackupRestoreDto.md)|  | [optional] 

### Return type

[**BackupProgressWrapper**](BackupProgressWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Backup progress: completed or not, progress percentage, error, tenant ID, backup progress item (Backup, Restore, Transfer), link |  -  |
**400** | Backup can not start as dump |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |
**403** | You don&#39;t have enough permission to create |  -  |
**404** | The required file or folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

