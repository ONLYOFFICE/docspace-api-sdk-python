# CapabilitiesDto
The capabilities parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ldap_enabled** | **bool** | Specifies if the LDAP settings are enabled or not. | [optional] 
**ldap_domain** | **str** | The LDAP domain. | [optional] 
**providers** | **List[str]** | The list of providers. | [optional] 
**sso_label** | **str** | The SP login label. | [optional] 
**oauth_enabled** | **bool** | Specifies if OAuth is enabled or not. | [optional] 
**sso_url** | **str** | The SSO URL. If this parameter is empty, then the SSO settings are disabled. | [optional] 
**identity_server_enabled** | **bool** | Specifies if identity server is enabled or not | [optional] 

## Example

```python
from docspace-api-sdk.models.capabilities_dto import CapabilitiesDto

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


