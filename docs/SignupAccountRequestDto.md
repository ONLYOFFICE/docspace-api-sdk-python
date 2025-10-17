# SignupAccountRequestDto
The request parameters for creating a third-party account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_type** | [**EmployeeType**](EmployeeType.md) |  | [optional] 
**first_name** | **str** | The user first name. | [optional] 
**last_name** | **str** | The user last name. | [optional] 
**email** | **str** | The user email address. | [optional] 
**password_hash** | **str** | The user password hash. | [optional] 
**key** | **str** | The user link key. | 
**culture** | **str** | The user culture code. | [optional] 
**serialized_profile** | **str** | The third-party profile in the serialized format | 

## Example

```python
from docspace_api_sdk.models.signup_account_request_dto import SignupAccountRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SignupAccountRequestDto from a JSON string
signup_account_request_dto_instance = SignupAccountRequestDto.from_json(json)
# print the JSON string representation of the object
print(SignupAccountRequestDto.to_json())

# convert the object into a dict
signup_account_request_dto_dict = signup_account_request_dto_instance.to_dict()
# create an instance of SignupAccountRequestDto from a dict
signup_account_request_dto_from_dict = SignupAccountRequestDto.from_dict(signup_account_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


