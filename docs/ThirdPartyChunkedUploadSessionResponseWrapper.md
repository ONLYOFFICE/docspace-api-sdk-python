# ThirdPartyChunkedUploadSessionResponseWrapper
The reserved chunked upload wrapped in the envelope the two older session operations answer with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Always true in a body that reaches the caller, because a call that does not succeed answers with an error  status and no body at all. It cannot be used to tell a refusal from a success. | [optional] 
**data** | [**ThirdPartyChunkedUploadSessionResponse**](ThirdPartyChunkedUploadSessionResponse.md) | The reserved upload itself, in the same shape the newer session operations answer with directly. | [optional] 

## Example

```python
from docspace_api_sdk.models.third_party_chunked_upload_session_response_wrapper import ThirdPartyChunkedUploadSessionResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyChunkedUploadSessionResponseWrapper from a JSON string
third_party_chunked_upload_session_response_wrapper_instance = ThirdPartyChunkedUploadSessionResponseWrapper.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyChunkedUploadSessionResponseWrapper.to_json())

# convert the object into a dict
third_party_chunked_upload_session_response_wrapper_dict = third_party_chunked_upload_session_response_wrapper_instance.to_dict()
# create an instance of ThirdPartyChunkedUploadSessionResponseWrapper from a dict
third_party_chunked_upload_session_response_wrapper_from_dict = ThirdPartyChunkedUploadSessionResponseWrapper.from_dict(third_party_chunked_upload_session_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


