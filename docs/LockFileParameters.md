# LockFileParameters
The lock state a file is to be put into.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock_file** | **bool** | The state to reach: `true` locks the file, which blocks editing, renaming and deleting for everybody but the  account that locked it and the room admins, and drops the others out of a running editing session; `false`  releases the lock. | [optional] 

## Example

```python
from docspace_api_sdk.models.lock_file_parameters import LockFileParameters

# TODO update the JSON string below
json = "{}"
# create an instance of LockFileParameters from a JSON string
lock_file_parameters_instance = LockFileParameters.from_json(json)
# print the JSON string representation of the object
print(LockFileParameters.to_json())

# convert the object into a dict
lock_file_parameters_dict = lock_file_parameters_instance.to_dict()
# create an instance of LockFileParameters from a dict
lock_file_parameters_from_dict = LockFileParameters.from_dict(lock_file_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


