# CspWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CspDto**](CspDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.csp_wrapper import CspWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CspWrapper from a JSON string
csp_wrapper_instance = CspWrapper.from_json(json)
# print the JSON string representation of the object
print(CspWrapper.to_json())

# convert the object into a dict
csp_wrapper_dict = csp_wrapper_instance.to_dict()
# create an instance of CspWrapper from a dict
csp_wrapper_from_dict = CspWrapper.from_dict(csp_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


