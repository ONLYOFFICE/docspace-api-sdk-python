# SsoSettingsRequestsDto
The whole SAML Single Sign-On configuration of the portal, carried as a serialised JSON object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serialize_settings** | **str** | The configuration object serialised to a JSON string, not a nested object. It is the complete configuration  rather than a patch - fields left out are stored empty - so start from `GET api/2.0/settings/ssov2` or  `GET api/2.0/settings/ssov2/default` and send back a changed copy. The identity provider entity ID and  sign-in URL are required, the sign-in and sign-out URLs have to be absolute `http` or `https` addresses, and  the attribute mapping has to name the first name, last name and email fields; the values each SAML field  accepts are listed by `GET api/2.0/settings/ssov2/constants`. An empty string, or a string that carries no  configuration object, is refused with 400. | 

## Example

```python
from docspace_api_sdk.models.sso_settings_requests_dto import SsoSettingsRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSettingsRequestsDto from a JSON string
sso_settings_requests_dto_instance = SsoSettingsRequestsDto.from_json(json)
# print the JSON string representation of the object
print(SsoSettingsRequestsDto.to_json())

# convert the object into a dict
sso_settings_requests_dto_dict = sso_settings_requests_dto_instance.to_dict()
# create an instance of SsoSettingsRequestsDto from a dict
sso_settings_requests_dto_from_dict = SsoSettingsRequestsDto.from_dict(sso_settings_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


