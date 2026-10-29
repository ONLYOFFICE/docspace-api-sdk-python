# CreateServiceLimitRequestDto
The spending limit to create on the AI services: for the portal as a whole, for every user, or for one user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**ServiceLimitScope**](ServiceLimitScope.md) | Whom the limit applies to. | [optional] 
**user_id** | **UUID** | The ID of the portal user a personal limit is set for, as returned in `id` by the people operations. | [optional] 
**amount_value** | **float** | The most money the AI services may cost per period, in their currency, which cannot be chosen. Zero blocks the  AI services completely. | [optional] 
**quantity_value** | **int** | The largest quantity the AI services may consume per period, in their common unit. Zero blocks the AI services  completely. | [optional] 
**period** | [**ServiceLimitPeriod**](ServiceLimitPeriod.md) | The window the thresholds apply to, in UTC. A day, week or month is calendar-aligned rather than rolling - a  daily limit resets at midnight UTC, a weekly one on Monday - while a lifetime limit counts from its creation and  never resets. | [optional] 

## Example

```python
from docspace_api_sdk.models.create_service_limit_request_dto import CreateServiceLimitRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServiceLimitRequestDto from a JSON string
create_service_limit_request_dto_instance = CreateServiceLimitRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateServiceLimitRequestDto.to_json())

# convert the object into a dict
create_service_limit_request_dto_dict = create_service_limit_request_dto_instance.to_dict()
# create an instance of CreateServiceLimitRequestDto from a dict
create_service_limit_request_dto_from_dict = CreateServiceLimitRequestDto.from_dict(create_service_limit_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


