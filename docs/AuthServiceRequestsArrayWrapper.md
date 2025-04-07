# AuthServiceRequestsArrayWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[AuthServiceRequestsDto]**](AuthServiceRequestsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.auth_service_requests_array_wrapper import AuthServiceRequestsArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AuthServiceRequestsArrayWrapper from a JSON string
auth_service_requests_array_wrapper_instance = AuthServiceRequestsArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(AuthServiceRequestsArrayWrapper.to_json())

# convert the object into a dict
auth_service_requests_array_wrapper_dict = auth_service_requests_array_wrapper_instance.to_dict()
# create an instance of AuthServiceRequestsArrayWrapper from a dict
auth_service_requests_array_wrapper_from_dict = AuthServiceRequestsArrayWrapper.from_dict(auth_service_requests_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


