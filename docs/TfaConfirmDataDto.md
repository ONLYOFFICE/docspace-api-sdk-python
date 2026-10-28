# TfaConfirmDataDto
The confirmation link the caller has to follow to pass the two-factor step, and the cookie it depends on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The link to open. Its `type` shows which step it is: phone activation or phone authorization for the SMS  method, and authenticator activation or re-verification for the application method. The whole body is empty  when the portal requires no second factor of the caller. | [optional] 
**cookie_name** | **str** | The name of the confirmation cookie the link is validated against. It is filled in only for the  authenticator-application method; the SMS method returns `url` alone. | [optional] 
**cookie_value** | **str** | The value of that cookie. The call already set it on the response, so it is repeated here only for a client  that does not keep cookies of its own; it is filled in under the same condition as `cookieName`, and a  later call to this operation replaces it. | [optional] 

## Example

```python
from docspace_api_sdk.models.tfa_confirm_data_dto import TfaConfirmDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of TfaConfirmDataDto from a JSON string
tfa_confirm_data_dto_instance = TfaConfirmDataDto.from_json(json)
# print the JSON string representation of the object
print(TfaConfirmDataDto.to_json())

# convert the object into a dict
tfa_confirm_data_dto_dict = tfa_confirm_data_dto_instance.to_dict()
# create an instance of TfaConfirmDataDto from a dict
tfa_confirm_data_dto_from_dict = TfaConfirmDataDto.from_dict(tfa_confirm_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


