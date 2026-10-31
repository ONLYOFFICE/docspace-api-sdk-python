# AiAgentsGet200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**AiAgentsGet200ResponseAllOfResponse**](AiAgentsGet200ResponseAllOfResponse.md) |  | [optional] 
**count** | **int** | How many items this response carries: the length of the page for a list, 1 for a single object | [optional] 
**total** | **int** | How many items the whole list holds across all pages, for working out how many pages to request. Sent only by the operations that page their results, and left out of every other response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_agents_get200_response import AiAgentsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AiAgentsGet200Response from a JSON string
ai_agents_get200_response_instance = AiAgentsGet200Response.from_json(json)
# print the JSON string representation of the object
print(AiAgentsGet200Response.to_json())

# convert the object into a dict
ai_agents_get200_response_dict = ai_agents_get200_response_instance.to_dict()
# create an instance of AiAgentsGet200Response from a dict
ai_agents_get200_response_from_dict = AiAgentsGet200Response.from_dict(ai_agents_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


