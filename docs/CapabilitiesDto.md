# CapabilitiesDto
The sign-in methods this portal offers, as a login client needs them before anyone has signed in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ldap_enabled** | **bool** | Whether members may sign in with their directory credentials. It is `false` both when LDAP sign-in is  switched off and when the pricing plan or the installation does not include it, and also when the settings  could not be read at all - a `false` here means the method is not offered, never that it is unknown. | 
**ldap_domain** | **str** | The directory domain members authenticate against, to be shown next to the login field. It is empty  whenever `ldapEnabled` is `false`, and also while the portal has not completed a directory synchronisation. | [optional] 
**providers** | **List[str]** | The keys of the external identity providers to offer, ordered for the country the caller's IP address  resolves to and reduced to those this installation has credentials for. Pass one of them as `provider` to  `POST api/2.0/authentication`. An empty list means external sign-in is not on offer. | 
**sso_label** | **str** | The caption for the single sign-on button in the portal language, empty whenever `ssoUrl` is. | 
**oauth_enabled** | **bool** | Whether external identity providers may be used on this portal at all. While it is `false`, `providers` is  empty because the list is not even assembled. | 
**sso_url** | **str** | The address to send the browser to for SAML single sign-on. It is empty when single sign-on is not on  offer, which is the one thing to test - there is no separate flag for it. | 
**identity_server_enabled** | **bool** | Whether the installation exposes its built-in identity server, which is what the portal's own OAuth  applications authenticate against. It concerns third-party applications signing in to the portal, not  portal members signing in to an external provider - that is `providers`. | 

## Example

```python
from docspace_api_sdk.models.capabilities_dto import CapabilitiesDto

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesDto from a JSON string
capabilities_dto_instance = CapabilitiesDto.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesDto.to_json())

# convert the object into a dict
capabilities_dto_dict = capabilities_dto_instance.to_dict()
# create an instance of CapabilitiesDto from a dict
capabilities_dto_from_dict = CapabilitiesDto.from_dict(capabilities_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


