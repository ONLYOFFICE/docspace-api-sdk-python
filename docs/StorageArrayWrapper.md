# StorageArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[StorageDto]**](StorageDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

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


