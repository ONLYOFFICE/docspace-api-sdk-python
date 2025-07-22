# AnonymousConfigDto
The anonymous config parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **bool** | Specifies if the anonymous is a request. | [optional] 

## Example

```python
from docspace-api-sdk.models.anonymous_config_dto import AnonymousConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of AnonymousConfigDto from a JSON string
anonymous_config_dto_instance = AnonymousConfigDto.from_json(json)
# print the JSON string representation of the object
print(AnonymousConfigDto.to_json())

# convert the object into a dict
anonymous_config_dto_dict = anonymous_config_dto_instance.to_dict()
# create an instance of AnonymousConfigDto from a dict
anonymous_config_dto_from_dict = AnonymousConfigDto.from_dict(anonymous_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


