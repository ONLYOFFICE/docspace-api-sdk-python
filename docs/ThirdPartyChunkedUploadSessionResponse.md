# ThirdPartyChunkedUploadSessionResponse
The reserved chunked upload: where the parts are sent, how much was declared and when the reservation lapses. No  content of the file is described here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the reserved upload, repeated in the path of every call that follows it - the chunk uploads,  the finalize and the abort. It is thirty-two hexadecimal characters without separators, and it is the only  thing the server checks, so anyone holding it can write into this upload. | [optional] 
**path** | **List[str]** | The chain of folders leading to the destination, outermost first and the destination itself last, with folders  the caller cannot read left out. An answer that reports a stored part carries the destination folder alone  instead of the whole chain. | [optional] 
**created** | **datetime** | The moment the upload was reserved, in UTC. | [optional] 
**expired** | **datetime** | The moment the reservation lapses and the parts buffered for it are dropped, in UTC. It is a gap rather than a  deadline for the whole transfer: every accepted part pushes it twelve hours past that part, so only a long  silence loses the upload. | [optional] 
**location** | **str** | The absolute address of the separate chunk handler that also accepts the parts of this upload, kept for  clients written against it. A caller working through this API does not need it and sends the parts to the  session operations instead. | [optional] 
**bytes_total** | **int** | The size in bytes that was declared when the upload was reserved, echoed back. It is what the arriving parts  are counted against to decide the file is complete, not the amount received so far. | [optional] 

## Example

```python
from docspace_api_sdk.models.third_party_chunked_upload_session_response import ThirdPartyChunkedUploadSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyChunkedUploadSessionResponse from a JSON string
third_party_chunked_upload_session_response_instance = ThirdPartyChunkedUploadSessionResponse.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyChunkedUploadSessionResponse.to_json())

# convert the object into a dict
third_party_chunked_upload_session_response_dict = third_party_chunked_upload_session_response_instance.to_dict()
# create an instance of ThirdPartyChunkedUploadSessionResponse from a dict
third_party_chunked_upload_session_response_from_dict = ThirdPartyChunkedUploadSessionResponse.from_dict(third_party_chunked_upload_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


