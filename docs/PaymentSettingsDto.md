# PaymentSettingsDto
Where to buy or extend the portal's subscription, and what the subscription in force looks like.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales_email** | **str** | The vendor mailbox to write to about buying, extending or changing the subscription, picked for the portal  language. It is not the portal's own support address. | 
**feedback_and_support_url** | **str** | Not populated: nothing fills this field in, so it always comes back empty. The help and support addresses  live in `externalResources` of `GET api/2.0/settings` instead. | [optional] 
**buy_url** | **str** | The vendor page for buying or extending the subscription, chosen for the licence kind the installation was  built for and for the portal language. It is a page for a person to open, not an API to call. | 
**standalone** | **bool** | Whether this is a server installation someone administers themselves rather than a portal in the cloud,  which decides whether payment means uploading a licence file or a subscription in the vendor's store. | 
**current_license** | [**CurrentLicenseInfo**](CurrentLicenseInfo.md) | The subscription in force, reduced to the two facts a payment page needs. | 
**max** | **int** | The largest quantity of a paid item - members, storage - that may be bought in one go, `999` unless the  installation configures another cap. It bounds a single purchase, not the total a portal may hold. | 

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


