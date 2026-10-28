# SaveAuthKeysRequestDto
The keys to store for one third-party authorization or storage provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The internal key of the provider, such as `google` or `box`. Take it from the `name` of  `GET api/2.0/settings/authservice`. | [optional] 
**title** | **str** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 
**description** | **str** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 
**instruction** | **str** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 
**can_set** | **bool** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 
**paid** | **bool** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 
**props** | [**List[AuthKeyRequest]**](AuthKeyRequest.md) | The keys of the provider with their new values, by the key names `GET api/2.0/settings/authservice` lists in  `props`. | [optional] 

## Example

```python
from docspace_api_sdk.models.save_auth_keys_request_dto import SaveAuthKeysRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SaveAuthKeysRequestDto from a JSON string
save_auth_keys_request_dto_instance = SaveAuthKeysRequestDto.from_json(json)
# print the JSON string representation of the object
print(SaveAuthKeysRequestDto.to_json())

# convert the object into a dict
save_auth_keys_request_dto_dict = save_auth_keys_request_dto_instance.to_dict()
# create an instance of SaveAuthKeysRequestDto from a dict
save_auth_keys_request_dto_from_dict = SaveAuthKeysRequestDto.from_dict(save_auth_keys_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


