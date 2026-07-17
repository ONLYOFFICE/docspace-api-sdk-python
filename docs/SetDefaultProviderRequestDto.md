# SetDefaultProviderRequestDto
Request parameters for setting the default AI provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **int** | AI provider identifier. | [optional] 
**default_model** | **str** | Default model identifier to use with this provider. | 

## Example

```python
from docspace_api_sdk.models.set_default_provider_request_dto import SetDefaultProviderRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetDefaultProviderRequestDto from a JSON string
set_default_provider_request_dto_instance = SetDefaultProviderRequestDto.from_json(json)
# print the JSON string representation of the object
print(SetDefaultProviderRequestDto.to_json())

# convert the object into a dict
set_default_provider_request_dto_dict = set_default_provider_request_dto_instance.to_dict()
# create an instance of SetDefaultProviderRequestDto from a dict
set_default_provider_request_dto_from_dict = SetDefaultProviderRequestDto.from_dict(set_default_provider_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


