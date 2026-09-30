# ThirdPartyRequestDto
The credentials and the title of a third-party storage account to connect or to re-authenticate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The address of the storage server to connect to. It is needed by the WebDAV presets whose server is not known  in advance (`WebDav`, `Nextcloud`, `ownCloud`), where it points at the WebDAV endpoint of that server, and by  `SharePoint`; the presets with a fixed address and the OAuth services ignore it. | [optional] 
**login** | **str** | The account name at the storage service, used by the services that authenticate by login and password. A login  sent without a password is rejected as an invalid request. | [optional] 
**password** | **str** | The password, or the application password, for `login` at the storage service. Either this or `token` has to  be sent, and the credentials are verified against the service before the account is saved. | [optional] 
**token** | **str** | The OAuth 2.0 authorization code from the consent screen of `Box`, `DropboxV2`, `GoogleDrive` or `OneDrive` -  not an access token: the portal exchanges the code for its own token and keeps that. The client ID and  redirect URL the consent screen URL is built from come from `GET api/2.0/files/thirdparty/capabilities`. | [optional] 
**customer_title** | **str** | The name the connected account is shown under in the portal. Characters that a folder title cannot hold are  replaced and the value is truncated, and a title that comes out of that empty is refused. | 
**provider_key** | **str** | The storage service to connect, as the `key` of `GET api/2.0/files/thirdparty/providers`; the value is matched  case-insensitively. `Nextcloud` and `ownCloud` are presets over WebDAV and are stored and reported back as  `WebDav`. | 
**provider_id** | **int** | The account to re-authenticate instead of connecting a new one, as `providerId` of  `GET api/2.0/files/thirdparty`; both a number and its decimal string form are accepted. For an account  attached to the Rooms section only the credentials are applied, and its title and server address are kept. | [optional] 

## Example

```python
from docspace_api_sdk.models.third_party_request_dto import ThirdPartyRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyRequestDto from a JSON string
third_party_request_dto_instance = ThirdPartyRequestDto.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyRequestDto.to_json())

# convert the object into a dict
third_party_request_dto_dict = third_party_request_dto_instance.to_dict()
# create an instance of ThirdPartyRequestDto from a dict
third_party_request_dto_from_dict = ThirdPartyRequestDto.from_dict(third_party_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


