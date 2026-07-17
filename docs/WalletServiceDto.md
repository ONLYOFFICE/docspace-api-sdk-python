# WalletServiceDto
The wallet service information.

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
**ai_agents_quota** | [**TenantEntityQuotaSettings**](TenantEntityQuotaSettings.md) |  | [optional] 
**tenant_custom_quota** | [**TenantQuotaSettings**](TenantQuotaSettings.md) |  | [optional] 
**due_date** | **datetime** | The due date. | [optional] 
**inner_services** | [**List[WalletServiceDto]**](WalletServiceDto.md) | The list of inner services. | [optional] 
**service_name** | **str** | The service name. | [optional] 

## Example

```python
from docspace_api_sdk.models.wallet_service_dto import WalletServiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of WalletServiceDto from a JSON string
wallet_service_dto_instance = WalletServiceDto.from_json(json)
# print the JSON string representation of the object
print(WalletServiceDto.to_json())

# convert the object into a dict
wallet_service_dto_dict = wallet_service_dto_instance.to_dict()
# create an instance of WalletServiceDto from a dict
wallet_service_dto_from_dict = WalletServiceDto.from_dict(wallet_service_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


