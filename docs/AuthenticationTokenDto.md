# AuthenticationTokenDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Authentication token | [optional] 
**expires** | **datetime** | Token expiration time | [optional] 
**sms** | **bool** | Specifies if the authentication code is sent by SMS or not | [optional] 
**phone_noise** | **str** | Phone number | [optional] 
**tfa** | **bool** | Specifies if the two-factor application is used or not | [optional] 
**tfa_key** | **str** | Two-factor authentication key | [optional] 
**confirm_url** | **str** | Confirmation email URL | [optional] 

## Example

```python
from docspace.models.authentication_token_dto import AuthenticationTokenDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationTokenDto from a JSON string
authentication_token_dto_instance = AuthenticationTokenDto.from_json(json)
# print the JSON string representation of the object
print(AuthenticationTokenDto.to_json())

# convert the object into a dict
authentication_token_dto_dict = authentication_token_dto_instance.to_dict()
# create an instance of AuthenticationTokenDto from a dict
authentication_token_dto_from_dict = AuthenticationTokenDto.from_dict(authentication_token_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


