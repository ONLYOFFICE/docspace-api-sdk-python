# StorageRequestsDto

The request parameters for configuring the storage module settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | **str** | The name for the storage module to be configured. | 
**props** | [**List[ItemKeyValuePairStringString]**](ItemKeyValuePairStringString.md) | The list of configuration key-value pairs for the storage module. | [optional] 

## Example

```python
from docspace.models.storage_requests_dto import StorageRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of StorageRequestsDto from a JSON string
storage_requests_dto_instance = StorageRequestsDto.from_json(json)
# print the JSON string representation of the object
print(StorageRequestsDto.to_json())

# convert the object into a dict
storage_requests_dto_dict = storage_requests_dto_instance.to_dict()
# create an instance of StorageRequestsDto from a dict
storage_requests_dto_from_dict = StorageRequestsDto.from_dict(storage_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


