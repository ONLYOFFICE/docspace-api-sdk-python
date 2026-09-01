# UploadSessionResponseIntegerWrapper
The successful API response containing the UploadSessionResponseDtoInteger object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**UploadSessionResponseDtoInteger**](UploadSessionResponseDtoInteger.md) | The UploadSessionResponseDtoInteger object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.upload_session_response_integer_wrapper import UploadSessionResponseIntegerWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSessionResponseIntegerWrapper from a JSON string
upload_session_response_integer_wrapper_instance = UploadSessionResponseIntegerWrapper.from_json(json)
# print the JSON string representation of the object
print(UploadSessionResponseIntegerWrapper.to_json())

# convert the object into a dict
upload_session_response_integer_wrapper_dict = upload_session_response_integer_wrapper_instance.to_dict()
# create an instance of UploadSessionResponseIntegerWrapper from a dict
upload_session_response_integer_wrapper_from_dict = UploadSessionResponseIntegerWrapper.from_dict(upload_session_response_integer_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


