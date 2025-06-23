# AuthServiceRequestsDto

The request parameters for handling the authorization service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the authentication service. | [optional] 
**title** | **str** | The user-friendly display title of the authentication service. | [optional] 
**description** | **str** | The brief description of the authentication service. | [optional] 
**instruction** | **str** | The detailed instructions for configuring or using the authentication service. | [optional] 
**can_set** | **bool** | Specifies whether the authentication service can be configured by the user. | [optional] 
**props** | [**List[AuthKey]**](AuthKey.md) | The collection of authorization keys associated with the authentication service. | [optional] 

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


