# MessageDto
The chat message information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the message. | [optional] 
**role** | [**Role**](Role.md) |  | [optional] 
**contents** | [**List[MessageContentDto]**](MessageContentDto.md) | The ordered collection of content blocks that make up the message body (text, tool calls, or attachments). | [optional] 
**created_on** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.message_dto import MessageDto

# TODO update the JSON string below
json = "{}"
# create an instance of MessageDto from a JSON string
message_dto_instance = MessageDto.from_json(json)
# print the JSON string representation of the object
print(MessageDto.to_json())

# convert the object into a dict
message_dto_dict = message_dto_instance.to_dict()
# create an instance of MessageDto from a dict
message_dto_from_dict = MessageDto.from_dict(message_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


