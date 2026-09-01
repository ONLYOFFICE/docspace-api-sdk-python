# ApiKeyResponseDto
The response data for the API key operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The API key unique identifier. | 
**name** | **str** | The API key name. | 
**key** | **str** | The full API key value (only returned when creating a new key). | 
**key_postfix** | **str** | The API key postfix (used for identification). | [optional] 
**permissions** | **List[str]** | The list of permissions granted to the API key. | 
**last_used** | **datetime** | The date and time when the API key was last used. | [optional] 
**create_on** | **datetime** | The date and time when the API key was created. | [optional] 
**create_by** | [**EmployeeDto**](EmployeeDto.md) | The identifier of the user who created the API key. | [optional] 
**expires_at** | **datetime** | The date and time when the API key expires. | [optional] 
**is_active** | **bool** | Indicates whether the API key is active or not. | 

## Example

```python
from docspace_api_sdk.models.api_key_response_dto import ApiKeyResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyResponseDto from a JSON string
api_key_response_dto_instance = ApiKeyResponseDto.from_json(json)
# print the JSON string representation of the object
print(ApiKeyResponseDto.to_json())

# convert the object into a dict
api_key_response_dto_dict = api_key_response_dto_instance.to_dict()
# create an instance of ApiKeyResponseDto from a dict
api_key_response_dto_from_dict = ApiKeyResponseDto.from_dict(api_key_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


