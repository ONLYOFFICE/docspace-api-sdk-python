# CapabilitiesWrapper
The successful API response containing the CapabilitiesDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CapabilitiesDto**](CapabilitiesDto.md) | The CapabilitiesDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.capabilities_wrapper import CapabilitiesWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesWrapper from a JSON string
capabilities_wrapper_instance = CapabilitiesWrapper.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesWrapper.to_json())

# convert the object into a dict
capabilities_wrapper_dict = capabilities_wrapper_instance.to_dict()
# create an instance of CapabilitiesWrapper from a dict
capabilities_wrapper_from_dict = CapabilitiesWrapper.from_dict(capabilities_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


