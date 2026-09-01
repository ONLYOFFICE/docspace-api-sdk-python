# FileLinkWrapper
The successful API response containing the FileLink object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FileLink**](FileLink.md) | The FileLink object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.file_link_wrapper import FileLinkWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FileLinkWrapper from a JSON string
file_link_wrapper_instance = FileLinkWrapper.from_json(json)
# print the JSON string representation of the object
print(FileLinkWrapper.to_json())

# convert the object into a dict
file_link_wrapper_dict = file_link_wrapper_instance.to_dict()
# create an instance of FileLinkWrapper from a dict
file_link_wrapper_from_dict = FileLinkWrapper.from_dict(file_link_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


