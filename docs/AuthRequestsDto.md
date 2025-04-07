# AuthRequestsDto

Authentication request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | Username / email | [optional] 
**password** | **str** | Password | [optional] 
**password_hash** | **str** | Password hash | [optional] 
**provider** | **str** | Provider type | [optional] 
**access_token** | **str** | Provider access token | [optional] 
**serialized_profile** | **str** | Serialized user profile | [optional] 
**code** | **str** | Two-factor authentication code | [optional] 
**code_o_auth** | **str** | Code for getting a token | [optional] 
**session** | **bool** | Session based authentication or not | [optional] 
**confirm_data** | [**ConfirmData**](ConfirmData.md) |  | [optional] 
**recaptcha_type** | [**RecaptchaType**](RecaptchaType.md) |  | [optional] 
**recaptcha_response** | **str** | reCAPTCHA response | [optional] 
**culture** | **str** | Culture | [optional] 

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


