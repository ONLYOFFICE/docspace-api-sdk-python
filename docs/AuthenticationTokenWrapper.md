# AuthenticationTokenWrapper
The successful API response containing the AuthenticationTokenDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**AuthenticationTokenDto**](AuthenticationTokenDto.md) | The AuthenticationTokenDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.authentication_token_wrapper import AuthenticationTokenWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationTokenWrapper from a JSON string
authentication_token_wrapper_instance = AuthenticationTokenWrapper.from_json(json)
# print the JSON string representation of the object
print(AuthenticationTokenWrapper.to_json())

# convert the object into a dict
authentication_token_wrapper_dict = authentication_token_wrapper_instance.to_dict()
# create an instance of AuthenticationTokenWrapper from a dict
authentication_token_wrapper_from_dict = AuthenticationTokenWrapper.from_dict(authentication_token_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


