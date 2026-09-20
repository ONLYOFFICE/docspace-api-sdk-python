# CreateApiKeyRequestDto
The request parameters for creating a new API key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The label that tells this key apart in the key list. It is required, may be up to 30 characters long, and does  not have to be unique. | 
**permissions** | **List[str]** | The scopes the key may use. Every value has to come from `GET api/2.0/keys/permissions`, an unknown value or  an empty array is rejected, and passing `*` or omitting the field records a key without scope restrictions. | [optional] 
**expires_in_days** | **int** | The lifetime of the key in days, counted from the moment it is created, from 1 to 365. Omit it to create a key  that never expires. | [optional] 

## Example

```python
from docspace_api_sdk.models.create_api_key_request_dto import CreateApiKeyRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApiKeyRequestDto from a JSON string
create_api_key_request_dto_instance = CreateApiKeyRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateApiKeyRequestDto.to_json())

# convert the object into a dict
create_api_key_request_dto_dict = create_api_key_request_dto_instance.to_dict()
# create an instance of CreateApiKeyRequestDto from a dict
create_api_key_request_dto_from_dict = CreateApiKeyRequestDto.from_dict(create_api_key_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


