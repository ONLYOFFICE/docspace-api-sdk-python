# StorageArrayWrapper
The successful API response containing the list of StorageDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[StorageDto]**](StorageDto.md) | The list of StorageDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.storage_array_wrapper import StorageArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of StorageArrayWrapper from a JSON string
storage_array_wrapper_instance = StorageArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(StorageArrayWrapper.to_json())

# convert the object into a dict
storage_array_wrapper_dict = storage_array_wrapper_instance.to_dict()
# create an instance of StorageArrayWrapper from a dict
storage_array_wrapper_from_dict = StorageArrayWrapper.from_dict(storage_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


