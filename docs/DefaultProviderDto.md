# DefaultProviderDto
Default AI provider information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **int** | AI provider identifier. | [optional] 
**default_model** | **str** | Default model identifier used with this provider. | 
**provider_title** | **str** | AI provider title. | [optional] 

## Example

```python
from docspace_api_sdk.models.default_provider_dto import DefaultProviderDto

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultProviderDto from a JSON string
default_provider_dto_instance = DefaultProviderDto.from_json(json)
# print the JSON string representation of the object
print(DefaultProviderDto.to_json())

# convert the object into a dict
default_provider_dto_dict = default_provider_dto_instance.to_dict()
# create an instance of DefaultProviderDto from a dict
default_provider_dto_from_dict = DefaultProviderDto.from_dict(default_provider_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


