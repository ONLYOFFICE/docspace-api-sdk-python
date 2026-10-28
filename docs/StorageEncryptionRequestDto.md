# StorageEncryptionRequestDto
Whether the users are warned before the portals go down for the storage encryption pass.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notify_users** | **bool** | Whether every user of every portal on the server is mailed before the encryption or decryption pass starts.  The pass runs either way; the flag only decides whether people are told that their portal is about to become  unavailable. | [optional] 

## Example

```python
from docspace_api_sdk.models.storage_encryption_request_dto import StorageEncryptionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of StorageEncryptionRequestDto from a JSON string
storage_encryption_request_dto_instance = StorageEncryptionRequestDto.from_json(json)
# print the JSON string representation of the object
print(StorageEncryptionRequestDto.to_json())

# convert the object into a dict
storage_encryption_request_dto_dict = storage_encryption_request_dto_instance.to_dict()
# create an instance of StorageEncryptionRequestDto from a dict
storage_encryption_request_dto_from_dict = StorageEncryptionRequestDto.from_dict(storage_encryption_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


