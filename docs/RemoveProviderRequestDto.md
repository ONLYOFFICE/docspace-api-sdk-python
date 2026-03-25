# RemoveProviderRequestDto
Request parameters for deleting one or more AI providers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | The set of AI provider identifiers to delete. | 

## Example

```python
from docspace_api_sdk.models.remove_provider_request_dto import RemoveProviderRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveProviderRequestDto from a JSON string
remove_provider_request_dto_instance = RemoveProviderRequestDto.from_json(json)
# print the JSON string representation of the object
print(RemoveProviderRequestDto.to_json())

# convert the object into a dict
remove_provider_request_dto_dict = remove_provider_request_dto_instance.to_dict()
# create an instance of RemoveProviderRequestDto from a dict
remove_provider_request_dto_from_dict = RemoveProviderRequestDto.from_dict(remove_provider_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


