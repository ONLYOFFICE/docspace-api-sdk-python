# EmailValidationKeyModel

The confirmation email parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The email validation key. | [optional] 
**empl_type** | [**EmployeeType**](EmployeeType.md) |  | [optional] 
**email** | **str** | The email address. | [optional] 
**ui_d** | **str** | The user ID. | [optional] 
**type** | [**ConfirmType**](ConfirmType.md) |  | [optional] 
**first** | **str** | Specifies whether it is the first time account access or not. | [optional] 
**room_id** | **str** | The room ID. | [optional] 

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


