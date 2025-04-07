# ConversationResultDto

Result of file conversation operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Operation ID | [optional] 
**operation** | [**FileOperationType**](FileOperationType.md) |  | [optional] 
**progress** | **int** | Operation progress | [optional] 
**source** | **str** | Source file | [optional] 
**result** | **object** | Resulting file | [optional] 
**error** | **str** | Error | [optional] 
**processed** | **str** | Specifies if the operation is processed or not | [optional] 

## Example

```python
from docspace.models.conversation_result_dto import ConversationResultDto

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


