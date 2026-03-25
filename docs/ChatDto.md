# ChatDto
The chat session information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The unique identifier of the AI chat session. | [optional] 
**title** | **str** | The display title of the chat session. | [optional] 
**created_on** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**modified_on** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**created_by** | [**EmployeeDto**](EmployeeDto.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.chat_dto import ChatDto

# TODO update the JSON string below
json = "{}"
# create an instance of ChatDto from a JSON string
chat_dto_instance = ChatDto.from_json(json)
# print the JSON string representation of the object
print(ChatDto.to_json())

# convert the object into a dict
chat_dto_dict = chat_dto_instance.to_dict()
# create an instance of ChatDto from a dict
chat_dto_from_dict = ChatDto.from_dict(chat_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


