# BackupProgressWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BackupProgress**](BackupProgress.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.backup_progress_wrapper import BackupProgressWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of BackupProgressWrapper from a JSON string
backup_progress_wrapper_instance = BackupProgressWrapper.from_json(json)
# print the JSON string representation of the object
print(BackupProgressWrapper.to_json())

# convert the object into a dict
backup_progress_wrapper_dict = backup_progress_wrapper_instance.to_dict()
# create an instance of BackupProgressWrapper from a dict
backup_progress_wrapper_from_dict = BackupProgressWrapper.from_dict(backup_progress_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


