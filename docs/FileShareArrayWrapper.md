# FileShareArrayWrapper
The successful API response containing the list of FileShareDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[FileShareDto]**](FileShareDto.md) | The list of FileShareDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.file_share_array_wrapper import FileShareArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FileShareArrayWrapper from a JSON string
file_share_array_wrapper_instance = FileShareArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(FileShareArrayWrapper.to_json())

# convert the object into a dict
file_share_array_wrapper_dict = file_share_array_wrapper_instance.to_dict()
# create an instance of FileShareArrayWrapper from a dict
file_share_array_wrapper_from_dict = FileShareArrayWrapper.from_dict(file_share_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


