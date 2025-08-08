# ConversationResultDto
The result of file convertion operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The conversion operation ID. | [optional] 
**operation** | [**FileOperationType**](FileOperationType.md) |  | [optional] 
**progress** | **int** | The conversion operation progress. | [optional] 
**source** | **str** | The source file for the conversion. | [optional] 
**result** | **object** | The resulting file after the conversion. | [optional] 
**error** | **str** | The conversion operation error message. | [optional] 
**processed** | **str** | Specifies if the conversion operation is processed or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.conversation_result_dto import ConversationResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationResultDto from a JSON string
conversation_result_dto_instance = ConversationResultDto.from_json(json)
# print the JSON string representation of the object
print(ConversationResultDto.to_json())

# convert the object into a dict
conversation_result_dto_dict = conversation_result_dto_instance.to_dict()
# create an instance of ConversationResultDto from a dict
conversation_result_dto_from_dict = ConversationResultDto.from_dict(conversation_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


