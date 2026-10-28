# ConfirmWrapper
The successful API response containing the ConfirmDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ConfirmDto**](ConfirmDto.md) | The ConfirmDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.confirm_wrapper import ConfirmWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmWrapper from a JSON string
confirm_wrapper_instance = ConfirmWrapper.from_json(json)
# print the JSON string representation of the object
print(ConfirmWrapper.to_json())

# convert the object into a dict
confirm_wrapper_dict = confirm_wrapper_instance.to_dict()
# create an instance of ConfirmWrapper from a dict
confirm_wrapper_from_dict = ConfirmWrapper.from_dict(confirm_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


