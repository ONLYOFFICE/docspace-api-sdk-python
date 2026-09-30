# ThirdPartyFolderWrapper
The successful API response containing the ThirdPartyFolderDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ThirdPartyFolderDto**](ThirdPartyFolderDto.md) | The ThirdPartyFolderDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.third_party_folder_wrapper import ThirdPartyFolderWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyFolderWrapper from a JSON string
third_party_folder_wrapper_instance = ThirdPartyFolderWrapper.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyFolderWrapper.to_json())

# convert the object into a dict
third_party_folder_wrapper_dict = third_party_folder_wrapper_instance.to_dict()
# create an instance of ThirdPartyFolderWrapper from a dict
third_party_folder_wrapper_from_dict = ThirdPartyFolderWrapper.from_dict(third_party_folder_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


