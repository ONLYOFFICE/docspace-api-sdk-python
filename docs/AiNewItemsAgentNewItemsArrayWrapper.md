# AiNewItemsAgentNewItemsArrayWrapper
The successful API response containing the list of NewItemsDtoAgentNewItemsDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[AiNewItemsDtoAgentNewItemsDto]**](AiNewItemsDtoAgentNewItemsDto.md) | The list of NewItemsDtoAgentNewItemsDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_new_items_agent_new_items_array_wrapper import AiNewItemsAgentNewItemsArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AiNewItemsAgentNewItemsArrayWrapper from a JSON string
ai_new_items_agent_new_items_array_wrapper_instance = AiNewItemsAgentNewItemsArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(AiNewItemsAgentNewItemsArrayWrapper.to_json())

# convert the object into a dict
ai_new_items_agent_new_items_array_wrapper_dict = ai_new_items_agent_new_items_array_wrapper_instance.to_dict()
# create an instance of AiNewItemsAgentNewItemsArrayWrapper from a dict
ai_new_items_agent_new_items_array_wrapper_from_dict = AiNewItemsAgentNewItemsArrayWrapper.from_dict(ai_new_items_agent_new_items_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


