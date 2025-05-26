# CreateApiKeyRequestDto

The request parameters for creating a new API key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The API key name. | 
**permissions** | **List[str]** | The list of permissions granted to the API key. | [optional] 
**expires_in_days** | **int** | The number of days until the API key expires (null for no expiration). | [optional] 

## Example

```python
from docspace.models.create_api_key_request_dto import CreateApiKeyRequestDto

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


