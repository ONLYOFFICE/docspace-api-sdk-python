# ThirdPartyChunkedUploadSessionResponseResponseWrapper
The successful API response containing the ThirdPartyChunkedUploadSessionResponse object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ThirdPartyChunkedUploadSessionResponse**](ThirdPartyChunkedUploadSessionResponse.md) | The ThirdPartyChunkedUploadSessionResponse object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.third_party_chunked_upload_session_response_response_wrapper import ThirdPartyChunkedUploadSessionResponseResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyChunkedUploadSessionResponseResponseWrapper from a JSON string
third_party_chunked_upload_session_response_response_wrapper_instance = ThirdPartyChunkedUploadSessionResponseResponseWrapper.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyChunkedUploadSessionResponseResponseWrapper.to_json())

# convert the object into a dict
third_party_chunked_upload_session_response_response_wrapper_dict = third_party_chunked_upload_session_response_response_wrapper_instance.to_dict()
# create an instance of ThirdPartyChunkedUploadSessionResponseResponseWrapper from a dict
third_party_chunked_upload_session_response_response_wrapper_from_dict = ThirdPartyChunkedUploadSessionResponseResponseWrapper.from_dict(third_party_chunked_upload_session_response_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


