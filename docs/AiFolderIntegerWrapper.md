# AiFolderIntegerWrapper
The successful API response containing the FolderDtoInteger object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**AiFolderDtoInteger**](AiFolderDtoInteger.md) | The FolderDtoInteger object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_folder_integer_wrapper import AiFolderIntegerWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AiFolderIntegerWrapper from a JSON string
ai_folder_integer_wrapper_instance = AiFolderIntegerWrapper.from_json(json)
# print the JSON string representation of the object
print(AiFolderIntegerWrapper.to_json())

# convert the object into a dict
ai_folder_integer_wrapper_dict = ai_folder_integer_wrapper_instance.to_dict()
# create an instance of AiFolderIntegerWrapper from a dict
ai_folder_integer_wrapper_from_dict = AiFolderIntegerWrapper.from_dict(ai_folder_integer_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


