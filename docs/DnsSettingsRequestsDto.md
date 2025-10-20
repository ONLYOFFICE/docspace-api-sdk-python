# DnsSettingsRequestsDto
The request parameters for managing the DNS (Domain Name System) settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_name** | **str** | The DNS (Domain Name System) configuration name. | [optional] 
**enable** | **bool** | Specifies whether the DNS settings are enabled. | [optional] 

## Example

```python
from docspace_api_sdk.models.dns_settings_requests_dto import DnsSettingsRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSettingsRequestsDto from a JSON string
dns_settings_requests_dto_instance = DnsSettingsRequestsDto.from_json(json)
# print the JSON string representation of the object
print(DnsSettingsRequestsDto.to_json())

# convert the object into a dict
dns_settings_requests_dto_dict = dns_settings_requests_dto_instance.to_dict()
# create an instance of DnsSettingsRequestsDto from a dict
dns_settings_requests_dto_from_dict = DnsSettingsRequestsDto.from_dict(dns_settings_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


