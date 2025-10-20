# SsoIdpSettings
The SSO IdP settings.

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
from docspace_api_sdk.models.sso_idp_settings import SsoIdpSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SsoIdpSettings from a JSON string
sso_idp_settings_instance = SsoIdpSettings.from_json(json)
# print the JSON string representation of the object
print(SsoIdpSettings.to_json())

# convert the object into a dict
sso_idp_settings_dict = sso_idp_settings_instance.to_dict()
# create an instance of SsoIdpSettings from a dict
sso_idp_settings_from_dict = SsoIdpSettings.from_dict(sso_idp_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


