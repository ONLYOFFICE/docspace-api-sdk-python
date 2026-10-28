# UserExistsResponseWrapper
The successful API response containing the UserExistsResponseDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**UserExistsResponseDto**](UserExistsResponseDto.md) | The UserExistsResponseDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.user_exists_response_wrapper import UserExistsResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of UserExistsResponseWrapper from a JSON string
user_exists_response_wrapper_instance = UserExistsResponseWrapper.from_json(json)
# print the JSON string representation of the object
print(UserExistsResponseWrapper.to_json())

# convert the object into a dict
user_exists_response_wrapper_dict = user_exists_response_wrapper_instance.to_dict()
# create an instance of UserExistsResponseWrapper from a dict
user_exists_response_wrapper_from_dict = UserExistsResponseWrapper.from_dict(user_exists_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


