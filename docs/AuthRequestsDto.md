# AuthRequestsDto

The parameters required for the user authentication requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | The username or email used for authentication. | [optional] 
**password** | **str** | The password in plain text for user authentication. | [optional] 
**password_hash** | **str** | The hashed password for secure verification. | [optional] 
**provider** | **str** | The type of authentication provider (e.g., internal, Google, Azure). | [optional] 
**access_token** | **str** | The access token used for authentication with external providers. | [optional] 
**serialized_profile** | **str** | The serialized user profile data, if applicable. | [optional] 
**code** | **str** | The code for two-factor authentication. | [optional] 
**code_o_auth** | **str** | The authorization code used for obtaining OAuth tokens. | [optional] 
**session** | **bool** | Specifies whether the authentication is session-based. | [optional] 
**confirm_data** | [**ConfirmData**](ConfirmData.md) |  | [optional] 
**recaptcha_type** | [**RecaptchaType**](RecaptchaType.md) |  | [optional] 
**recaptcha_response** | **str** | The user&#39;s response to the CAPTCHA challenge. | [optional] 
**culture** | **str** | The culture code for localization during authentication. | [optional] 

## Example

```python
from docspace.models.auth_requests_dto import AuthRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRequestsDto from a JSON string
auth_requests_dto_instance = AuthRequestsDto.from_json(json)
# print the JSON string representation of the object
print(AuthRequestsDto.to_json())

# convert the object into a dict
auth_requests_dto_dict = auth_requests_dto_instance.to_dict()
# create an instance of AuthRequestsDto from a dict
auth_requests_dto_from_dict = AuthRequestsDto.from_dict(auth_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


