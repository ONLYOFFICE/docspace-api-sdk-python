# StorageDto
One third-party storage provider the portal data can be kept in, with the keys it expects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The provider's key, which is what `PUT api/2.0/settings/storage` and its CDN and backup counterparts take  as the storage to switch to. The built-in local storage has no entry of its own: a listing in which  nothing is `current` means the data sits locally. | 
**title** | **str** | The provider name in the portal language, falling back to `id` when this build ships no wording for it. | 
**properties** | [**List[AuthKey]**](AuthKey.md) | The settings the provider expects, each with its key, its localised label and the value the server  currently holds. For the entry marked `current` the values come from the portal's saved storage settings  and for the others from the installation configuration, so a setting nobody has configured comes back with  an empty value rather than being left out. | [optional] 
**current** | **bool** | Whether the portal is using this provider right now. At most one entry of a listing has it set. | 
**is_set** | **bool** | Whether the provider's keys are already filled in on the server, so it could be switched to without  sending credentials. It says nothing about whether the credentials still work. | 

## Example

```python
from docspace_api_sdk.models.storage_dto import StorageDto

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDto from a JSON string
storage_dto_instance = StorageDto.from_json(json)
# print the JSON string representation of the object
print(StorageDto.to_json())

# convert the object into a dict
storage_dto_dict = storage_dto_instance.to_dict()
# create an instance of StorageDto from a dict
storage_dto_from_dict = StorageDto.from_dict(storage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


