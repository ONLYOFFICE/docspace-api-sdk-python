# ApiKeyResponseDto

The response data for the API key operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the API key. | [optional] 
**name** | **str** | The API key name. | [optional] 
**key** | **str** | The full API key value (only returned when creating a new key). | [optional] 
**key_postfix** | **str** | The API key postfix (used for identification). | [optional] 
**permissions** | **List[str]** | The list of permissions granted to the API key. | [optional] 
**last_used** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**create_on** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**create_by** | [**EmployeeDto**](EmployeeDto.md) |  | [optional] 
**expires_at** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**is_active** | **bool** | Indicates whether the API key is active or not. | [optional] 

## Example

```python
from docspace.models.api_key_response_dto import ApiKeyResponseDto

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


