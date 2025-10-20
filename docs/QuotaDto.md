# QuotaDto
The quota information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The quota ID. | 
**title** | **str** | The quota title. | 
**price** | [**PriceDto**](PriceDto.md) |  | 
**non_profit** | **bool** | Specifies if the quota is nonprofit or not. | 
**free** | **bool** | Specifies if the quota is free or not. | 
**trial** | **bool** | Specifies if the quota is trial or not. | 
**features** | [**List[TenantQuotaFeatureDto]**](TenantQuotaFeatureDto.md) | The list of tenant quota features. | 
**users_quota** | [**TenantEntityQuotaSettings**](TenantEntityQuotaSettings.md) |  | [optional] 
**rooms_quota** | [**TenantEntityQuotaSettings**](TenantEntityQuotaSettings.md) |  | [optional] 
**tenant_custom_quota** | [**TenantQuotaSettings**](TenantQuotaSettings.md) |  | [optional] 
**due_date** | **datetime** | The due date. | [optional] 

## Example

```python
from docspace_api_sdk.models.quota_dto import QuotaDto

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaDto from a JSON string
quota_dto_instance = QuotaDto.from_json(json)
# print the JSON string representation of the object
print(QuotaDto.to_json())

# convert the object into a dict
quota_dto_dict = quota_dto_instance.to_dict()
# create an instance of QuotaDto from a dict
quota_dto_from_dict = QuotaDto.from_dict(quota_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


