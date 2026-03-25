# FileIntegerWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FileDtoInteger**](FileDtoInteger.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.file_integer_wrapper import FileIntegerWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FileIntegerWrapper from a JSON string
file_integer_wrapper_instance = FileIntegerWrapper.from_json(json)
# print the JSON string representation of the object
print(FileIntegerWrapper.to_json())

# convert the object into a dict
file_integer_wrapper_dict = file_integer_wrapper_instance.to_dict()
# create an instance of FileIntegerWrapper from a dict
file_integer_wrapper_from_dict = FileIntegerWrapper.from_dict(file_integer_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


