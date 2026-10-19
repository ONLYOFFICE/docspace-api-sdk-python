# TenantAiAccessSettingsRequestDto
Whether AI functionality is available on the portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether AI is available on the portal at all - chat, agents and vectorization together. Switching it off  hides the AI Agents folder and makes every AI endpoint unreachable for all members at once, not only for the  caller, and the change is pushed to connected clients rather than waiting for their next request. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_ai_access_settings_request_dto import TenantAiAccessSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAiAccessSettingsRequestDto from a JSON string
tenant_ai_access_settings_request_dto_instance = TenantAiAccessSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(TenantAiAccessSettingsRequestDto.to_json())

# convert the object into a dict
tenant_ai_access_settings_request_dto_dict = tenant_ai_access_settings_request_dto_instance.to_dict()
# create an instance of TenantAiAccessSettingsRequestDto from a dict
tenant_ai_access_settings_request_dto_from_dict = TenantAiAccessSettingsRequestDto.from_dict(tenant_ai_access_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


