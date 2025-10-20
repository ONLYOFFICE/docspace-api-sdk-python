# BackupServiceStateWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BackupServiceStateDto**](BackupServiceStateDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.backup_service_state_wrapper import BackupServiceStateWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of BackupServiceStateWrapper from a JSON string
backup_service_state_wrapper_instance = BackupServiceStateWrapper.from_json(json)
# print the JSON string representation of the object
print(BackupServiceStateWrapper.to_json())

# convert the object into a dict
backup_service_state_wrapper_dict = backup_service_state_wrapper_instance.to_dict()
# create an instance of BackupServiceStateWrapper from a dict
backup_service_state_wrapper_from_dict = BackupServiceStateWrapper.from_dict(backup_service_state_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


