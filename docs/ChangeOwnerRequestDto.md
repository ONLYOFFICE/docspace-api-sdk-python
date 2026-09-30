# ChangeOwnerRequestDto
The rooms and files to hand over, together with the account that takes them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_ids** | [**List[BatchRequestDtoAllOfFileIds]**](BatchRequestDtoAllOfFileIds.md) | The rooms to hand over, identified as `GET api/2.0/files/rooms` returns them - a number for a room stored on  the portal and a string for one that lives on a connected third-party account. Only rooms belong here; a  folder inside a room is refused. | [optional] 
**file_ids** | [**List[BatchRequestDtoAllOfFileIds]**](BatchRequestDtoAllOfFileIds.md) | The files to hand over, identified as a listing operation returns them - a number for a file stored on the  portal and a string for one on a connected third-party account. Only a file kept in the portal's common  section is accepted. | [optional] 
**user_id** | **UUID** | The account that becomes the owner of every listed entry. It has to be an active member allowed to manage  rooms, so a deactivated account, a guest or a plain member is rejected, and for a private room the account  must have set up its encryption keys beforehand. | 

## Example

```python
from docspace_api_sdk.models.change_owner_request_dto import ChangeOwnerRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeOwnerRequestDto from a JSON string
change_owner_request_dto_instance = ChangeOwnerRequestDto.from_json(json)
# print the JSON string representation of the object
print(ChangeOwnerRequestDto.to_json())

# convert the object into a dict
change_owner_request_dto_dict = change_owner_request_dto_instance.to_dict()
# create an instance of ChangeOwnerRequestDto from a dict
change_owner_request_dto_from_dict = ChangeOwnerRequestDto.from_dict(change_owner_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


