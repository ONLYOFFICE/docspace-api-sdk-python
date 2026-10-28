# ThirdPartyAccountDto
A third-party storage account the caller has connected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporate** | **bool** | Whether the account is attached to the legacy Common section, which is the case only for accounts inherited  from an older portal. | [optional] 
**rooms_storage** | **bool** | Whether the account is attached to the Rooms section, room templates and the archive counted in. This is where  `POST api/2.0/files/thirdparty` puts every account it connects. | [optional] 
**customer_title** | **str** | The name the account is shown under in the portal, as it was saved when the account was connected. | [optional] 
**provider_id** | **int** | The account ID to send to `DELETE api/2.0/files/thirdparty/{providerId}`, or as `providerId` to  re-authenticate the account. | [optional] 
**provider_key** | **str** | The storage service behind the account. `WebDav` stands for every WebDAV preset, so it does not tell which of  them was chosen when the account was connected. | [optional] 

## Example

```python
from docspace_api_sdk.models.third_party_account_dto import ThirdPartyAccountDto

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyAccountDto from a JSON string
third_party_account_dto_instance = ThirdPartyAccountDto.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyAccountDto.to_json())

# convert the object into a dict
third_party_account_dto_dict = third_party_account_dto_instance.to_dict()
# create an instance of ThirdPartyAccountDto from a dict
third_party_account_dto_from_dict = ThirdPartyAccountDto.from_dict(third_party_account_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


