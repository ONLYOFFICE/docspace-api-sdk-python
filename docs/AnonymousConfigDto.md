# AnonymousConfigDto
How the editors treat a participant who opened the document without an account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **bool** | Whether the editors ask an anonymous participant for a display name before letting them in. It follows the  chat permission of the document, since a nameless participant cannot take part in one. | 

## Example

```python
from docspace_api_sdk.models.anonymous_config_dto import AnonymousConfigDto

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


