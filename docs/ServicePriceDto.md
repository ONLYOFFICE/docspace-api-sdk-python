# ServicePriceDto
Represents a price of the service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The price unique identifier. | [optional] 
**account_number** | **int** | The account number. | [optional] 
**service_id** | **int** | The service ID. | [optional] 
**time_unit** | [**PriceTimeUnit**](PriceTimeUnit.md) | The time unit the price is bound to. | [optional] 
**cost_price** | **float** | The cost price. | [optional] 
**extra_charge** | **float** | The extra charge added to the cost price. | [optional] 
**service_price** | **float** | The resulting service price. | [optional] 
**quota** | **float** | The quota the price is set for. | [optional] 
**time_bound** | [**TimeBoundDto**](TimeBoundDto.md) | The period the price is effective in. | [optional] 
**status** | [**PriceStatus**](PriceStatus.md) | The price status. | [optional] 
**created** | **datetime** | The date and time when the price was created. | [optional] 
**discount_category_id** | **int** | The discount category ID. | [optional] 
**discount_category** | [**DiscountCategoryDto**](DiscountCategoryDto.md) | The discount category. | [optional] 

## Example

```python
from docspace_api_sdk.models.service_price_dto import ServicePriceDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePriceDto from a JSON string
service_price_dto_instance = ServicePriceDto.from_json(json)
# print the JSON string representation of the object
print(ServicePriceDto.to_json())

# convert the object into a dict
service_price_dto_dict = service_price_dto_instance.to_dict()
# create an instance of ServicePriceDto from a dict
service_price_dto_from_dict = ServicePriceDto.from_dict(service_price_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


