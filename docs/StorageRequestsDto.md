# StorageRequestsDto

Storage settings request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | **str** | Storage name | [optional] 
**props** | [**List[ItemKeyValuePairStringString]**](ItemKeyValuePairStringString.md) | Storage properties | [optional] 

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


