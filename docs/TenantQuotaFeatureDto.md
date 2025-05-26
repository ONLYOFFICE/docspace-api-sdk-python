# TenantQuotaFeatureDto

The tenant quota feature parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the tenant quota feature. | [optional] 
**title** | **str** | The title of the tenant quota feature. | [optional] 
**image** | **str** | The image URL of the tenant quota feature. | [optional] 
**value** | **object** | The value of the tenant quota feature. | [optional] 
**type** | **str** | The type of the tenant quota feature. | [optional] 
**used** | [**FeatureUsedDto**](FeatureUsedDto.md) |  | [optional] 
**price_title** | **str** | The price title of the tenant quota feature. | [optional] 

## Example

```python
from docspace.models.tenant_quota_feature_dto import TenantQuotaFeatureDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantQuotaFeatureDto from a JSON string
tenant_quota_feature_dto_instance = TenantQuotaFeatureDto.from_json(json)
# print the JSON string representation of the object
print(TenantQuotaFeatureDto.to_json())

# convert the object into a dict
tenant_quota_feature_dto_dict = tenant_quota_feature_dto_instance.to_dict()
# create an instance of TenantQuotaFeatureDto from a dict
tenant_quota_feature_dto_from_dict = TenantQuotaFeatureDto.from_dict(tenant_quota_feature_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


