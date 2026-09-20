# StorageRequestsDto
Which storage provider the portal is pointed at, and the credentials it needs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | **str** | The storage provider to switch to, by the identifier the matching listing operation reports - `default` for  the built-in local storage. The provider has to be available on the server, which that listing reports as  `isSet`, otherwise the request is refused with 400; sending the module already in use changes nothing. | 
**props** | [**List[ItemKeyValuePairStringString]**](ItemKeyValuePairStringString.md) | The credentials the provider expects, as the name and value pairs it defines - a bucket, a region and an  access key for an Amazon S3 storage, for instance. Read the expected names from the entry of that provider in  the listing operation; they differ per provider, so there is no fixed set. | [optional] 

## Example

```python
from docspace_api_sdk.models.storage_requests_dto import StorageRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of StorageRequestsDto from a JSON string
storage_requests_dto_instance = StorageRequestsDto.from_json(json)
# print the JSON string representation of the object
print(StorageRequestsDto.to_json())

# convert the object into a dict
storage_requests_dto_dict = storage_requests_dto_instance.to_dict()
# create an instance of StorageRequestsDto from a dict
storage_requests_dto_from_dict = StorageRequestsDto.from_dict(storage_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


