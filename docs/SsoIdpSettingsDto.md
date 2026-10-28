# SsoIdpSettingsDto
The identity provider the portal trusts: its entity id, endpoints and bindings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | The entity ID. | [optional] 
**sso_url** | **str** | The SSO URL. | [optional] 
**sso_binding** | **str** | The SSO binding. | [optional] 
**slo_url** | **str** | The SLO URL. | [optional] 
**slo_binding** | **str** | The SLO binding. | [optional] 
**name_id_format** | **str** | The name ID format. | [optional] 

## Example

```python
from docspace_api_sdk.models.sso_idp_settings_dto import SsoIdpSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SsoIdpSettingsDto from a JSON string
sso_idp_settings_dto_instance = SsoIdpSettingsDto.from_json(json)
# print the JSON string representation of the object
print(SsoIdpSettingsDto.to_json())

# convert the object into a dict
sso_idp_settings_dto_dict = sso_idp_settings_dto_instance.to_dict()
# create an instance of SsoIdpSettingsDto from a dict
sso_idp_settings_dto_from_dict = SsoIdpSettingsDto.from_dict(sso_idp_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


