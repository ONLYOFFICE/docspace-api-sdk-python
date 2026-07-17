# MessageContentDto
The base class for message content blocks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**MessageContentType**](MessageContentType.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.message_content_dto import MessageContentDto

# TODO update the JSON string below
json = "{}"
# create an instance of MessageContentDto from a JSON string
message_content_dto_instance = MessageContentDto.from_json(json)
# print the JSON string representation of the object
print(MessageContentDto.to_json())

# convert the object into a dict
message_content_dto_dict = message_content_dto_instance.to_dict()
# create an instance of MessageContentDto from a dict
message_content_dto_from_dict = MessageContentDto.from_dict(message_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


