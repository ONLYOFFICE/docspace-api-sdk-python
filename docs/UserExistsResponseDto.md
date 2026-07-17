# UserExistsResponseDto
The user existence check response parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exists** | **bool** | Specifies whether the user exists or not. | 
**status** | [**EmployeeStatus**](EmployeeStatus.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.user_exists_response_dto import UserExistsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserExistsResponseDto from a JSON string
user_exists_response_dto_instance = UserExistsResponseDto.from_json(json)
# print the JSON string representation of the object
print(UserExistsResponseDto.to_json())

# convert the object into a dict
user_exists_response_dto_dict = user_exists_response_dto_instance.to_dict()
# create an instance of UserExistsResponseDto from a dict
user_exists_response_dto_from_dict = UserExistsResponseDto.from_dict(user_exists_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


