# WebItemSecurityRequestsDto

The request parameters for configuring security settings of a single web module.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The module ID. | 
**enabled** | **bool** | Controls whether the security restrictions are enforced for this module. | [optional] 
**subjects** | **List[str]** | The collection of user and group identifiers granted access to the module. | [optional] 

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


