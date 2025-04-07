# WebItemsSecurityRequestsDto

Module request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ItemKeyValuePairStringBoolean]**](ItemKeyValuePairStringBoolean.md) | Products with security information | [optional] 

## Example

```python
from docspace.models.web_items_security_requests_dto import WebItemsSecurityRequestsDto

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


