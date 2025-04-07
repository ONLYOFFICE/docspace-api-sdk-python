# StorageEncryptionRequestsDto

Storage encryption request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notify_users** | **bool** | Specifies if the users will be notified about the encryption process or note | [optional] 

## Example

```python
from docspace.models.storage_encryption_requests_dto import StorageEncryptionRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of StorageEncryptionRequestsDto from a JSON string
storage_encryption_requests_dto_instance = StorageEncryptionRequestsDto.from_json(json)
# print the JSON string representation of the object
print(StorageEncryptionRequestsDto.to_json())

# convert the object into a dict
storage_encryption_requests_dto_dict = storage_encryption_requests_dto_instance.to_dict()
# create an instance of StorageEncryptionRequestsDto from a dict
storage_encryption_requests_dto_from_dict = StorageEncryptionRequestsDto.from_dict(storage_encryption_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


