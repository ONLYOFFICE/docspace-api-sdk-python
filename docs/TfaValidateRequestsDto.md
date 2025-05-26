# TfaValidateRequestsDto

The request parameters for validating the two-factor authentication codes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The verification code provided by the user. | 

## Example

```python
from docspace.models.tfa_validate_requests_dto import TfaValidateRequestsDto

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


