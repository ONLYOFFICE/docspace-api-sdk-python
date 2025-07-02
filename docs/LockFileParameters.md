# LockFileParameters
The parameters for locking a file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock_file** | **bool** | Specifies whether to lock a file or not. | [optional] 

## Example

```python
from docspace-api-python.models.lock_file_parameters import LockFileParameters

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


