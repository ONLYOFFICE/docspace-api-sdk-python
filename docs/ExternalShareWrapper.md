# ExternalShareWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ExternalShareDto**](ExternalShareDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.external_share_wrapper import ExternalShareWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalShareWrapper from a JSON string
external_share_wrapper_instance = ExternalShareWrapper.from_json(json)
# print the JSON string representation of the object
print(ExternalShareWrapper.to_json())

# convert the object into a dict
external_share_wrapper_dict = external_share_wrapper_instance.to_dict()
# create an instance of ExternalShareWrapper from a dict
external_share_wrapper_from_dict = ExternalShareWrapper.from_dict(external_share_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


