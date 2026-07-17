# ChatWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ChatDto**](ChatDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.chat_wrapper import ChatWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ChatWrapper from a JSON string
chat_wrapper_instance = ChatWrapper.from_json(json)
# print the JSON string representation of the object
print(ChatWrapper.to_json())

# convert the object into a dict
chat_wrapper_dict = chat_wrapper_instance.to_dict()
# create an instance of ChatWrapper from a dict
chat_wrapper_from_dict = ChatWrapper.from_dict(chat_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


