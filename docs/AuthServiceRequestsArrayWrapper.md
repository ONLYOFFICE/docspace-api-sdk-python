# AuthServiceRequestsArrayWrapper
The successful API response containing the list of AuthServiceRequestsDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[AuthServiceRequestsDto]**](AuthServiceRequestsDto.md) | The list of AuthServiceRequestsDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.auth_service_requests_array_wrapper import AuthServiceRequestsArrayWrapper

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


