# SsoBindingTypeDto
The SAML bindings the SSO settings accept.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**saml20_http_post** | **str** | The SAML 2.0 HTTP POST binding, which carries the request in a self-submitting form. It is what the  built-in configuration uses and the one to pick when requests are signed, since it has no length limit. | [optional] [readonly] 
**saml20_http_redirect** | **str** | The SAML 2.0 HTTP redirect binding, which carries the request in the query string and is therefore bound  by the length a URL may have. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.sso_binding_type_dto import SsoBindingTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of SsoBindingTypeDto from a JSON string
sso_binding_type_dto_instance = SsoBindingTypeDto.from_json(json)
# print the JSON string representation of the object
print(SsoBindingTypeDto.to_json())

# convert the object into a dict
sso_binding_type_dto_dict = sso_binding_type_dto_instance.to_dict()
# create an instance of SsoBindingTypeDto from a dict
sso_binding_type_dto_from_dict = SsoBindingTypeDto.from_dict(sso_binding_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


