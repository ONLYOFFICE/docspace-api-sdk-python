# TfaValidateRequestsDto
The one-time code that completes a pending two-factor step, and how long the resulting sign-in lasts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code to check - either one from the authenticator application or one of the account's unused backup  codes, which is spent by the check. A wrong code is refused with 400 and counts against the portal login  attempt limit. | 
**session** | **bool** | Whether the sign-in that follows is tied to the browser session. When it is, the session ends with the  browser rather than lasting for the portal session lifetime. | [optional] 

## Example

```python
from docspace_api_sdk.models.tfa_validate_requests_dto import TfaValidateRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TfaValidateRequestsDto from a JSON string
tfa_validate_requests_dto_instance = TfaValidateRequestsDto.from_json(json)
# print the JSON string representation of the object
print(TfaValidateRequestsDto.to_json())

# convert the object into a dict
tfa_validate_requests_dto_dict = tfa_validate_requests_dto_instance.to_dict()
# create an instance of TfaValidateRequestsDto from a dict
tfa_validate_requests_dto_from_dict = TfaValidateRequestsDto.from_dict(tfa_validate_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


