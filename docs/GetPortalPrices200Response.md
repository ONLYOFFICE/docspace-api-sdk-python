# GetPortalPrices200Response
The successful API response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **Dict[str, float]** | The response payload. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.get_portal_prices200_response import GetPortalPrices200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPortalPrices200Response from a JSON string
get_portal_prices200_response_instance = GetPortalPrices200Response.from_json(json)
# print the JSON string representation of the object
print(GetPortalPrices200Response.to_json())

# convert the object into a dict
get_portal_prices200_response_dict = get_portal_prices200_response_instance.to_dict()
# create an instance of GetPortalPrices200Response from a dict
get_portal_prices200_response_from_dict = GetPortalPrices200Response.from_dict(get_portal_prices200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


