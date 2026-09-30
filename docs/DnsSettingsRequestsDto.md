# DnsSettingsRequestsDto
The custom domain the portal answers on, and whether that mapping is in force.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_name** | **str** | The domain the portal is to be reachable under, as a bare hostname without a scheme. It must not collide with  the reserved base domain of the installation, and a name that fails validation is refused without disturbing  the mapping in force. It is read only while `enable` is true. | [optional] 
**enable** | **bool** | Whether the custom domain is put in force. Setting it false clears the mapping and ignores `dnsName`; setting  it true also stops the previous domain from answering and rewrites any Content Security Policy entry that  named it. | [optional] 

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


