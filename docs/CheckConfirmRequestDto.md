# CheckConfirmRequestDto
The confirmation link parameters to check.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The email validation key. | [optional] 
**empl_type** | [**EmployeeType**](EmployeeType.md) | The user type. | [optional] 
**email** | **str** | The email address. | [optional] 
**enc_email** | **str** | The encrypted email address. | [optional] 
**ui_d** | **UUID** | The user ID. | [optional] 
**type** | [**ConfirmType**](ConfirmType.md) | The confirmation email type. | [optional] 
**first** | **str** | Specifies whether it is the first time account access or not. | [optional] 
**room_id** | **str** | The room ID. | [optional] 

## Example

```python
from docspace_api_sdk.models.check_confirm_request_dto import CheckConfirmRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CheckConfirmRequestDto from a JSON string
check_confirm_request_dto_instance = CheckConfirmRequestDto.from_json(json)
# print the JSON string representation of the object
print(CheckConfirmRequestDto.to_json())

# convert the object into a dict
check_confirm_request_dto_dict = check_confirm_request_dto_instance.to_dict()
# create an instance of CheckConfirmRequestDto from a dict
check_confirm_request_dto_from_dict = CheckConfirmRequestDto.from_dict(check_confirm_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


