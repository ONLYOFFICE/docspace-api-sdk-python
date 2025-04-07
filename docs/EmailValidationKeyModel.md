# EmailValidationKeyModel

Confirmation email parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key | [optional] 
**empl_type** | [**EmployeeType**](EmployeeType.md) |  | [optional] 
**email** | **str** | Email | [optional] 
**ui_d** | **str** | User ID | [optional] 
**type** | [**ConfirmType**](ConfirmType.md) |  | [optional] 
**first** | **str** | Access an account for the first time or not | [optional] 
**room_id** | **str** | Room ID | [optional] 

## Example

```python
from docspace.models.email_validation_key_model import EmailValidationKeyModel

# TODO update the JSON string below
json = "{}"
# create an instance of EmailValidationKeyModel from a JSON string
email_validation_key_model_instance = EmailValidationKeyModel.from_json(json)
# print the JSON string representation of the object
print(EmailValidationKeyModel.to_json())

# convert the object into a dict
email_validation_key_model_dict = email_validation_key_model_instance.to_dict()
# create an instance of EmailValidationKeyModel from a dict
email_validation_key_model_from_dict = EmailValidationKeyModel.from_dict(email_validation_key_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


