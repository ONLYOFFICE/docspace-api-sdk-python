# BackupProgressWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BackupProgress**](BackupProgress.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

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


