# PaymentSettingsDto
The payment settings parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales_email** | **str** | The email address for sales inquiries and support. | 
**feedback_and_support_url** | **str** | The URL for accessing the feedback and support resources. | [optional] 
**buy_url** | **str** | The URL for purchasing or upgrading the product. | 
**standalone** | **bool** | Indicates whether the system is running in standalone mode. | 
**current_license** | [**CurrentLicenseInfo**](CurrentLicenseInfo.md) |  | 
**max** | **int** | The maximum quota quantity. | 

## Example

```python
from docspace_api_sdk.models.payment_settings_dto import PaymentSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSettingsDto from a JSON string
payment_settings_dto_instance = PaymentSettingsDto.from_json(json)
# print the JSON string representation of the object
print(PaymentSettingsDto.to_json())

# convert the object into a dict
payment_settings_dto_dict = payment_settings_dto_instance.to_dict()
# create an instance of PaymentSettingsDto from a dict
payment_settings_dto_from_dict = PaymentSettingsDto.from_dict(payment_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


