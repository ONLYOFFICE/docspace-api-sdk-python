# ConversationResultArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[ConversationResultDto]**](ConversationResultDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.conversation_result_array_wrapper import ConversationResultArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationResultArrayWrapper from a JSON string
conversation_result_array_wrapper_instance = ConversationResultArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(ConversationResultArrayWrapper.to_json())

# convert the object into a dict
conversation_result_array_wrapper_dict = conversation_result_array_wrapper_instance.to_dict()
# create an instance of ConversationResultArrayWrapper from a dict
conversation_result_array_wrapper_from_dict = ConversationResultArrayWrapper.from_dict(conversation_result_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


