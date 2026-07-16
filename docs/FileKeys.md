# FileKeys

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** |  | [optional] 
**public_key_id** | **UUID** |  | [optional] 
**private_key_enc** | **str** |  | [optional] 
**tenant_id** | **int** |  | [optional] 
**file_id** | **int** |  | [optional] 
**create_on** | **datetime** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.file_keys import FileKeys

# TODO update the JSON string below
json = "{}"
# create an instance of FileKeys from a JSON string
file_keys_instance = FileKeys.from_json(json)
# print the JSON string representation of the object
print(FileKeys.to_json())

# convert the object into a dict
file_keys_dict = file_keys_instance.to_dict()
# create an instance of FileKeys from a dict
file_keys_from_dict = FileKeys.from_dict(file_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


