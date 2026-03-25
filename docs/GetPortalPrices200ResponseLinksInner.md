# GetPortalPrices200ResponseLinksInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URL of the link | [optional] 
**action** | **str** | Action associated with the link | [optional] 

## Example

```python
from docspace_api_sdk.models.get_portal_prices200_response_links_inner import GetPortalPrices200ResponseLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPortalPrices200ResponseLinksInner from a JSON string
get_portal_prices200_response_links_inner_instance = GetPortalPrices200ResponseLinksInner.from_json(json)
# print the JSON string representation of the object
print(GetPortalPrices200ResponseLinksInner.to_json())

# convert the object into a dict
get_portal_prices200_response_links_inner_dict = get_portal_prices200_response_links_inner_instance.to_dict()
# create an instance of GetPortalPrices200ResponseLinksInner from a dict
get_portal_prices200_response_links_inner_from_dict = GetPortalPrices200ResponseLinksInner.from_dict(get_portal_prices200_response_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


