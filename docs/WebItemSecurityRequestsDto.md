# WebItemSecurityRequestsDto
The access rule stored for one portal module: whether it may be opened, and by whom.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The module the rule applies to, given as a GUID. A value that is not a GUID fails the request as invalid. | 
**enabled** | **bool** | Whether the module may be opened. It decides the outcome only while `subjects` names somebody: an empty  `subjects` array is stored as access for everyone whatever this flag says. | [optional] 
**subjects** | **List[UUID]** | The users and groups the rule is stored for, given by their IDs. This is the whole allow-list that is to hold  afterwards and not a list of additions - what was stored before is dropped. Leaving it out applies `enabled`  to everyone and skips the audit trail entry, while sending it empty stores access for everyone. | [optional] 

## Example

```python
from docspace_api_sdk.models.web_item_security_requests_dto import WebItemSecurityRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebItemSecurityRequestsDto from a JSON string
web_item_security_requests_dto_instance = WebItemSecurityRequestsDto.from_json(json)
# print the JSON string representation of the object
print(WebItemSecurityRequestsDto.to_json())

# convert the object into a dict
web_item_security_requests_dto_dict = web_item_security_requests_dto_instance.to_dict()
# create an instance of WebItemSecurityRequestsDto from a dict
web_item_security_requests_dto_from_dict = WebItemSecurityRequestsDto.from_dict(web_item_security_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


