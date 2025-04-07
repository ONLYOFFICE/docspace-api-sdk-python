# WebItemSecurityRequestsDto

Module request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Module ID | [optional] 
**enabled** | **bool** | Specifies if the module security settings are enabled or not | [optional] 
**subjects** | **List[str]** | List of user/group IDs with the access to the module | [optional] 

## Example

```python
from docspace.models.web_item_security_requests_dto import WebItemSecurityRequestsDto

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


