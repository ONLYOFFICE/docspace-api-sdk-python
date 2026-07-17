# IPRestrictionArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[IPRestriction]**](IPRestriction.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.ip_restriction_array_wrapper import IPRestrictionArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of IPRestrictionArrayWrapper from a JSON string
ip_restriction_array_wrapper_instance = IPRestrictionArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(IPRestrictionArrayWrapper.to_json())

# convert the object into a dict
ip_restriction_array_wrapper_dict = ip_restriction_array_wrapper_instance.to_dict()
# create an instance of IPRestrictionArrayWrapper from a dict
ip_restriction_array_wrapper_from_dict = IPRestrictionArrayWrapper.from_dict(ip_restriction_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


