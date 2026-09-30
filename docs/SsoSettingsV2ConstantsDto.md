# SsoSettingsV2ConstantsDto
The SSO settings constants: every value the settings accept, by name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sso_name_id_format_type** | [**SsoNameIdFormatTypeDto**](SsoNameIdFormatTypeDto.md) | The values the `nameIdFormat` of the identity provider settings accepts. The built-in configuration uses  the SAML 2.0 transient format. | [optional] 
**sso_binding_type** | [**SsoBindingTypeDto**](SsoBindingTypeDto.md) | The values the `ssoBinding` and `sloBinding` of the identity provider settings accept - how the portal  sends its sign-in and sign-out requests. The built-in configuration uses HTTP POST for both. | [optional] 
**sso_signing_algorithm_type** | [**SsoSigningAlgorithmTypeDto**](SsoSigningAlgorithmTypeDto.md) | The values the `signingAlgorithm` of the service provider certificate and the `verifyAlgorithm` of the  identity provider certificate accept. The built-in configuration uses RSA-SHA1 for both. | [optional] 
**sso_encrypt_algorithm_type** | [**SsoEncryptAlgorithmTypeDto**](SsoEncryptAlgorithmTypeDto.md) | The values the `encryptAlgorithm` and `decryptAlgorithm` of the certificate settings accept. The built-in  configuration uses AES-128 everywhere. | [optional] 
**sso_sp_certificate_action_type** | [**SsoSpCertificateActionTypeDto**](SsoSpCertificateActionTypeDto.md) | The values the `action` of a service provider certificate accepts, which is what the portal's own key  pair may be used for. | [optional] 
**sso_idp_certificate_action_type** | [**SsoIdpCertificateActionTypeDto**](SsoIdpCertificateActionTypeDto.md) | The values the `action` of an identity provider certificate accepts, which is what the provider's  certificate may be used for - the mirror image of the service provider actions. | [optional] 

## Example

```python
from docspace_api_sdk.models.sso_settings_v2_constants_dto import SsoSettingsV2ConstantsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSettingsV2ConstantsDto from a JSON string
sso_settings_v2_constants_dto_instance = SsoSettingsV2ConstantsDto.from_json(json)
# print the JSON string representation of the object
print(SsoSettingsV2ConstantsDto.to_json())

# convert the object into a dict
sso_settings_v2_constants_dto_dict = sso_settings_v2_constants_dto_instance.to_dict()
# create an instance of SsoSettingsV2ConstantsDto from a dict
sso_settings_v2_constants_dto_from_dict = SsoSettingsV2ConstantsDto.from_dict(sso_settings_v2_constants_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


