# CreateProviderRequestDto
Request parameters for creating a new AI provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ProviderType**](ProviderType.md) |  | [optional] 
**title** | **str** | The display title for the AI provider. | 
**url** | **str** | The API endpoint URL for the AI provider. Required for OpenAiCompatible type; optional for other types that have default URLs. | [optional] 
**key** | **str** | The authentication API key for the AI provider. | 

## Example

```python
from docspace_api_sdk.models.create_provider_request_dto import CreateProviderRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProviderRequestDto from a JSON string
create_provider_request_dto_instance = CreateProviderRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateProviderRequestDto.to_json())

# convert the object into a dict
create_provider_request_dto_dict = create_provider_request_dto_instance.to_dict()
# create an instance of CreateProviderRequestDto from a dict
create_provider_request_dto_from_dict = CreateProviderRequestDto.from_dict(create_provider_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


