# ExternalDbSyncTaskWrapper
The successful API response containing the ExternalDbSyncTaskDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ExternalDbSyncTaskDto**](ExternalDbSyncTaskDto.md) | The ExternalDbSyncTaskDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.external_db_sync_task_wrapper import ExternalDbSyncTaskWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDbSyncTaskWrapper from a JSON string
external_db_sync_task_wrapper_instance = ExternalDbSyncTaskWrapper.from_json(json)
# print the JSON string representation of the object
print(ExternalDbSyncTaskWrapper.to_json())

# convert the object into a dict
external_db_sync_task_wrapper_dict = external_db_sync_task_wrapper_instance.to_dict()
# create an instance of ExternalDbSyncTaskWrapper from a dict
external_db_sync_task_wrapper_from_dict = ExternalDbSyncTaskWrapper.from_dict(external_db_sync_task_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


