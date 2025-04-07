# AuthServiceRequestsDto

Request parameters for authorization service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**title** | **str** | Title | [optional] 
**description** | **str** | Description | [optional] 
**instruction** | **str** | Instruction | [optional] 
**can_set** | **bool** | Specifies if the authentication service can be set or not | [optional] 
**props** | [**List[AuthKey]**](AuthKey.md) | List of authorization keys | [optional] 

## Example

```python
from docspace.models.auth_service_requests_dto import AuthServiceRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthServiceRequestsDto from a JSON string
auth_service_requests_dto_instance = AuthServiceRequestsDto.from_json(json)
# print the JSON string representation of the object
print(AuthServiceRequestsDto.to_json())

# convert the object into a dict
auth_service_requests_dto_dict = auth_service_requests_dto_instance.to_dict()
# create an instance of AuthServiceRequestsDto from a dict
auth_service_requests_dto_from_dict = AuthServiceRequestsDto.from_dict(auth_service_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


