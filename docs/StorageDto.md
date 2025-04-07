# StorageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**title** | **str** | Title | [optional] 
**properties** | [**List[AuthKey]**](AuthKey.md) | List of authentication keys | [optional] 
**current** | **bool** | Specifies if this is the current storage or not | [optional] 
**is_set** | **bool** | Specifies if this storage can be set or not | [optional] 

## Example

```python
from docspace.models.storage_dto import StorageDto

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDto from a JSON string
storage_dto_instance = StorageDto.from_json(json)
# print the JSON string representation of the object
print(StorageDto.to_json())

# convert the object into a dict
storage_dto_dict = storage_dto_instance.to_dict()
# create an instance of StorageDto from a dict
storage_dto_from_dict = StorageDto.from_dict(storage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


