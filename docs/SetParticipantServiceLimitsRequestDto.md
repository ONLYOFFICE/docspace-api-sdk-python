# SetParticipantServiceLimitsRequestDto
The personal spending limit on the AI services to set for each of several portal users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[UUID]** | The IDs of the portal users the limit is set for, as returned in `id` by the people operations. | 
**amount_value** | **float** | The most money the AI services may cost each user per period, in their currency, which cannot be chosen. Zero  blocks the AI services completely. | [optional] 
**quantity_value** | **int** | The largest quantity the AI services may consume per period for each user, in their common unit. Zero blocks the  AI services completely. | [optional] 
**period** | [**ServiceLimitPeriod**](ServiceLimitPeriod.md) | The window the thresholds apply to, in UTC. A day, week or month is calendar-aligned rather than rolling - a  daily limit resets at midnight UTC, a weekly one on Monday - while a lifetime limit counts from its creation and  never resets. | [optional] 

## Example

```python
from docspace_api_sdk.models.set_participant_service_limits_request_dto import SetParticipantServiceLimitsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetParticipantServiceLimitsRequestDto from a JSON string
set_participant_service_limits_request_dto_instance = SetParticipantServiceLimitsRequestDto.from_json(json)
# print the JSON string representation of the object
print(SetParticipantServiceLimitsRequestDto.to_json())

# convert the object into a dict
set_participant_service_limits_request_dto_dict = set_participant_service_limits_request_dto_instance.to_dict()
# create an instance of SetParticipantServiceLimitsRequestDto from a dict
set_participant_service_limits_request_dto_from_dict = SetParticipantServiceLimitsRequestDto.from_dict(set_participant_service_limits_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


