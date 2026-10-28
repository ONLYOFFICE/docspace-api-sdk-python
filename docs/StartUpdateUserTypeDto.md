# StartUpdateUserTypeDto
The parameters for updating the type of the user or guest when reassigning rooms and shared files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EmployeeType**](EmployeeType.md) | The type to convert the account to. Only `Guest` and `User` are accepted, because they are the types that  cannot own rooms; `RoomAdmin`, `DocSpaceAdmin` and `All` are rejected here and belong to  `PUT api/2.0/people/type/{type}`. | [optional] 
**user_id** | **UUID** | The ID of the account being converted. It has to be an active account other than the caller, and only the  portal owner may pass the ID of a DocSpace administrator. | [optional] 
**reassign_user_id** | **UUID** | The ID of the administrator who receives the rooms and the shared files of the converted account. It has to be  an active room admin or DocSpace admin other than the converted account, and when it is omitted the data goes  to the caller. | [optional] 

## Example

```python
from docspace_api_sdk.models.start_update_user_type_dto import StartUpdateUserTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of StartUpdateUserTypeDto from a JSON string
start_update_user_type_dto_instance = StartUpdateUserTypeDto.from_json(json)
# print the JSON string representation of the object
print(StartUpdateUserTypeDto.to_json())

# convert the object into a dict
start_update_user_type_dto_dict = start_update_user_type_dto_instance.to_dict()
# create an instance of StartUpdateUserTypeDto from a dict
start_update_user_type_dto_from_dict = StartUpdateUserTypeDto.from_dict(start_update_user_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


