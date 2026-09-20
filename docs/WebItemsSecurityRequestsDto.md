# WebItemsSecurityRequestsDto
The modules switched on or off together, one entry per module.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ItemKeyValuePairStringBoolean]**](ItemKeyValuePairStringBoolean.md) | The modules to switch, each entry pairing a module GUID as its `key` with the new enabled flag as its  `value`. A key that is not a GUID fails the whole request as invalid, and a module listed twice is applied  once, from its first entry. No allow-list travels here: switching a product module on restores the users and  groups it was last restricted to, and everything else is stored as a plain allow or deny for everyone. | [optional] 

## Example

```python
from docspace_api_sdk.models.web_items_security_requests_dto import WebItemsSecurityRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebItemsSecurityRequestsDto from a JSON string
web_items_security_requests_dto_instance = WebItemsSecurityRequestsDto.from_json(json)
# print the JSON string representation of the object
print(WebItemsSecurityRequestsDto.to_json())

# convert the object into a dict
web_items_security_requests_dto_dict = web_items_security_requests_dto_instance.to_dict()
# create an instance of WebItemsSecurityRequestsDto from a dict
web_items_security_requests_dto_from_dict = WebItemsSecurityRequestsDto.from_dict(web_items_security_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


