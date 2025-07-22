# SecurityRequestsDto
The request parameters for managing user security and access permissions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | The product ID for which permissions are being set. | 
**user_id** | **str** | The ID of the user whose permissions are being configured. | 
**administrator** | **bool** | Specifies whether the user has administrative privileges. | [optional] 

## Example

```python
from docspace-api-sdk.models.security_requests_dto import SecurityRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRequestsDto from a JSON string
security_requests_dto_instance = SecurityRequestsDto.from_json(json)
# print the JSON string representation of the object
print(SecurityRequestsDto.to_json())

# convert the object into a dict
security_requests_dto_dict = security_requests_dto_instance.to_dict()
# create an instance of SecurityRequestsDto from a dict
security_requests_dto_from_dict = SecurityRequestsDto.from_dict(security_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


