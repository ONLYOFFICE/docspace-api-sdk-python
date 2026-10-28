# ConversationResultArrayWrapper
The successful API response containing the list of ConversationResultDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[ConversationResultDto]**](ConversationResultDto.md) | The list of ConversationResultDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.conversation_result_array_wrapper import ConversationResultArrayWrapper

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


