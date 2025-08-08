# RoomSecurityDto
The room security parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[FileShareDto]**](FileShareDto.md) | The list of room members. | [optional] 
**warning** | **str** | The warning message. | [optional] 
**error** | [**RoomSecurityError**](RoomSecurityError.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.room_security_dto import RoomSecurityDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoomSecurityDto from a JSON string
room_security_dto_instance = RoomSecurityDto.from_json(json)
# print the JSON string representation of the object
print(RoomSecurityDto.to_json())

# convert the object into a dict
room_security_dto_dict = room_security_dto_instance.to_dict()
# create an instance of RoomSecurityDto from a dict
room_security_dto_from_dict = RoomSecurityDto.from_dict(room_security_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


