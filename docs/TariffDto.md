# TariffDto
The subscription this portal runs on: its state, the end of the current period, and the quotas it is made of.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_source** | **bool** | Whether the installation runs the open-source build, which has no paid plan at all. This flag and the two  below describe the build rather than the subscription, and all three are left empty for a caller without  the portal-settings right. | [optional] 
**enterprise** | **bool** | Whether the installation runs on an Enterprise licence file, which is what makes the licence operations  under `api/2.0/settings/license` usable. | [optional] 
**developer** | **bool** | Whether the installation runs on a Developer licence, an Enterprise licence meant for embedding rather  than for production use. | [optional] 
**id** | **int** | The identifier of the subscription record itself, for quoting when a charge has to be traced. It is filled  in for a caller with the portal-settings right only, and nothing accepts it as an argument. | [optional] 
**state** | [**TariffState**](TariffState.md) | How the subscription stands: on trial, paid, inside the grace period that follows the due date, or unpaid.  It is the one field every caller gets, whatever their role, so a client can warn about payment without  needing administrator rights. | [optional] 
**due_date** | [**ApiDateTime**](ApiDateTime.md) | When the current period ends, in the portal time zone. It is filled in for a room or DocSpace  administrator only, and set to the largest value a date can hold for a subscription that never ends. | [optional] 
**delay_due_date** | [**ApiDateTime**](ApiDateTime.md) | When the grace period after `dueDate` runs out and the portal is cut off, in the portal time zone. Filled  in under the same conditions as `dueDate`, and equal to it when the plan grants no grace period. | [optional] 
**license_date** | [**ApiDateTime**](ApiDateTime.md) | When the licence file behind the subscription was issued, in the portal time zone. It is meaningful on a  server installation and filled in for a caller with the portal-settings right only. | [optional] 
**customer_id** | **str** | The account in the billing system the subscription is charged to, empty for a portal that has never been  billed. Filled in for a caller with the portal-settings right only. | [optional] 
**quotas** | [**List[TariffQuotaDto]**](TariffQuotaDto.md) | The quotas the subscription is made of - the plan itself and its add-ons - with the overdue ones listed  alongside the current ones, so an entry here is not proof that it is still being paid for; read each  entry's own `state` for that. Filled in for a caller with the portal-settings right only. | [optional] 

## Example

```python
from docspace_api_sdk.models.tariff_dto import TariffDto

# TODO update the JSON string below
json = "{}"
# create an instance of TariffDto from a JSON string
tariff_dto_instance = TariffDto.from_json(json)
# print the JSON string representation of the object
print(TariffDto.to_json())

# convert the object into a dict
tariff_dto_dict = tariff_dto_instance.to_dict()
# create an instance of TariffDto from a dict
tariff_dto_from_dict = TariffDto.from_dict(tariff_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


